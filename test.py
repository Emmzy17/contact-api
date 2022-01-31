import requests

BASE = 'http://127.0.0.1:5000/'
#response = requests.patch(BASE + 'name/Emj', {'name' : 'lizza', 'phone_no':90568829, 'email':'bliz23@yahoo.com'})
#print(response.json())
#response = requests.get(BASE + 'name/Emj')
#print(response.json())
response = requests.delete(BASE + 'name/Emj')
print(response)