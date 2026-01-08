print('Radhe Radhe')

# Question and Answer Application

from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv
from langchain_community.vectorstores import Chroma
from langchain.chains import RetrievalQA
import streamlit as st

load_dotenv()
llm=ChatGoogleGenerativeAI(model='gemini-2.5-flash-lite')
embedding_model=GoogleGenerativeAIEmbeddings(model='models/embedding-001')


loader=PyPDFLoader('machinelearningpdf.pdf')
docs=loader.load()

splitter=RecursiveCharacterTextSplitter(chunk_size=1000,chunk_overlap=100)
chunks=splitter.split_documents(docs)
# print(chunks)

vectorstore=Chroma.from_documents(chunks,embedding_model)
retriever=vectorstore.as_retriever(search_kwargs={"k":15})
qa=RetrievalQA.from_chain_type(
    llm=llm,
    retriever=retriever,
    return_source_documents=True)

# query="  what is Reinforcement Learning and Evaluating Hypotheses "
# result=qa.invoke({'query':query})
# print("\n Answer:-",result['result'])
# print('\n sources:')
# for doc in result['source_documents']:
#     print(doc.page_content)



st.title("RAG-based Question Answering System")
st.write("Ask any question related to the uploaded PDF.")

# User input
query = st.text_input("Enter your question here:")

if st.button("Get Answer"):
    if query.strip() != "":
        result = qa.invoke({'query': query})
        st.subheader("Answer:")
        st.write(result['result'])

        st.subheader("Source Documents:")
        for i, doc in enumerate(result['source_documents'], 1):
            st.markdown(f"**Source {i}:**")
            st.write(doc.page_content)
    else:
        st.warning("Please enter a question!")