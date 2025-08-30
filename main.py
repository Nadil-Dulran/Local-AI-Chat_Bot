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

def handle_conversation():
    context = ""
    print("Welcome to the My AI Chat Bot!, Type 'exit' to quit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            print("Exiting the Chat. Goodbye!")
            break

        result = chain.invoke({"context": context, "question": user_input})
        print("AI BOT: ", result)
        context += f"\nUser: {user_input}\nAI BOT: {result}"
        
if __name__ == "__main__":
    handle_conversation()
