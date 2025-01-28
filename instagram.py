import requests
from dotenv import load_dotenv
import os

load_dotenv('.env')

key = os.getenv("NOVINHUB_API_KEY")

def send_message(conversation_id, message):

  url = f"https://api.novinhub.com/token/v2/conversation/{conversation_id}/reply"

  payload = {'content': message}
  files=[
  ]
  headers = {
  'Authorization': f'Bearer {os.getenv("NOVINHUB_API_KEY")}'
  }

  response = requests.request("POST", url, headers=headers, data=payload, files=files)

  print(response.text)
  return response.text
