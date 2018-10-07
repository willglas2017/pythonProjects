# -*- coding: utf-8 -*-
import csv
import simplejson as json

#%%
# Get necessary files
filepath = '/Users/willglas/Desktop/Brown/Sigma/SCInfoFile.csv'
filetowrite = '/Users/willglas/Desktop/Brown/Sigma/SCInfoFileJSON.txt'
filetowritepretty = '/Users/willglas/Desktop/Brown/Sigma/SCInfoFileJSONPretty.txt'
fileForContacts = '/Users/willglas/Desktop/Brown/Sigma/SCInfoFileContacts.csv'
fileForNumsEmails = '/Users/willglas/Desktop/Brown/Sigma/numsEmailsList.txt'
fileForNames = '/Users/willglas/Desktop/Brown/Sigma/SCBrownNamesList.txt'

#%%
# Gets 'Full Name', 'Phone Number', 'Home Town'
data = []
with open(filepath, 'r') as f:
    reader = csv.reader(f)
    headers = next(reader)
    
    for row in reader:
        d = dict(zip(headers, row))
        data.append(d)
#%%
# Gets names keys
namesEmail = []
with open(fileForNames, 'r') as f:
    namesEmail = f.read().splitlines()
#%%
# Adds names keys to data
classData = {namesEmail[i]:data[i] for i in range(len(namesEmail))}
#%%
# Finds emailable phone num
nums = {}
with open(fileForNumsEmails, 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        nums[row[0]] = row[1]
#%%
# Adds emailable phone num to data
for name in classData:
    classData[name]['emailablePhoneNum'] = nums[name]

#%%
# Writes data to file pretty
with open(filetowritepretty, 'w+') as outfile:  
    json.dump(classData, outfile, indent=4 * ' ')
    
#%%
# Writes data to file as dict
with open(filetowrite, 'w+') as outfile:  
    json.dump(classData, outfile)    
             
#%% 
# Writes data in google contacts format to file 
with open(fileForContacts, 'w+') as f:
    f.write('Name,E-mail 1 - Type')
    f.write("\n")
    for name in classData:
        f.write(classData[name]['Full Name']+ "," + classData[name]['emailablePhoneNum']+"\n")
#%%
        
# Converts it to 1s and 0s
binary = ' '.join(format(ord(i),'b').zfill(8) for i in json.dumps(classData))
#print("\n"+binary)