from modules.memory import add_memory,get_memory
# from openai import OpenAI
# from dotenv import load_dotenv
# import os
# load_dotenv() 
# client=OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
# def ask_ai(question):
#     response=client.responses.create(
#         model="gpt-5",
#         input=question
#     )
#     return response.output_text


import ollama
def ask_ai(question):
    add_memory("user",question)
    response=ollama.chat(
        model="llama3.2:3b",
        messages=get_memory()
    )
    answer=response["message"]["content"]
    add_memory("assistant",answer)
    return answer

