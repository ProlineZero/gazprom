import json
import requests
import os

# Run server 
# os.system("python manage.py runserver")

urlAdd = "http://127.0.0.1:8000/api/add_article"
filename = "ruwikiquote-20230213-cirrussearch-general.json"

def _value_if_key_exists(key, dict):
    if key in dict:
        return dict[key]
    else:
        return None

#Due to the incorrectness of the json dump file and the resulting inability to read the json.load() file,
# reading is organized in this way. 
with open(filename, "r", encoding="utf-8") as datafile:
    data = []
    #Skip each second string
    while(datafile.readline()):
        #read required string
        str = datafile.readline()
        raw_data = json.loads(str)

        title = _value_if_key_exists("title", raw_data ) 
        category = _value_if_key_exists("category", raw_data ) 
        wiki = _value_if_key_exists("wiki", raw_data ) 
        language = _value_if_key_exists("language", raw_data ) 
        auxiliary_text = _value_if_key_exists("auxiliary_text", raw_data ) 
        create_timestamp = _value_if_key_exists("create_timestamp", raw_data ) 
        timestamp = _value_if_key_exists("timestamp", raw_data ) 

        article = {
            'title': title,
            'category': category,
            'wiki': wiki,
            'language': language,
            'auxiliary_text': auxiliary_text if auxiliary_text else [],
            'create_timestamp': create_timestamp,
            'timestamp': timestamp
        }
        data.append(article)
        
        if len(data) == 200:
            requests.post(urlAdd, json=data)
            data.clear()
    requests.post(urlAdd, json=data)




