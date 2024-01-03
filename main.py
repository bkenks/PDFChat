import streamlit as st
from dotenv import load_dotenv
from PyPDF2 import PdfReader
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings, HuggingFaceInstructEmbeddings
from langchain.vectorstores.faiss import FAISS
from langchain.chat_models import ChatOpenAI
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain
from htmlTemplates import css, bot_template, user_template


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
    embeddings = OpenAIEmbeddings()
    #embeddings = HuggingFaceInstructEmbeddings(model_name="hkunlp/instructor-xl")
    vectorStore = FAISS.from_texts(texts=textChunks, embedding=embeddings)
    return vectorStore


def GetConversationChain(vectorStore):
    llm = ChatOpenAI()
    memory = ConversationBufferMemory(memory_key="chatHistory", return_messages=True)
    conversationChain = ConversationalRetrievalChain.from_llm(
        llm=llm,
        retriever=vectorStore.as_retriever(),
        memory=memory
    )
    return conversationChain


def HandleUserInput(userQuestion):
    response = st.session_state.conversation({"question":userQuestion})
    st.write(response)


def main():
    load_dotenv()
    st.set_page_config(page_title="Chat with multiple PDFs", page_icon=":books:")

    st.write(css, unsafe_allow_html=True)

    if "conversation" not in st.session_state:
        st.session_state.conversation = None

    st.header("Chat with multiple PDFs :books:")
    userQuestion = st.text_input("Ask a question about your documents:")
    if userQuestion:
        HandleUserInput(userQuestion)

    st.write(user_template.replace("{{MSG}}", "Hello Bot"), unsafe_allow_html=True)
    st.write(bot_template.replace("{{MSG}}", "Hello Human"), unsafe_allow_html=True)

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

                # create conversation chain
                st.session_state.conversation = GetConversationChain(vectorStore)


if __name__ == '__main__':
    main()