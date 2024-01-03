import streamlit as st
from dotenv import load_dotenv
from PyPDF2 import PdfReader
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings, HuggingFaceInstructEmbeddings
from langchain.vectorstores.faiss import FAISS


def GetPDFText(pdfDocs):
    text = ""

    for pdf in pdfDocs:
        pdfReader = PdfReader(pdf)

        for page in pdfReader.pages:
            text += page.extract_text()

    return text


def GetTextChunks(text):
    textSplitter = CharacterTextSplitter(
        separator = "\n",
        chunk_size = 1000,
        chunk_overlap = 200,
        length_function = len
    )
    chunks = textSplitter.split_text(text)
    return(chunks)


def GetVectorStore(textChunks):
    #embeddings = OpenAIEmbeddings()
    embeddings = HuggingFaceInstructEmbeddings(model_name="hkunlp/instructor-xl")
    vectorStore = FAISS.from_texts(texts=textChunks, embedding=embeddings)
    return vectorStore

def main():
    load_dotenv()
    st.set_page_config(page_title="Chat with multiple PDFs", page_icon=":books:")

    st.header("Chat with multiple PDFs :books:")
    st.text_input("Ask a question about your documents:")

    with st.sidebar:
        st.subheader("Your documents")
        pdfDocs = st.file_uploader(
            "Upload your PDFs here and click Process", accept_multiple_files=True)
        
        if st.button("Process"):
            with st.spinner("Processing"):
                # get PDF text
                rawText = GetPDFText(pdfDocs)

                # get the text chunks
                textChunks = GetTextChunks(rawText)

                # create vector store
                vectorStore = GetVectorStore(textChunks)


if __name__ == '__main__':
    main()