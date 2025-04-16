# 📄 Ask Your PDF

**Ask Your PDF** is a Streamlit-based application that allows users to upload PDF documents and ask questions about their content. The app uses **FAISS** for efficient document retrieval and **Groq's API** (powered by Llama models) for generating accurate answers. It features a sleek dark mode interface for a professional and user-friendly experience.

---

## 🚀 Features

- Upload PDF documents and process their content.
- Retrieve relevant document sections using **FAISS**.
- Generate answers to user queries with **Groq's API** and Llama models.
- Aesthetic dark mode interface for better usability.

---

## 🛠️ Technologies Used

- **Python**: Core programming language.
- **Streamlit**: For building the web interface.
- **FAISS**: For vector similarity search.
- **Sentence Transformers**: For text embeddings.
- **Groq API**: For Llama-based language model integration.
- **PyPDF2**: For extracting text from PDFs.
- **LangChain**: For text chunking and splitting.

---

## 📂 Project Structure

```
doc-qna-RAG/
├── app.py               # Main Streamlit app
├── utils.py             # Utility functions for text processing, FAISS, and LLM integration
├── .env                 # Environment variables (API keys)
├── requirements.txt     # Python dependencies
└── README.md            # Project documentation
```

---

## ⚙️ Setup Instructions

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/Omayer111/AskYourPDF---RAG-GROQ-FAISS-Streamlit-.git
   cd AskYourPDF---RAG-GROQ-FAISS-Streamlit-
   ```

2. **Install Dependencies**:
   Ensure Python 3.8 or higher is installed, then run:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set Up Environment Variables**:
   Create a `.env` file in the root directory and add your **Groq API key**:
   ```properties
   GROQ_API_KEY=gsk_your_api_key_here
   ```

4. **Run the Application**:
   Start the Streamlit app:
   ```bash
   streamlit run app.py
   ```

5. **Upload a PDF and Ask Questions**:
   - Upload a PDF file using the file uploader.
   - Type your question in the input box and get answers based on the document content.

---

## 📚 How It Works

1. **PDF Processing**:
   - Extracts text from the uploaded PDF using `PyPDF2`.
   - Splits the text into chunks using `RecursiveCharacterTextSplitter`.

2. **Indexing and Retrieval**:
   - Generates embeddings for the text chunks using `SentenceTransformer`.
   - Indexes the embeddings using **FAISS** for fast similarity search.
   - Retrieves the most relevant chunks based on the user's query.

3. **Question Answering**:
   - Sends the query and retrieved context to **Groq's API** (Llama model).
   - Returns the generated answer to the user.

---

## 🖥️ Screenshots


### Q&A Section
*(Add a screenshot of the Q&A section here)*


https://github.com/user-attachments/assets/9f7900a0-27e1-4ca8-a6b0-19cd4b681367




[BANGLADESH INVESTMENT SUMMIT 2025.pdf](https://file.mofa.gov.bd/media/6f16aa9a-6de9-46b7-b923-43a6c4b935a5/BANGLADESH%20INVESTMENT%20SUMMIT%202025.pdf)



---

## 🛡️ License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## ✨ Developed By

**Abu Omayer**
