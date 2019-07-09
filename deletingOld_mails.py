import imaplib
import email
from email.parser import HeaderParser
from datetime import date
today = date.today()
now = list(map(int,today.strftime("%d/%m/%Y").split('/')))
mon = {'jan':1,'feb':2,'mar':3,'apr':4,'may':5,'jun':6,'jul':7,'aug':8,'sep':9,'oct':10,'nov':11,'dec':12}

box = imaplib.IMAP4_SSL('imap.gmail.com',993)
box.login('reddy.incognito@gmail.com','luvuz!ndag!')
box.select('Inbox')
_,data=box.search(None, 'ALL')
_, starred = box.search(None, 'FLAGGED')
for num in data[0].split():
	rv, data = box.fetch(num, '(RFC822)')
	if rv != 'OK':
		print("error")
		continue
	msg = email.message_from_string(data[0][1].decode('utf-8'))
	mail_date = msg['Date']
	date_split = list(mail_date.split(' ')[1:4])
	day = int(date_split[0])
	month = mon[date_split[1].lower()]
	year = int(date_split[2])
	if num not in starred[0] and ((year == now[2] and month<(now[1]%12)+1) or year<now[2]):
		print(mail_date)
		box.store(num,'+FLAGS','\\Deleted')
box.expunge()
box.close()
box.logout()
