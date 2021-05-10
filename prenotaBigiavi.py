import requests
import random
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import imaplib
import email
from email.header import decode_header
import webbrowser
import os
import time
from datetime import date
import datetime

username =""
password =""
today = date.today()
nextDay = today + datetime.timedelta( 2 )
anno = str(nextDay)[:4]
mese = str(nextDay)[5:7]
giorno = str(nextDay)[8:10]
giornoSettimana = datetime.date(int(anno), int(mese), int(giorno)).weekday()

payloadZonaGialla = {
	"email":username,
	"date":str(nextDay),
	"start_time":"08:00",
	"end_time":"18:45",
	"note":None,
	"user_firstname":None,
	"user_lastname":None,
	"user_phone":None,
	"person_count":1}
user_agent_list = [
'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:77.0) Gecko/20100101 Firefox/77.0',
'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36',
'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:77.0) Gecko/20100101 Firefox/77.0',
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36']
url = 'https://httpbin.org/headers'
user_agent = random.choice(user_agent_list)
headers = {'User-Agent': user_agent}
link="https://reservation.affluences.com/api/reserve/50157" #per bigiavi
r1 = requests.post(link, json=payloadZonaGialla, headers=headers, timeout=5)

time.sleep(5)
######################
###MAIL###########
######################
imap = imaplib.IMAP4_SSL("outlook.office365.com")
imap.login(username, password)
status, messages = imap.select("INBOX")
messaggi_1 = int(messages[0])
res, msg = imap.fetch(str(messaggi_1), "(RFC822)")
for response in msg:
        if isinstance(response, tuple):
            msg = email.message_from_bytes(response[1])
            if msg.is_multipart():
                for part in msg.walk():
                    try:
                        body_1 = part.get_payload(decode=True).decode()
                    except:
                        pass

imap.close()
imap.logout()
#####################
##confermo###
####################
soup=(BeautifulSoup(body_1, 'html.parser'))
soup.encode('utf-8')
url=""
for link in soup.findAll('a'):
        url=str(link)[len("<a href=\""):len("<a href=\"https://affluences.com/reservation/confirm?reservationToken=941f3dfb-c945-57da-9eed-cfcad868c02e")]
        break
t=url[len("https://affluences.com/reservation/confirm?reservationToken="):]
l="https://reservation.affluences.com/api/reservations/"+t+"/confirmation"	
headers = {
"authority": "reservation.affluences.com",
"method": "POST",
"path": "/api/reservations/"+t+"/confirmation",
"scheme": "https",
"accept": "application/json, text/plain, */*",
"accept-encoding": "gzip, deflate, br",
"accept-language": "it",
"content-length": "2",
"content-type": "application/json",
"dnt": "1",
"origin": "https://affluences.com",
"referer": "https://affluences.com/",
"sec-ch-ua": "\"Chromium\";v=\"88\", \"Google Chrome\";v=\"88\", \";Not A Brand\";v=\"99\"",
"sec-ch-ua-mobile": "?0",
"sec-fetch-dest": "empty",
"sec-fetch-mode": "cors",
"sec-fetch-site": "same-site",
"user-agent": user_agent
}
r1= requests.options(l, timeout=1)
r1 = requests.post(l,json={}, headers=headers,timeout=5)









