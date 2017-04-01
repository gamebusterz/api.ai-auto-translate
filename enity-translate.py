
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests
# import json
API_KEY = "YOUR-GOOGLE-TRANSLATE-API-KEY-HERE"

#
# r=requests.post(url='https://translation.googleapis.com/language/translate/v2?parameters',params=PARAMETERS)
# data=r.json()
# print(data)

import json
import os
from pprint import pprint
output = {}

def translate_req(string_list):
    PARAMETERS= {'key': API_KEY, 'source':'en','target':'fr','q':string_list}
    r=requests.post(url='https://translation.googleapis.com/language/translate/v2?parameters',params=PARAMETERS)
    translate_response=r.json()

    translated_list=[]
    for i in translate_response['data']['translations']:
        translated_list.append(i['translatedText'])
    output['entries'].append({'value':translated_list[0],'synonyms':translated_list})

def translate_json(data):
    output['name']=data['name']
    output['isOverridable']=data['isOverridable']
    output['entries'] = []

    for i in data['entries']:
        translate_req(i['synonyms'])

    output['isEnum'] = data['isEnum']
    output['automatedExpansion'] = data['automatedExpansion']
    json_data = json.dumps(output, indent=2)
    # print(json_data)
    return json_data

# with open('/home/yankee/crowdFunding/app/entity/Payment-NotAllowed.json') as data_file:
#     data = json.load(data_file)
#     translated_json = translate_json(data)
path = '/home/yankee/crowdFunding/app/entity/'
os.system('mkdir -p /home/yankee/FrenchBot/entity/')

for jsonfile in os.listdir(path):
    jsonfile = path+jsonfile
    with open(jsonfile) as data_file:
        data = json.load(data_file)
        translated_json = translate_json(data)
        print(translated_json)
    with open('/home/yankee/FrenchBot/entity/'+output['name']+'.json','w+') as outfile:
        outfile.write(translated_json)



# input_list = data['entries'][0]['synonyms']
#
# PARAMETERS= {'key': API_KEY, 'source':'en','target':'fr','q':input_list}
# r=requests.post(url='https://translation.googleapis.com/language/translate/v2?parameters',params=PARAMETERS)
# data=r.json()
# print(data)



# translate_req(['Hello World','One two three'])
