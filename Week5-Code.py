import requests as rq
from datetime import datetime

BASE_URL = 'https://webdevv2.pythonanywhere.com/'


payload = {'input': 'THIS IS A NEW INPUT'}

resposne = rq.get(BASE_URL, params = payload)

json_values = resposne.json()

rq_input = json_values['input']
time_stamp = json_values['timestamp']
character_count = json_values['character_count']

print(f'input is: {rq_input}')
print(f'Date is: {datetime.fromtimestamp(time_stamp)}')
print(f'input is: {character_count}')
