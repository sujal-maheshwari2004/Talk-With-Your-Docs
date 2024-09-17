# Chat with Docs

**Chat with Docs** is a Streamlit-based application that allows users to upload PDF files or generate PDFs from Wikipedia articles and then query these documents using natural language. The application leverages natural language processing (NLP) capabilities, enabling users to ask questions about the content of the PDFs and receive human-like responses.

## Features

- **PDF Upload**: Users can upload one or more PDF files from their local system.
- **Wikipedia PDF Generation**: Users can search for Wikipedia articles, scrape the content, and generate a PDF from the article.
- **PDF Text Processing**: The application extracts text from uploaded or generated PDFs.
- **Chunked Text Splitting**: Text is split into smaller chunks to improve the accuracy of queries.
- **Vector Search with FAISS**: Text chunks are embedded using OpenAI embeddings, and FAISS is used to create a vector store for efficient similarity searches.
- **Natural Language Querying**: Users can ask questions about the content of the PDFs, and the application uses an OpenAI language model to generate responses.

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/sujal-maheshwari2004/chat-with-docs.git
   cd chat-with-docs
   ```

2. **Install required dependencies:**

   You can install the required Python packages using pip:

   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables:**

   Create a `.env` file in the root directory and add your OpenAI API key:

   ```env
   OPENAI_API_KEY=your_openai_api_key
   ```

4. **Run the application:**

   Start the Streamlit application with the following command:

   ```bash
   streamlit run app.py
   ```

## Usage

### 1. **Upload PDF Files**

   - Select "Local File" from the dropdown.
   - Upload one or more PDF files using the file uploader.
   - Once uploaded, you can enter a query in the text input box and ask questions about the content.

### 2. **Generate PDF from Wikipedia**

   - Select "Wikipedia" from the dropdown.
   - Enter a Wikipedia search query in the input box.
   - The application will find the most relevant Wikipedia page, scrape the content, and generate a PDF.
   - After generating the PDF, you can download it and ask questions about the content.

### 3. **Querying the Document**

   - For both local PDFs and Wikipedia-generated PDFs, you can enter queries in the text box.
   - The application will process your query and provide a response based on the content of the document.

## Project Structure

- **app.py**: Main application file containing the Streamlit app logic.
- **requirements.txt**: List of Python packages required to run the application.
- **.env**: Environment file to store your API keys securely.

## Dependencies

The application relies on the following Python libraries:

- **Streamlit**: Web framework for creating interactive applications.
- **Wikipedia**: API wrapper for retrieving Wikipedia articles.
- **Requests**: Library for making HTTP requests.
- **BeautifulSoup4**: HTML and XML parser used for web scraping.
- **FPDF**: Library for generating PDF files.
- **PyPDF2**: Library for reading and manipulating PDF files.
- **LangChain**: NLP framework for working with language models and embeddings.
- **FAISS**: Vector search library for efficient similarity search.
- **OpenAI**: For using GPT-based models to process natural language queries.

## Troubleshooting

- **Error processing PDF**: Ensure the PDF files are not encrypted or corrupted.
- **Wikipedia page not found**: Try refining your search query if the page cannot be found or if disambiguation occurs.
- **Environment variable issues**: Ensure your OpenAI API key is correctly set in the `.env` file.

## License

This project is licensed under the MIT License.

## Acknowledgments

- Thanks to the developers of the libraries and tools that made this project possible, including Streamlit, OpenAI, and FAISS.
