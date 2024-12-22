
from langchain_neo4j import Neo4jGraph
from dotenv import load_dotenv
import os
from langchain_groq import ChatGroq

load_dotenv()

NEO4J_URI = os.getenv("NEO4J_URI")
NEO4J_USERNAME = os.getenv("NEO4J_USERNAME")
NEO4J_PASSWORD = os.getenv("NEO4J_PASSWORD")

def get_Neo4JGraph():
    graph = Neo4jGraph(url=NEO4J_URI,username=NEO4J_USERNAME,password=NEO4J_PASSWORD)
    print("graph==>",graph)
    return graph

def get_chatGroq():
   groq_api_key = os.getenv("GROQ_API_KEY")
   llm = ChatGroq(groq_api_key=groq_api_key,model_name="Gemma2-9b-It")
   print("llm==> ",llm)
   return llm

