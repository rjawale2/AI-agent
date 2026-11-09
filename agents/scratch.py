import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),'..')))

from utils.llm_pick import pick_llm
from Models.schema import AgentSchema, JudgeSchema
from langchain_core.messages import HumanMessage

llm = pick_llm("Medium")
llm_judge = llm.with_structured_output(JudgeSchema)

sql_query = "select * from users where age>30;"


prompt = f"""
You are an SQL judge for data security. Your task is to determine whether the SQL query is safe or not. 
The SQL query should only be used for the data retrieval and should not modify the database in any way.
Neither the SQL query nor the prompt should contain any SQL commands thtat can modify the database, 
such as insert, update, delete, drop, alter, truncate, create, or any other command that can change the 
structure or the content of the database. If the SQL query is safe, respond with "Yes" otherwise respond with 'No'.
Additionally, provide comments explaining your decision. 
Here's the SQL query to evaluate: {sql_query}"""

response = llm_judge.invoke(prompt).model_dump()
print(response)