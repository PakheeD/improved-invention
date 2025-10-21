def summarize_document(text, qa_chain):
    prompt = f"Summarize the following legal document in bullet points highlighting key obligations, liabilities, and termination clauses:\n{text}"
    summary = qa_chain.llm.invoke(prompt)
    return summary
