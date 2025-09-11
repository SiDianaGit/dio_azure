
import os
# obter a chave da variável de ambiente
api_key = os.environ.get('GOOGLE_API_KEY')

if api_key is None:
    print("Erro: A variável de ambiente 'GOOGLE_API_KEY' não foi encontrada.")
else:
    # Use a chave para suas operações
    print("Chave de API obtida com sucesso!")

# Configuração para uso do LLM Google Gemini no chat bot
from google import genai

client = genai.Client()
modelo = "gemini-2.0-flash"
chat = client.chats.create(model=modelo)

from google.genai import types

chatConfig = types.GenerateContentConfig(
  system_instruction= "Você é um assistente pessoal e você sempre responde de forma sucinta."
)
chat = client.chats.create(model=modelo, config=chatConfig)

prompt = input("Esperando prompt: ")
while prompt != "fim":
  response = chat.send_message(prompt)
  print("Resposta: ", response.text)
  print("\n\n")
  prompt = input("Digite 'fim' para encerrar o chat. Esperando prompt: ")


