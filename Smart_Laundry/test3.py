import requests
import json
data = {'is_wm_reserved': 'mmy789@naver.com'}    
r = requests.post('http://127.0.0.1:8000/WM/test/61/', data=data)        
# r = requests.post('http://127.0.0.1:8000/post/', data=data)   
    
print(r.text)
print(r.json())
print(r.content)