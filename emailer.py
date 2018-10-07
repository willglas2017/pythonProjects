# -*- coding: utf-8 -*-

import smtplib
import json




def sendEmail(toAddr, msg=None, user=None, mailService=None, password=None):
    server = connectToServer();
    
    if not user:
        user = input("Input username: ")
    if not mailService:
        mailService = input("Mail Provider: ")
    if not password:
        password = input("Password: ")
    if not msg:
        msg = input("Message: ")
   
    server.login(user, password)
    
    
    fromAddr= user+'@'+ mailService
    
    
    
    server.sendmail(fromAddr, toAddr, msg)
    
    print("Done")
    
def connectToServer():
    server = smtplib.SMTP('smtp.gmail.com', 587)

    server.ehlo()
    server.starttls()
    server.ehlo()
    
    return server
    
def emailTextSigma(msg=None, user=None, mailService=None, password=None):
    if not user:
        user = input("Input username: ")
    if not mailService:
        mailService = input("Mail Provider: ")
    if not password:
        password = input("Password: ")
    if not msg:
        msg = input("Message: ")
        
    fileWithData = '/Users/willglas/Desktop/Brown/Sigma/SCInfoFileJSON.txt'
    
    conf = input("Are you sure you want to mass email the class?")
    
    if not conf:
        return
    
    with open(fileWithData, 'r+') as f:
        data = json.loads(f.read())
        for name in data:
            if data[name]['emailablePhoneNum'] != '':
                sendEmail(data[name]['emailablePhoneNum'], msg.format(name), user, mailService, password)
    
if __name__ == '__main__':
    message = "Hey, hope your summer is going well. You think you are going to make it to Montreal?                      \nAlso, is {}@brown.edu your brown email adress?"
    'sigchibetanu21', 'gmail.com', 'goodcharacter'
    
#    emailTextSigma(message, )
    