import streamlit as st
import wikipedia
import requests
from bs4 import BeautifulSoup
from fpdf import FPDF
import os
from PyPDF2 import PdfReader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.llms.openai import OpenAI
from langchain.chains.question_answering import load_qa_chain
from dotenv import load_dotenv

load_dotenv()

# Wikipedia user/app initiation
wikipedia.set_user_agent('MyApp/1.0')

# Function to search for a Wikipedia page based on user query and return a URL
def search_wikipedia(query):
    try:
        results = wikipedia.search(query)
        if results:
            page_title = results[0]
            page = wikipedia.page(page_title)
            return page.url
        else:
            return None
    except wikipedia.exceptions.DisambiguationError as e:
        return None
    except wikipedia.exceptions.PageError:
        return None
    except Exception as e:
        return None

# Function to scrap a Wikipedia URL
def scrape_wikipedia_page(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        title = soup.find('h1', {'id': 'firstHeading'}).text
        content = soup.find('div', {'id': 'mw-content-text'})
        if content:
            paragraphs = content.find_all('p')
            page_content = '\n'.join([para.text for para in paragraphs])
            return {'title': title, 'content': page_content}
        else:
            return None
    else:
        return None

# Helper function for PDF embedding
def filter_text(text):
    return ''.join(char for char in text if ord(char) < 128)

def split_text_into_chunks(text, chunk_size):
    return [text[i:i + chunk_size] for i in range(0, len(text), chunk_size)]

# Save the scrapped data to a PDF
def save_to_pdf(data, filename):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.set_font("Arial", size=16, style='B')
    pdf.multi_cell(0, 10, filter_text(data['title']), align='C')
    pdf.ln(10)
    pdf.set_font("Arial", size=12)
    content = filter_text(data['content'])
    for chunk in split_text_into_chunks(content, 4000):
        pdf.multi_cell(0, 10, chunk)
        pdf.add_page()
    pdf.output(filename)

# Function to process PDF file
def process_pdf_file(pdf_file):
    try:
        pdf_reader = PdfReader(pdf_file)
        text = ""
        for page in pdf_reader.pages:
            text += page.extract_text()
        return text
    except Exception as e:
        st.write(f"Error processing PDF file: {e}")
        return None

def main():
    st.header("Chat with Docs ")

    # Select PDF source
    pdf_source = st.selectbox("Get PDF from:", ["Local File", "Wikipedia"])

    if pdf_source == "Local File":
        # upload multiple PDF files
        pdf_files = st.file_uploader("Upload your PDFs", type='pdf', accept_multiple_files=True)

        if pdf_files:
            texts = []
            for pdf_file in pdf_files:
                text = process_pdf_file(pdf_file)
                if text:
                    texts.append(text)
            if texts:
                # Combine texts into a single string
                text = '\n'.join(texts)

                # Split the txt into chunks    
                text_splitter = RecursiveCharacterTextSplitter(
                    chunk_size=500,
                    chunk_overlap=100,
                    length_function=len
                    )
                chunks = text_splitter.split_text(text=text)

                # embeddings and vectorstore
                embeddings = OpenAIEmbeddings()
                db = FAISS.from_texts(chunks, embeddings)

                #take user input and query it from the vector database
                query_input = st.text_input("Ask a question from your doc : ", key="query_input")
                if query_input:
                    try:
                        docs = db.similarity_search(query_input, 3)

                        # using an llm to generate human like responses after querying the data
                        llm = OpenAI(temperature=0)
                        chain = load_qa_chain(llm=llm, chain_type="stuff")
                        response = chain.invoke(input={"input_documents": docs, "question": query_input})
                        st.write(response)
                    except Exception as e:
                        st.write("Sorry, I couldn't generate a response to that question.")
            else:
                st.write("Error processing PDFfiles")
    else:
        # Get PDF from Wikipedia
        wikipedia_query = st.text_input("Enter Wikipedia query:")
        if wikipedia_query:
            try:
                url = search_wikipedia(wikipedia_query)
                if url:
                    scraped_data = scrape_wikipedia_page(url)
                    if scraped_data:
                        pdf_filename =f"{scraped_data['title'].replace(' ', '_')}.pdf"
                        save_to_pdf(scraped_data, pdf_filename)
                        with open(pdf_filename, "rb") as f:
                            st.download_button("Download PDF", f, pdf_filename)

                        # Process PDF text
                        pdf_file = open(pdf_filename, "rb")
                        text = process_pdf_file(pdf_file)
                        if text:
                            # Split the txt into chunks    
                            text_splitter = RecursiveCharacterTextSplitter(
                                chunk_size=500,
                                chunk_overlap=100,
                                length_function=len
                                )
                            chunks = text_splitter.split_text(text=text)

                            # embeddings and vectorstore
                            embeddings = OpenAIEmbeddings()
                            db = FAISS.from_texts(chunks, embeddings)

                            #take user input and query it from the vector database
                            query_input = st.text_input("Ask a question from your doc : ", key="query_input")
                            if query_input:
                                try:
                                    docs = db.similarity_search(query_input, 3)

                                    # using an llm to generate human like responses after querying the data
                                    llm = OpenAI(temperature=0)
                                    chain = load_qa_chain(llm=llm, chain_type="stuff")
                                    response = chain.invoke(input={"input_documents": docs, "question": query_input})
                                    st.write(response[2])
                                except Exception as e:
                                    st.write("Sorry, I couldn't generate a response to that question.")
                        else:
                            st.write("Error processing PDF file")
                    else:
                        st.error("Failed to retrieve the page content.")
                else:
                    st.error("Page not found!")
            except Exception as e:
                st.error("Sorry, there was an error retrieving the PDF from Wikipedia.")

if __name__ == '__main__':
    main()