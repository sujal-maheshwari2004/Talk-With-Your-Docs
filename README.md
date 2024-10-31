# Chat with Docs

This is a Streamlit-based application that allows users to interact with PDF documents by querying content from uploaded PDFs or retrieving information from Wikipedia articles. Using embeddings and a question-answering model, users can ask questions about the document content for quick and contextual answers.

## Features

- **PDF Upload**: Upload multiple PDF files locally and ask questions based on their content.
- **Wikipedia Integration**: Search and download Wikipedia articles as PDFs, then ask questions about the article content.
- **Embeddings and Query System**: Uses embeddings to generate contextually relevant answers to user questions from the document content.
- **Downloadable Wikipedia PDFs**: Save Wikipedia article content as a PDF for offline use.

## Installation

### Prerequisites

- Python 3.8 or above
- [Streamlit](https://streamlit.io/)
- [PyPDF2](https://pypi.org/project/PyPDF2/)
- [FPDF](https://pypi.org/project/fpdf/)
- [BeautifulSoup](https://pypi.org/project/beautifulsoup4/)
- [Requests](https://pypi.org/project/requests/)
- [LangChain](https://pypi.org/project/langchain/)
- [FAISS](https://pypi.org/project/faiss-cpu/) (for local CPU-based usage)
- [dotenv](https://pypi.org/project/python-dotenv/)
- [Wikipedia-API](https://pypi.org/project/wikipedia-api/)

### Setting up the Project

1. **Clone the repository**:
   ```bash
   git clone https://github.com/sujal-maheshwari2004/Talk-With-Your-Docs.git
   cd chat-with-docs
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up OpenAI API Key**:
   - Create a `.env` file in the root directory.
   - Add your OpenAI API key:
     ```
     OPENAI_API_KEY=your_openai_api_key
     ```

4. **Run the Application**:
   ```bash
   streamlit run app.py
   ```

## Usage

1. **Select PDF Source**: Choose between uploading a local PDF file or searching for a Wikipedia article.
2. **Local PDF Upload**: Upload one or multiple PDF files, ask questions, and receive answers from the content.
3. **Wikipedia Article**: Enter a search query to retrieve a Wikipedia article, download it as a PDF, and ask questions about it.

## File Structure

- `app.py`: Main application script for the Streamlit interface.
- `wiki_utils.py`: Contains helper functions for searching and scraping Wikipedia pages.
- `pdf_utils.py`: Contains functions to save data to PDF and extract text from PDFs.
- `embeddings_utils.py`: Contains the function `create_embeddings_and_query` to generate embeddings for document content and answer user queries.

## Dependencies

Make sure to check `requirements.txt` for a full list of dependencies.

## Future Improvements

- Add support for more document formats (e.g., Word documents).
- Enhance question-answering capabilities by experimenting with different embeddings and model types.
- Add caching for previously queried content to improve performance.
