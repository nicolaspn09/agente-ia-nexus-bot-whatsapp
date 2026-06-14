import os
from decouple import config # Busca a variável de ambiente
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_groq import ChatGroq # Busca os modelos do groq
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_chroma import Chroma
from langchain_core.messages import HumanMessage, AIMessage
from langchain_huggingface import HuggingFaceEmbeddings

# Comunica com o groq
os.environ["GROQ_API_KEY"] = config("GROQ_API_KEY")

# Classe do bot
class AIBot():    
    # Inicializador
    def __init__(self):
        pass # Logica de negocio removida por seguranca corporativa

    def __build_retriever(self):
        pass # Logica de negocio removida por seguranca corporativa


    def __build_messages(self, history_messages, question):
        pass # Logica de negocio removida por seguranca corporativa

    def invoke(self, history_messages, question):
        pass # Logica de negocio removida por seguranca corporativa
