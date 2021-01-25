#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 20 18:44:34 2021

@author: julien
"""
import requests
import pprint
import json

# Un petit ensemble de données qu'un serveur envoie au navigateur web de l'utilisateu ( données personnelr ).
#-----------------------------------------------------------------------------------------------------------

cookies = {
    'acceptCookieFun': 'on',
    'atuserid': '%7B%22name%22%3A%22atuserid%22%2C%22val%22%3A%22bbcb4d05-c614-429e-9705-91e1f22536a6%22%2C%22options%22%3A%7B%22end%22%3A%222022-02-15T13%3A46%3A56.552Z%22%2C%22path%22%3A%22%2F%22%7D%7D',
    'atidvisitor': '%7B%22name%22%3A%22atidvisitor%22%2C%22val%22%3A%7B%22vrn%22%3A%22-602676-%22%7D%2C%22options%22%3A%7B%22path%22%3A%22%2F%22%2C%22session%22%3A15724800%2C%22end%22%3A15724800%7D%7D',
    'csrftoken': 'XHkQOfBjn7BbBspgKk3SfXB8Wk12TjU8',
    'edxloggedin': 'true',
    'edx_session': 'wpymygbxaixb4t7oq9qeq7e9dsmb9kvc',
    'edx-user-info': '{\\"username\\": \\"Dindon53\\"\\054 \\"version\\": 1\\054 \\"email\\": \\"lienmontage@hotmail.com\\"\\054 \\"header_urls\\": {\\"learner_profile\\": \\"https://www.fun-mooc.fr/u/Dindon53\\"\\054 \\"logout\\": \\"https://www.fun-mooc.fr/logout\\"\\054 \\"account_settings\\": \\"https://www.fun-mooc.fr/account/settings\\"}}',
}

# Permet au client et au  serveur de transmettre des informations supplémentaires de requète ( indispensable )
#-----------------------------------------------------------------------------------------------------
headers = {
    'Connection': 'keep-alive',
    'sec-ch-ua': '"Google Chrome";v="87", " Not;A Brand";v="99", "Chromium";v="87"',
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'X-CSRFToken': 'XHkQOfBjn7BbBspgKk3SfXB8Wk12TjU8',
    'X-Requested-With': 'XMLHttpRequest',
    'sec-ch-ua-mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Dest': 'empty',
    'Referer': 'https://www.fun-mooc.fr/courses/course-v1:ulb+44013+session04/discussion/forum/ce953728a12d1ebe20c60239f1900d3e89dce41d/threads/60085107e47b4a0001000799',
    'Accept-Language': 'fr-FR,fr;q=0.9,en-US;q=0.8,en;q=0.7',
    'dnt': '1',
}
# Paramètre pas indispensable mais utile
#-----------------------------------------------------------------------------------------------------

params = (
    ('ajax', '1'),
    ('page', '1'),
    ('sort_key', 'date'),
    ('sort_order', 'desc'),
)

url ="https://www.fun-mooc.fr/courses/course-v1:ulb+44013+session04/discussion/forum"

response = requests.get(url, headers=headers, params=params, cookies=cookies)

block = response.json()
print(block)
