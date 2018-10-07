# -*- coding: utf-8 -*-
import csv
import os
import json

filepath = '/Users/willglas/Desktop/Brown/Sigma/SCInfoFile.csv'
filetowrite = '/Users/willglas/Desktop/Brown/Sigma/SCInfoFileJSON.txt'
fileForContacts = '/Users/willglas/Desktop/Brown/Sigma/SCInfoFileContacts.csv'
fileForNumsEmails = '/Users/willglas/Desktop/Brown/Sigma/numsEmailsList.txt'
fileForNames = '/Users/willglas/Desktop/Brown/Sigma/SCBrownNamesList.txt'

data = []
with open(filepath, 'r') as f:
    reader = csv.reader(f)
    headers = next(reader)
    
    for row in reader:
        d = dict(zip(headers, row))
        data.append(d)
nums = []
with open(fileForNumsEmails, 'r') as f:
    lines = f.read().splitlines()
    nums = lines
nums = ['' if nums[i] == 'None' else nums[i] for i in range(len(nums))]
numsA = ['4016443719@vzwpix.com', '8572720059@txt.att.net', '4017425692@vzwpix.com', '4082076284@tmomail.net', '4019241167@txt.att.net', '4015231774@txt.att.net', '6179092264@txt.att.net', '8054519603@vzwpix.com', '8175757035@txt.att.net', '5186186858@txt.att.net', '2032742537@txt.att.net', '4018625613@vzwpix.com', '9175872293@txt.att.net', '6107453636@vzwpix.com', '2143150385@tmomail.net', '4158878750@vzwpix.com', '6177561582@messaging.sprintpcs.com', '7813664736@txt.att.net', '5712256731@txt.att.net', '3108835905@vzwpix.com', '3107452234@txt.att.net', '2019379266@vzwpix.com', '4153424744@txt.att.net', '2035853078@vzwpix.com', '4065295825@vzwpix.com', '6318302503@txt.att.net', '2672262367@txt.att.net', '2039287636@txt.att.net', '5132557158@vzwpix.com', '6363525291@txt.att.net', '2132223706@vzwpix.com', '6176995704@vzwpix.com', '9172078570@txt.att.net', '4015437037@txt.att.net', '', '', '4123523915@txt.att.net', '8475251663@txt.att.net', '', '']

#os.system("oascript /Users/willglas/Desktop/Brown/Sigma/sendMessage.scpt ")
for i in range(len(data)):
    data[i]['emailablePhoneNum'] = nums[i]

namesEmail = []
with open(fileForNames, 'r') as f:
    namesEmail = f.read().splitlines()
        
classData = {namesEmail[i]:data[i] for i in range(len(namesEmail))}



with open(filetowrite, 'w+') as f:
    f.write(json.dumps(classData))
    
        
    
with open(fileForContacts, 'w+') as f:
    f.write('Name,E-mail 1 - Type')
    f.write("\n")
    for name in classData:
        f.write(classData[name]['Full Name']+ "," + classData[name]['emailablePhoneNum']+"\n")