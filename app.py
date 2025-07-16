import streamlit as st
from gpt_backend import ask_gpt
from retrieval import retrieve_docs

st.title("GenAI Q&A Assistant")

question = st.text_input("Ask a question:")

if st.button("Submit") and question:
    docs = retrieve_docs(question)
    context = "\n".join(docs)
    prompt = f"Context:\n{context}\n\nQuestion: {question}"
    answer = ask_gpt(prompt)
    st.write("Answer:", answer)
