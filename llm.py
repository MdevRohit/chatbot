from openai import OpenAI
from src.prompt import system_instruction
client = "OpenAI()"
client = OpenAI(api_key="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")

messages = [ 
           {"role":"system","content":system_instruction}
    ]

def ask_order(messages , model="gpt-3.5-turbo", temperature = 0): 
    
    response = client.chat.completions.create(
        model = model,
        messages = messages,
        temperature = temperature,
        
    )
    return response.choices[0].message.content