# -*- coding: utf-8 -*-
"""
Created on Thu Dec 19 14:43:09 2024

@author: ASUS
"""
def pdf_parser(file_name,question,password):
    from langchain.chains import ConversationalRetrievalChain
    from langchain.memory import ConversationBufferMemory
    from langchain_community.vectorstores import FAISS
    from langchain_openai import ChatOpenAI
    from langchain_openai.embeddings import OpenAIEmbeddings
    from langchain_text_splitters import RecursiveCharacterTextSplitter
    from langchain_community.document_loaders import PyPDFLoader
    loader = PyPDFLoader(file_name)
    documents = loader.load()
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=40,
        separators=["\n\n", "\n", "。", "！", "？", "，", "、", ""]
    )
    texts = text_splitter.split_documents(documents)
    embeddings = OpenAIEmbeddings(model="text-embedding-3-large",
                                        openai_api_key=password)
    vectorstore = FAISS.from_documents(texts, embeddings)
    retriever=vectorstore.as_retriever()
    model = ChatOpenAI(model="gpt-3.5-turbo",openai_api_key=password)
    memory = ConversationBufferMemory(return_messages=True, memory_key='chat_history', output_key='answer')

    qa = ConversationalRetrievalChain.from_llm(
        llm=model,
        retriever=retriever,
        memory=memory,
        chain_type="map_reduce"
        
    )
    
    return qa.invoke({'question':question,"chat_history": memory})['answer']
