#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 16 12:27:15 2018

@author: willglas
"""

token = 'xUFbvudqTna1Y9jyzhigjC2yPgbYpMLL71bcHJaT'
filepath = '/Users/willglas/Desktop/Brown/Sigma/groupmeData.txt'

from groupy import Client
import json

client = Client.from_token(token)

groups = list(client.groups.list_all())

group = None
for x in groups:
    if x.name == 'Beta Fucking Nu':
        group = x
    

#for member in group.members:
#    print(member.nickname)
users = {}
total = 0
for message in group.messages.list_all():
    if message.name in users:
        users[message.name]['messages_sent'] += 1
    else:
        users[message.name] = {'messages_sent': 1}
    total += 1
    
totalPercent = 0
for user in users:
    users[user]['%'] = users[user]['messages_sent']/total *100
    totalPercent += users[user]['%']

with open(filepath, 'w+') as outfile:  
    json.dump(users, outfile, indent=4)
    
