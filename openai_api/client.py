from openai import OpenAI
import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())
api_key = os.getenv("OPENAI_API_KEY")

def get_car_ai_bio(model, brand, year):
    prompt = f'''
        Me mostre uma descrição de venda para o carro {brand} {model} {year} em apenas 250 caracteres. Fale coisas específicas desse modelo de carro.
    '''
    
    client = OpenAI(api_key=api_key) 
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user",
              "content": prompt}
        ],
        max_tokens=1000,
        temperature=0.7
    )

    return response.choices[0].message.content