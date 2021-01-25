#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 18 15:12:36 2021
@author: Garcia Julien
"""
# Import librairies
import conf
from pymongo import MongoClient
import requests
import json

# Connection bdd

#client = MongoClient("mongodb://%s:%s@%s/?authSource=%s"
#% (conf.user, conf.mdp,"127.0.0.1", "admin"))

# Elements pour url 
cookies = {
    'acceptCookieFun': 'on',
    'atuserid': '%7B%22name%22%3A%22atuserid%22%2C%22val%22%3A%22bbcb4d05-c614-429e-9705-91e1f22536a6%22%2C%22options%22%3A%7B%22end%22%3A%222022-02-15T13%3A46%3A56.552Z%22%2C%22path%22%3A%22%2F%22%7D%7D',
    'atidvisitor': '%7B%22name%22%3A%22atidvisitor%22%2C%22val%22%3A%7B%22vrn%22%3A%22-602676-%22%7D%2C%22options%22%3A%7B%22path%22%3A%22%2F%22%2C%22session%22%3A15724800%2C%22end%22%3A15724800%7D%7D',
    'csrftoken': 'IE5WWjLqcnmHqHb4kWJp2aL30dTV5sOv',
    'edxloggedin': 'true',
    'edx_session': 'jo4gaw6tgbr6fimy2odil6r5o5wi7vk7',
    'edx-user-info': '{\\"username\\": \\"Dindon53\\"\\054 \\"version\\": 1\\054 \\"email\\": \\"lienmontage@hotmail.com\\"\\054 \\"header_urls\\": {\\"learner_profile\\": \\"https://www.fun-mooc.fr/u/Dindon53\\"\\054 \\"logout\\": \\"https://www.fun-mooc.fr/logout\\"\\054 \\"account_settings\\": \\"https://www.fun-mooc.fr/account/settings\\"}}',
}

headers = {
    'Connection': 'keep-alive',
    'sec-ch-ua': '"Google Chrome";v="87", " Not;A Brand";v="99", "Chromium";v="87"',
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'X-CSRFToken': 'IE5WWjLqcnmHqHb4kWJp2aL30dTV5sOv',
    'X-Requested-With': 'XMLHttpRequest',
    'sec-ch-ua-mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Dest': 'empty',
    'Referer': 'https://www.fun-mooc.fr/courses/course-v1:ulb+44013+session04/discussion/forum',
    'Accept-Language': 'fr-FR,fr;q=0.9,en-US;q=0.8,en;q=0.7',
    'dnt': '1',
}


# Pour la reconstruction du lien
domaine_Fun_Mooc = "https://www.fun-mooc.fr/courses/course-v1:ulb+44013+session04/discussion/forum/"
theads = "threads"

# Récupération: Nombre de pages ( Requête1)
response = requests.get(domaine_Fun_Mooc, headers=headers, cookies=cookies)
data_Json = response.json()
number_pages = data_Json['num_pages']

fichier = open("data_2.json",'x')
n = 1
compt = 0
for page in range(1,10+n):
    params = (
        ('page', page),
        ('sort_key', 'date'),
        ('sort_order', 'desc'),
    )
   
    print("o---)=======>","Page numéro:",page,"<=======(---o")
    response = requests.get(domaine_Fun_Mooc, headers=headers, params=params, cookies=cookies)
    data_Json = response.json()
    for block in data_Json['discussion_data']:
        params2 = (
            ('sort_key', 'date'),
            ('sort_order', 'desc'),
        )
        
        url2 = domaine_Fun_Mooc + block['commentable_id']+'/'+ theads +'/'+ block['id']
        response2 = requests.get(url2, headers=headers,params=params2, cookies=cookies)
        data_comment = response2.json()
        compt = compt + 1

        #Insertion de données------------------#Information bdd---------------
        
        #bdd = client['Datalab2020']
        #collec = bdd['groupe2']
        

        json.dump(data_comment, fichier)
        
        #collec.insert_one(data_comment)
        print(compt)
        
print("Ready")
#------

#client.close()

