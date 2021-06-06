import requests
import json
data = {'is_wm_reserved': 'dbsrud9126@naver.com',
        'is_wm_door_open': False,
        'proximity_sensor': False,
        'lock': False,
        'servo_motor': True,
        'motor': 0
        }    
url = 'http://127.0.0.1:8000/WM/test/<int:pk>/'
r = requests.post(url, data=data)
# r = requests.post('http://127.0.0.1:8000/WM/test/61/', data=data)        
# r = requests.post('http://127.0.0.1:8000/post/', data=data)   
    
print(r.text)
print(r.json())
print(r.content)