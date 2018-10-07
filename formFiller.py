# -*- coding: utf-8 -*-

import re
from robobrowser import RoboBrowser
url = "https://frontrush.com/Roster/login/login.aspx"

user = 'william_glaser@brown.edu'
passWd = 'yE_63=xA$B'
name = 'William Glaser'
school = 'Brown University'
bruID = '140155065'
date = '09/09/2018'

browser = RoboBrowser(parser="lxml")
browser.open(url)
loginForm = browser.get_form()
loginForm['ctl00$ContentPlaceHolderLogin$txtRosterUsername'] = user
loginForm['ctl00$ContentPlaceHolderLogin$txtRosterLoginPassword'] = passWd
browser.submit_form(loginForm)

conf =browser.get_form()

browser.submit_form(conf, submit=conf.submit_fields['ctl00$Main$btnConfirm'])

inbox = browser.find(id="ctl00_Main_AthleteInbox")
links = inbox.find_all('a')

#THEORETICALLY THIS WORKS BUT IT DOESNT OH WELL
#browser.follow_link(links[0])


url = 'https://incontrol.acsathletics.com/TeamManager/FormBuilder/RenderForm.aspx?org_id=115&form_id=174877&instance_id=3582919&athlete_id=7659753'
browser.open(url)
form = browser.get_form()
sub = None
for key in form.keys():
    if 'UINSig' in key:
        form[key] = bruID
    if 'Calendar' in key:
        form[key] = date
    if 'SubmitButton' in key:
        sub = key
