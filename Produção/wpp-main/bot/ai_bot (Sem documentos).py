import os
from decouple import config # Busca a variável de ambiente
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_groq import ChatGroq # Busca os modelos do groq

# Comunica com o groq
os.environ["GROQ_API_KEY"] = config("GROQ_API_KEY")

# Classe do bot
class AIBot():    
    # Inicializador
    def __init__(self):
        pass # Logica de negocio removida por seguranca corporativa

    def invoke(self, question):
        pass # Logica de negocio removida por seguranca corporativa
