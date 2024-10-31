from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.llms.openai import OpenAI
from langchain.chains.question_answering import load_qa_chain

def create_embeddings_and_query(text: str, query: str) -> str:
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=100)
    chunks = text_splitter.split_text(text)
    
    embeddings = OpenAIEmbeddings()
    db = FAISS.from_texts(chunks, embeddings)
    
    docs = db.similarity_search(query, 3)
    llm = OpenAI(temperature=0)
    chain = load_qa_chain(llm=llm, chain_type="stuff")
    response = chain.invoke(input={"input_documents": docs, "question": query})
    return response
