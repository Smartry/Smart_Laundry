import requests
import json
data = {'code': 'dbsrud1234'}    
r = requests.post('http://127.0.0.1:8000/', data=data)        
# r = requests.post('http://127.0.0.1:8000/post/', data=data)   
    
print(r.text)
print(r.json())
print(r.content)