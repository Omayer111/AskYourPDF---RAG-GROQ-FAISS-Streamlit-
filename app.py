import streamlit as st
from utils import extract_text, chunk_text, create_index, search_index, ask_llm


# Add custom dark mode styling
st.markdown(
    """
    <style>
    body {
        background-color: #121212; /* Dark background */
        color: #ffffff; /* White text */
    }
    .stApp {
        background-color: #121212; /* Dark background for the app */
        color: #ffffff; /* White text */
    }
    h1, h2, h3, h4, h5, h6 {
        color: #4CAF50; /* Accent color for headings */
    }
    .stMarkdown p {
        color: #ffffff; /* White text for markdown content */
    }
    </style>
    """,
    unsafe_allow_html=True
)

if "chunks" not in st.session_state:
    st.session_state.chunks = []
if "index" not in st.session_state:
    st.session_state.index = None
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []


# Update the title with dark mode styling
st.markdown(
    """
    <h1 style="text-align: center; color: #4CAF50; font-size: 36px; font-weight: bold;">
        📄 Ask Your PDF
    </h1>
    """,
    unsafe_allow_html=True
)

# File uploader section
uploaded = st.file_uploader("Upload a PDF file", type="pdf")

if uploaded:
    with st.spinner("Processing your PDF..."):
        text = extract_text(uploaded)
        chunks = chunk_text(text, chunk_size=500, chunk_overlap=100)
        index, _ = create_index(chunks)

        st.session_state.chunks = chunks
        st.session_state.index = index
        st.success("PDF processed successfully!")

if st.session_state.index:
    query = st.text_input("Ask a question about the Doc:")
    if st.button("Ask") and query:
        with st.spinner("Thinking..."):
            top_chunks = search_index(query, st.session_state.chunks, st.session_state.index, top_k=5)
            context = "\n\n".join(top_chunks)
            answer = ask_llm(query, context)
            st.session_state.chat_history.append((query, answer))

# Display Q&A section with dark mode styling
for q, a in st.session_state.chat_history:
    st.markdown(
        f"""
        <div style="border: 2px solid #4CAF50; border-radius: 10px; padding: 16px; margin-bottom: 16px; background-color: #1E1E1E;">
            <p style="font-weight: bold; color: #4CAF50; margin-bottom: 8px;">Q: {q}</p>
            <p style="color: #ffffff;">A: {a}</p>
        </div>
        """,
        unsafe_allow_html=True
    )

# Footer with dark mode styling
st.markdown(
    """
    <div style="display: flex; justify-content: center; align-items: center; height: 50px; margin-top: 20px;">
        <p style="font-size: 14px; font-weight: bold; color: #4CAF50;">Developed by Abu Omayer</p>
    </div>
    """,
    unsafe_allow_html=True
)