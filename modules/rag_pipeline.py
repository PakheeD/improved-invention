from langchain.chains import RetrievalQA
from langchain_google_genai import ChatGoogleGenerativeAI

def get_qa_chain(vector_store):
    llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash", temperature=0.3)
    retriever = vector_store.as_retriever(search_kwargs={"k": 3})
    qa_chain = RetrievalQA.from_chain_type(llm=llm, retriever=retriever)
    return qa_chain
