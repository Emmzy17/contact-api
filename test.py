
from unicodedata import name
import requests

BASE = 'http://127.0.0.1:5000/'
response = requests.post(BASE , {'name': 'Emjay', 'phone_no':8164828761, 'email':'emanueladjerry@gmail.com'})
print(response)
#response = requests.delete(BASE + 'video/0')
#print(response)
#input()
#response = requests.patch(BASE + 'contact/emmy', {'name': name, 'phone_no': 8164828761})
#print(response.json())
