from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

template = """"
Answer the question below. 
  
Here is the coversation history: {context}

Question: {question}

Answer:

"""

model = OllamaLLM(model= "llama3.2")
prompt = ChatPromptTemplate.from_template(template)
chain = prompt | model

result = chain.invoke({"context": "", "question": "Hay how are you?"})
print(result)