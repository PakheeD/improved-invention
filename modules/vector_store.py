from langchain_community.vectorstores import FAISS

def build_vector_store(chunks, embeddings):
    vector_store = FAISS.from_texts(chunks, embedding=embeddings)
    vector_store.save_local("data/vectorstore/legal_vectors")
    return vector_store
