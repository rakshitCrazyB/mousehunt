from notify_run import Notify
import time as delay
import requests
from datetime import datetime

def notif(notice):
	notify.send(datetime.now().strftime("%m/%d/%Y, %H:%M:%S")+" " +notice)

def log (info):
	print (datetime.now().strftime("%m/%d/%Y, %H:%M:%S")+" "+info);

notify=Notify()
sleeptime = 900
cookies={}
hgsessid="VJw34SvCmjGFNB8STCb5MRPN21h8a71eziD4ryFO7sLS4ab3h7JmnPRL9Yng2reT"
phpsessid="jtam5thlg4l3j0od2hbfkbhk41"
cookies = {'HGSESSID': hgsessid,'PHPSESSID': phpsessid,'has_logged_in':'true'}
hgtoken='VJw34SvCmjGFNB8STCb5MRPN21h8a71eziD4ryFO7sLS4ab3h7JmnPRL9Yng2reT'
cookies ={'HG_TOKEN': hgtoken}
url='https://www.mousehuntgame.com/turn.php'
#url='https://www.mousehuntgame.com'

log("Starting Script")
#log(str(notify.info()))
notif('Starting Script')
while True:

	log("Calling mousehunt")

	r = requests.get(url, cookies=cookies)
	response=r.text

	#log("Response : "+repsonse)

	if "Rakshit Bansal" not in response:
		log("LoggedIn "+str(False))
		notif('Logged out of MH')
		log("Dying as logged out")	
		exit()
	else:
		log("LoggedIn "+str(True))

	if "The King has sent you a special reward!" in response:
		log("Kings Reward")
		notif('Kings Reward')
		log("Dying as kings reward")
		exit()

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
		min=int(minsec[0])
		sec=int(minsec[1])
		timetohorn=min*60 + sec
		log("timetohorn " + str(timetohorn))
		sleeptime=timetohorn+10
	log("Sleeping for "+str(sleeptime))
	delay.sleep(sleeptime)
	log("\n\n\n")		

