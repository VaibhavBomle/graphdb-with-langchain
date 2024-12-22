from dotenv import load_dotenv
from config import get_Neo4JGraph,get_chatGroq
from query_constant import movie_query
from langchain.chains import GraphCypherQAChain
import os

load_dotenv()

# Get initialize Neo4j
graph = get_Neo4JGraph()
print("graph==>",graph)
graph.query(movie_query)
graph.refresh_schema()

print("graph.schema====>",graph.schema)


# Get initialize get_chatGroq
llm = get_chatGroq()
print("llm==>",llm)

chain = GraphCypherQAChain.from_llm(graph=graph,llm=llm,verbose=True)
print("Chain ==>",chain)

response = chain.invoke({"query":"Who was the director of the movie Casino"})
print("response  ==>",response)



