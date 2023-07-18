import pandas as pd
import requests
import os
from api_key import api_key
import shutil


#api_key = "38319608-1012b573181c9697ce46a7d42"
flower = 'calendula'
base_url = f"https://pixabay.com/api/?key={api_key}&q={flower}+flowers&image_type=photo&pretty=true"
#https://pixabay.com/api/?key=38319608-1012b573181c9697ce46a7d42&q=yellow+flowers&image_type=photo&pretty=true
params = {
    'per_page': 50
}
result = requests.get(base_url,params = params)
json_data = result.json()

for image in json_data['hits']:
    name = image['id']
    image_url = image['largeImageURL']
    r = requests.get(image_url,stream = True)
    with open(str(name) + '.jpg' ,'wb') as f:
        f.write(r.content)
