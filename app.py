import streamlit as st
from dotenv import load_dotenv
from modules.pdf_loader import extract_text_from_pdf
from modules.text_processor import chunk_and_embed_text
from modules.vector_store import build_vector_store
from modules.rag_pipeline import get_qa_chain
from modules.summarizer import summarize_document

load_dotenv()

st.title("AI Legal Document Reviewer powered by LangChain + Gemini")
uploaded_file = st.file_uploader("Upload a legal PDF", type=["pdf"])

if uploaded_file:
    with st.spinner("Processing document..."):
        text = extract_text_from_pdf(uploaded_file)
        st.text_area("Extracted Text", text[:1500] + "...")
        
        chunks, embeddings = chunk_and_embed_text(text)
        vector_store = build_vector_store(chunks, embeddings)
        qa_chain = get_qa_chain(vector_store)

        st.success("Document ready for query!")

        question = st.text_input("Ask a question about the document:")
        if question:
            answer = qa_chain.run(question)
            st.write("Answer:", answer)

        if st.button("Generate Summary"):
            summary = summarize_document(text, qa_chain)
            st.markdown("### Summary")
            st.write(summary)
