import streamlit as st
from wiki_utils import search_wikipedia, scrape_wikipedia_page
from pdf_utils import save_to_pdf, process_pdf_file
from embeddings_utils import create_embeddings_and_query
from dotenv import load_dotenv

load_dotenv()

st.header("Chat with Docs")

# Select PDF source
pdf_source = st.selectbox("Get PDF from:", ["Local File", "Wikipedia"])

if pdf_source == "Local File":
    pdf_files = st.file_uploader("Upload your PDFs", type='pdf', accept_multiple_files=True)

    if pdf_files:
        texts = [process_pdf_file(pdf) for pdf in pdf_files if pdf]
        combined_text = '\n'.join(texts)
        
        if combined_text:
            query_input = st.text_input("Ask a question from your doc:", key="query_input")
            if query_input:
                response = create_embeddings_and_query(combined_text, query_input)
                st.write(response)
        else:
            st.error("Error processing PDF files.")

else:
    wikipedia_query = st.text_input("Enter Wikipedia query:")
    if wikipedia_query:
        url = search_wikipedia(wikipedia_query)
        
        if url:
            scraped_data = scrape_wikipedia_page(url)
            
            if scraped_data:
                pdf_filename = f"{scraped_data['title'].replace(' ', '_')}.pdf"
                save_to_pdf(scraped_data, pdf_filename)
                
                with open(pdf_filename, "rb") as f:
                    st.download_button("Download PDF", f, pdf_filename)

                text = process_pdf_file(open(pdf_filename, "rb"))
                
                if text:
                    query_input = st.text_input("Ask a question from your doc:", key="query_input")
                    if query_input:
                        response = create_embeddings_and_query(text, query_input)
                        st.write(response)
                else:
                    st.error("Error processing PDF file.")
            else:
                st.error("Failed to retrieve the page content.")
        else:
            st.error("Page not found!")
