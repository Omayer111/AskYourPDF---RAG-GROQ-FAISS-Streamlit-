import faiss
import numpy as np
from PyPDF2 import PdfReader
from sentence_transformers import SentenceTransformer
from langchain.text_splitter import RecursiveCharacterTextSplitter
import openai


embedder  = SentenceTransformer("all-MiniLM-L6-v2")


def extract_text(pdf_file):
    reader = PdfReader(pdf_file)
    text = ""
    for page in reader.pages:
        text += page.extract_text() or ""

    return text

def chunk_text(text, chunk_size=500, chunk_overlap=100):
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap
    )
    chunks = text_splitter.split_text(text)
    return chunks

def create_index(chunks):
    embeddings = embedder.encode(chunks)
    index = faiss.IndexFlatL2(len(embeddings[0]))
    index.add(np.array(embeddings))
    return index, embeddings

def search_index(query, chunks, index, top_k=5):
    query_vec = embedder.encode([query])
    distances, indices = index.search(np.array(query_vec), top_k)
    return [chunks[i] for i in indices[0]]

def ask_llm(question, context):
    prompt = f"Answer the question based on the context provided.\n\nContext: {context}\n\nQuestion: {question}\n\nAnswer:"
    
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.3,
        max_tokens=300
    )
    return response.choices[0].message.content