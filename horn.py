from notify_run import Notify
import time as delay
import requests
from datetime import datetime

def log (info):
	print (datetime.now().strftime("%m/%d/%Y, %H:%M:%S")+" "+info);

notify=Notify()
sleeptime = 900
cookies={}
cookies = {'HGSESSID': 'm5qih5rt0494s5gq13fqbouqf2','PHPSESSID':'m5qih5rt0494s5gq13fqbouqf2','has_logged_in':'true'}

url='https://www.mousehuntgame.com/turn.php'
#url='https://www.mousehuntgame.com'

log("Starting Script")
log(str(notify.info()))
notify.send('Starting Script')
while True:

	log("Calling mousehunt")

	r = requests.get(url, cookies=cookies)
	response=r.text

	#log("Response : "+repsonse)

	if "Rakshit Bansal" not in response:
		log("LoggedIn "+str(False))
		notify.send('Logged out of MH')
		log("Dying as logged out")	
		exit()
	else:
		log("LoggedIn "+str(True))

	timeindex=response.find('Next Hunt');
	time=response[timeindex+39:timeindex+44]
	if time[-1]=="<":
		time=time[:-1]
	
	if time=="Ready":
		ishornready=True
		log("IsHornReady "+str(ishornready))
		sleeptime=3
	else:	
		minsec=time.split(':')
		print minsec
		min=int(minsec[0])
		sec=int(minsec[1])
		timetohorn=min*60 + sec
		log("timetohorn " + str(timetohorn))
		sleeptime=timetohorn+10
	log("Sleeping for "+str(sleeptime))
	delay.sleep(sleeptime)
	log("\n\n\n")		
