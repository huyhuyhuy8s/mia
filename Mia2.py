# Nhập thư viện của pythonweb
import speech_recognition as sr
import pyttsx3
from gtts import gTTS
import playsound
import pyaudio
import os
from datetime import datetime
import wikipedia
import webbrowser
import time
import os
import pycaw
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
from Color_Console import *
import math
import subfile
import subfileVN
import new 

# Các biến số ban đầu
mia_ear = sr.Recognizer()
mia_mouth = pyttsx3.init()
mia_brain = ""

# Get default audio device using PyCAW
devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))

#Lập trình câu lệnh của lập trình viên
def webbrowsers():	#Chạy duyệt web
	webbrowser.open('https://www.google.com.vn/',new=1)
	mia_brain="Ok! Webbrowser is opened"
	print('you: ',you)
	print('Mia: ',mia_brain)
	mia_mouth.say(mia_brain)
	mia_mouth.runAndWait()

def wiki(keyword): #Tìm kiếm trong wiki
	try:
		print('**finding on wiki**')
		print(wikipedia.summary(keyword))	#search wiki
	except:
		print('Can not open')
		print('')
	run = False

def areyousure(): #ARE YOU SURE?
	print("Mia: Are you sure?")
	mia_mouth.say("Are you sure?")
	mia_mouth.runAndWait()
	print("Answer 'Yes' or 'No'")
	areyousurerun = 0
	with sr.Microphone() as mic:
		audio = mia_ear.listen(mic,timeout=5, phrase_time_limit=5)
		# audio = mia_ear.adjust_for_ambient_noise(mic)
	try:
		you = mia_ear.recognize_google(audio)
	except:
		you = input("Your answer: ")
	print("You: "+ you)
	return you

def doyouwanttosleep(): #Hỏi người dùng có muốn đi ngủ không?
	print("Mia: Do you want to sleep?")
	mia_mouth.say("Do you want to sleep?")
	mia_mouth.runAndWait()
	print("Answer 'Yes' or 'No'")
	areyousurerun = 0
	with sr.Microphone() as mic:
		audio = mia_ear.listen(mic,timeout=5, phrase_time_limit=5)
		# audio = mia_ear.adjust_for_ambient_noise(mic)
	try:
		you = mia_ear.recognize_google(audio)
	except:
		you = input("Your answer: ")
	print("You: "+ you)
	return you

def doyouwanttosleepVN():	#Hỏi người dùng có muốn đi ngủ không?VN
	mia_brain= "Bạn có muốn đi ngủ không??"
	print("Mia: " + mia_brain)
	output = gTTS(mia_brain,lang='vi',slow=False)
	noi()
	print("Answer 'Có' or 'Không'")
	areyousurerun = 0
	with sr.Microphone() as mic:
		audio = mia_ear.listen(mic,timeout=5, phrase_time_limit=5)
		# audio = mia_ear.adjust_for_ambient_noise(mic)
	try:
		you = mia_ear.recognize_google(audio, language="vi-VN")
	except:
		you = input("Câu trả lời của bạn: ")
	print("You: "+ you)
	return you

def shutdown():	#Tắt máy
	mia_brain='shut down'
	print("Mia: ",mia_brain + " the computer after 5 seconds")
	mia_mouth.say(mia_brain + " the computer after 5 seconds")
	mia_mouth.runAndWait()
	print("Mia: 5")
	mia_mouth.say("5")
	mia_mouth.runAndWait()
	print("Mia: 4")
	mia_mouth.say("4")
	mia_mouth.runAndWait()
	print("Mia: 3")
	mia_mouth.say("3")
	mia_mouth.runAndWait()
	print("Mia: 2")
	mia_mouth.say("2")
	mia_mouth.runAndWait()
	print("Mia: 1")
	mia_mouth.say("1")
	mia_mouth.runAndWait()
	print("Mia: Shutting down")
	mia_mouth.say("Shutting down")
	mia_mouth.runAndWait()
	os.system('shutdown -s')

def restart(): #Khởi động lại máy
	mia_brain='restart'
	print("Mia: ",mia_brain + " the computer after 5 seconds")
	mia_mouth.say(mia_brain + " the computer after 5 seconds")
	mia_mouth.runAndWait()
	print("Mia: 5")
	mia_mouth.say("5")
	mia_mouth.runAndWait()
	print("Mia: 4")
	mia_mouth.say("4")
	mia_mouth.runAndWait()
	print("Mia: 3")
	mia_mouth.say("3")
	mia_mouth.runAndWait()
	print("Mia: 2")
	mia_mouth.say("2")
	mia_mouth.runAndWait()
	print("Mia: 1")
	mia_mouth.say("1")
	mia_mouth.runAndWait()
	print("Mia: Restarting")
	mia_mouth.say("Restarting")
	mia_mouth.runAndWait()
	os.system('shutdown -r')

def tryagain():	#Lệnh input sai -> Nhập lại
	you = ""
	print("You ->>: {}".format(you))
	print("Mia: Sorry, I don't know what do you mean. Let's try again!")
	mia_brain = "Sorry, I don't know what do you mean. Let's try again!"
	mia_mouth.say(mia_brain)
	mia_mouth.runAndWait()

def tryagainVN():	#Lệnh input sai -> Nhập lại
	you = ""
	print("You ->>: {}".format(you))
	mia_brain = "Mình xin lỗi, mình nghe không rõ. Bạn nói lại nhé!"
	print("Mia: " + mia_brain)
	output = gTTS(mia_brain,lang='vi',slow=False)
	noi()

def cont():	#Continue (Tiếp tục)
	mia_brain="Ok! Let's continue our work."
	print("Mia: " + mia_brain)
	mia_mouth.say(mia_brain)
	mia_mouth.runAndWait()

def contVN():	#ContinueVN (Tiếp tục)
	mia_brain="Ok! Tiếp tục công việc nào."
	print("Mia: " + mia_brain)
	output = gTTS(mia_brain,lang='vi',slow=False)
	noi()

def playmusic():	#Chạy nhạc
	global run
	print("Ex: E:\\Music")
	music_dir = input("Nhập đường dẫn folder nhạc: ")
	songs = os.listdir(music_dir) 
	  
	print("Files and directories in '", music_dir, "' :")  
	  
	# print the list 
	print(songs) 
	qq = input("Nhập số thứ tự của bài hát: ")
	os.startfile(os.path.join(music_dir,songs[int(qq)]))
	run = False#Nhac

def noi():	#Nói tiếng Việt
	output.save('output.mp3')
	playsound.playsound('output.mp3')
	os.remove('output.mp3')
	# time.sleep(1)

def stopai():	#Dừng AI
	stopfile1 = open("stopai.txt","w")
	stopfile1.seek(0)
	stopfile1.writelines("1")

def continueai():	#Trở lại vòng lặp
	continuefile1 = open("continueai.txt","w")
	continuefile1.seek(0)
	continuefile1.writelines("1")

def writecontinueai(continueai):	#Xuất file continueai.txt=0
	stopfile1 = open("continueai.txt","w")
	stopfile1.seek(0)
	stopfile1.writelines(continueai)

def writestopai(stopai):	#Xuất file stopai.txt=0
	stopfile1 = open("stopai.txt","w")
	stopfile1.seek(0)
	stopfile1.writelines(stopai)

writecontinueai("0")

# Ngôn ngữ người dùng
os.chdir('.\\data')
file1 = open("language.txt","r+")
file1.seek(0)  
if file1 == "":
	# print(file1)
	new.language()
else:
	l=file1.read()
	if "EN" in l or "en" in l or "En" in l or "eN" in l:
		print("Using language: " + l)
	else:
		print("Ngôn ngữ đang sử dụng: " + l)

#Nhập tên người dùng
file1 = open("username.txt","r+")
file1.seek(0)  
if file1 == "":
	# print(file1)
	new.username()
else:
	user=file1.read()
	if "EN" in l or "en" in l or "En" in l or "eN" in l:
		print("User name: " + user)
	else:
		print("Tên người dùng: " + user)


#Nhập giao diện người dùng
file1 = open("theme.txt","r+")
file1.seek(0)  
if file1 == "":
	# print(file1)
	new.theme()
else:
	theme=file1.read()
	if "EN" in l or "en" in l or "En" in l or "eN" in l:
		print("Using theme: " + theme)
	else:
		print("Giao diện đang sử dụng: " + theme)

os.chdir('..')

# Đổi màu giao diện
if "light" in theme or "Light" in theme or "l" in theme or "L" in theme:
	color ( text = "black" , bg = "bright white" , delay = 0.67 ,repeat = -1 , dict = {} )
else:
	color ( text = "bright white" , bg = "black" , delay = 0.67 ,repeat = -1 , dict = {} )

#Mia Tiếng Anh
if "EN" in l or "en" in l or "En" in l or "eN" in l:
	#Xác định thời gian
	x = datetime.now()
	thoigian = int(x.strftime("%H"))
	if 5 < thoigian < 12: #Buổi sáng
		loichao = "Good morning " + str(user)
	elif 12 <= thoigian < 13:	#Buổi trưa
		loichao = str(user) + ", i think you should take a break"
	elif 13 <= thoigian < 17:	#Buổi chiều	
		loichao = "Good afternoon " + str(user)
	elif 17 <= thoigian < 23:	#Buổi tối
		loichao = "Good evening " + str(user)
	elif thoigian >= 23 or thoigian <= 3: #Khi vượt quá 11h đêm thì máy sẽ hỏi bạn có nên đi ngủ không?
		now = datetime.now()
		x = now.strftime("%H hours %M minutes %S seconds")
		loichao = "Good evening, " + str(user) + ". It's " + str(x)
	#OK GOOGLE (On working)
	o=0 
	while o<2:
		with sr.Microphone() as mic:
			mia_brain="I'm waitting!"
			print("Mia: " + mia_brain)
			# audio = mia_ear.listen(mic)
			audio = mia_ear.listen(mic,timeout=10, phrase_time_limit=10)
		try:
			you = mia_ear.recognize_google(audio)
		except:
			you = ""
		print("You: " + you)
		
		if "Hi Mia" in you or "hi Mia" in you or "hey Mia" in you or "Hey Mia" in you or "Hey" in you or "hey" in you:
			o=2
			stopai=0	

			# Get current volume 
			currentVolumeDb = volume.GetMasterVolumeLevel()
			currentVol=currentVolumeDb
			volume.SetMasterVolumeLevel(-28, None)
			currentVolumeDb2 = volume.GetMasterVolumeLevel()
			times=currentVolumeDb - currentVolumeDb2
			volume.SetMasterVolumeLevel(currentVolumeDb, None)

			if thoigian >= 23 or thoigian <= 3: #Ngủ đei
				ans = doyouwanttosleep()
				if "yes" in ans or "Yes" in ans:
					shutdown()
					break
				else:
					cont()
			
			mia_brain = str(loichao) + ", I'm Mia. What can i help you?" 
			print("Mia: ",mia_brain)
			mia_mouth.say(mia_brain)
			mia_mouth.runAndWait()
			
			#Vòng lặp chính của chương trình (Dừng khi 3 lần lặp lỗi)
			while stopai<3:
				with sr.Microphone() as mic:
					mia_brain = "I'm listening"
					print("Mia: " + mia_brain)
					mia_mouth.say(mia_brain)
					mia_mouth.runAndWait()
					# audio = mia_ear.listen(mic)
					while currentVolumeDb>=currentVolumeDb2:
						currentVolumeDb=currentVolumeDb - 1
						volume.SetMasterVolumeLevel(currentVolumeDb -0.4, None) # decreases the system volume by 1
						time.sleep(1/times)
					audio = mia_ear.listen(mic,timeout=5, phrase_time_limit=5)
					while currentVolumeDb<=currentVol:
						currentVolumeDb=currentVolumeDb + 1
						volume.SetMasterVolumeLevel(currentVolumeDb, None) # decreases the system volume by 1
						time.sleep(1/times)
					print("Mia: ...")
				try:
					you = mia_ear.recognize_google(audio)
				except:
					if stopai == 2:
						you=input("Your command: ")
					else:
						stopai=stopai+1
						tryagain()
						continue
				
				print("You: " + you)

				if you != "":
					file1 = open("you.txt","w")
					file1.writelines(you)
					file1.close()
					checksubfile=subfile.compare()
					if checksubfile != None:
						mia_brain=checksubfile
					else: # Xuất hiện từ lạ chưa được lập trình sẵn (Input Error)
						mia_brain="Sorry, I haven't learnt it yet! Let's try something else."
				else:
					tryagain()
					continue

				stopfile1 = open("stopai.txt","r+")
				stopfile1.seek(0)
				stopai=int(stopfile1.read())

				continuefile1 = open("continueai.txt","r+")
				continuefile1.seek(0)
				continueai=int(continuefile1.read())

				if continueai == 0:
					print("Mia: "+ str(mia_brain))
					mia_mouth.say(mia_brain)
					mia_mouth.runAndWait()
				else:
					writecontinueai("0")

			stopfile1 = open("stopai.txt","w")
			stopfile1.seek(0)
			stopfile1.writelines("0")

			writecontinueai("0")	

		elif you == "":
			print("System: Type 'Hi Mia'")
			you = input()
			if "Hi Mia" in you or "HI MIA" in you or "hi mia" in you or "Hi mia" in you or "himia" in you or "hi Mia" in you or "hey Mia" in you or "Hey Mia" in you or "Hey" in you or "hey" in you:
				print("You: " + you)

				o=2
				stopai=0	

				# Get current volume 
				currentVolumeDb = volume.GetMasterVolumeLevel()
				currentVol=currentVolumeDb
				volume.SetMasterVolumeLevel(-28, None)
				currentVolumeDb2 = volume.GetMasterVolumeLevel()
				times=currentVolumeDb - currentVolumeDb2
				volume.SetMasterVolumeLevel(currentVolumeDb, None)

				if thoigian >= 23 or thoigian <= 3: #Ngủ đei
					ans = doyouwanttosleep()
					if "yes" in ans or "Yes" in ans:
						shutdown()
						break
					else:
						cont()
				
				mia_brain = str(loichao) + ", I'm Mia. What can i help you?" 
				print("Mia: ",mia_brain)
				mia_mouth.say(mia_brain)
				mia_mouth.runAndWait()
				
				#Vòng lặp chính của chương trình (Dừng khi 3 lần lặp lỗi)
				while stopai<3:
					with sr.Microphone() as mic:
						mia_brain = "I'm listening"
						print("Mia: " + mia_brain)
						mia_mouth.say(mia_brain)
						mia_mouth.runAndWait()
						# audio = mia_ear.listen(mic)
						while currentVolumeDb>=currentVolumeDb2:
							currentVolumeDb=currentVolumeDb - 1
							volume.SetMasterVolumeLevel(currentVolumeDb -0.4, None) # decreases the system volume by 1
							time.sleep(1/times)
						audio = mia_ear.listen(mic,timeout=5, phrase_time_limit=5)
						while currentVolumeDb<=currentVol:
							currentVolumeDb=currentVolumeDb + 1
							volume.SetMasterVolumeLevel(currentVolumeDb, None) # decreases the system volume by 1
							time.sleep(1/times)
						print("Mia: ...")
					try:
						you = mia_ear.recognize_google(audio)
					except:
						if stopai == 2:
							you=input("Your command: ")
						else:
							stopai=stopai+1
							tryagain()
							continue
					
					print("You: " + you)

					if you != "":
						file1 = open("you.txt","w")
						file1.writelines(you)
						file1.close()
						checksubfile=subfile.compare()
						if checksubfile != None:
							mia_brain=checksubfile
						else: # Xuất hiện từ lạ chưa được lập trình sẵn (Input Error)
							mia_brain="Sorry, I haven't learnt it yet! Let's try something else."
					else:
						tryagain()
						continue

					stopfile1 = open("stopai.txt",mode = 'r+')
					stopfile1.seek(0)
					stopai=int(stopfile1.read())

					continuefile1 = open("continueai.txt",mode = 'r+')
					continuefile1.seek(0)
					continueai=int(continuefile1.read())

					if continueai == 0:
						print("Mia: "+ str(mia_brain))
						mia_mouth.say(mia_brain)
						mia_mouth.runAndWait()
					else:
						writecontinueai("0")

				stopfile1 = open("stopai.txt","w")
				stopfile1.seek(0)
				stopfile1.writelines("0")

				writecontinueai("0")	

		else:
			mia_brain="If you want to active Mia, please say or type: 'Hi Mia' or 'Hey Mia'"
			print("Mia: ",mia_brain)
			continue


#Mia Tiếng Việt
elif "VI" in l or "vi" in l or "Vi" in l or "vI" in l:
	#OK GOOGLE (On working)
	#Xác định thời gian
	x = datetime.now()
	thoigian = int(x.strftime("%H"))
	if 5 < thoigian < 12:
		loichao = "Chào buổi sáng " + str(user)
	elif 12 <= thoigian < 13:
		loichao = str(user) + ", Mình nghỉ bạn nên nghỉ ngơi một tí!"
	elif 13 <= thoigian < 17:
		loichao = "Chào buổi chiều " + str(user)
	elif 17 <= thoigian < 23:
		loichao = "Chào buổi tối " + str(user)
	elif thoigian >= 23 or thoigian <= 3: #Khi vượt quá 11h đêm thì máy sẽ hỏi bạn có nên đi ngủ không?
		now = datetime.now()
		x = now.strftime("%H giờ %M phút %S giây")
		loichao = "Chào buổi tối, " + str(user) + ". Hiện tại đang là " + str(x)
		
	o=0 
	while o<2:
		with sr.Microphone() as mic:
			mia_brain="Đang chờ lệnh!"
			print("Mia: " + mia_brain)
			# audio = mia_ear.listen(mic)
			audio = mia_ear.listen(mic,timeout=10, phrase_time_limit=10)
		try:
			you = mia_ear.recognize_google(audio)
		except:
			you = ""
		print("You: " + you)
		
		if "Hi Mia" in you or "hi Mia" in you or "hey Mia" in you or "Hey Mia" in you or "Hey" in you or "hey" in you or "Chào Mia" in you:
			o=2
			stopai=0	

			# Get current volume 
			currentVolumeDb = volume.GetMasterVolumeLevel()
			currentVol=currentVolumeDb
			volume.SetMasterVolumeLevel(-28, None)
			currentVolumeDb2 = volume.GetMasterVolumeLevel()
			times=currentVolumeDb - currentVolumeDb2
			volume.SetMasterVolumeLevel(currentVolumeDb, None)
			
			if thoigian >= 23 or thoigian <= 3: #Ngủ đei
				ans = doyouwanttosleepVN()
				if "có" in ans or "Có" in ans:
					shutdown()
					break
				else:
					contVN()
			
			mia_brain = loichao + ", Mình là Mia. Bạn cần gì?" 
			print("Mia: ",mia_brain)
			output = gTTS(mia_brain,lang='vi',slow=False)
			noi()

			
			#Vòng lặp chính của chương trình (Dừng khi 3 lần lặp lỗi)
			while stopai<3:
				with sr.Microphone() as mic:
					mia_brain = "Mình đang nghe đây"
					print("Mia: ",mia_brain)
					output = gTTS(mia_brain,lang='vi',slow=False)
					noi()
					# audio = mia_ear.listen(mic)
					while currentVolumeDb>=currentVolumeDb2:
						currentVolumeDb=currentVolumeDb - 1
						volume.SetMasterVolumeLevel(currentVolumeDb -0.4, None) # decreases the system volume by 1
						time.sleep(1/times)
					audio = mia_ear.listen(mic,timeout=5, phrase_time_limit=5)
					while currentVolumeDb<=currentVol:
						currentVolumeDb=currentVolumeDb + 1
						volume.SetMasterVolumeLevel(currentVolumeDb, None) # decreases the system volume by 1
						time.sleep(1/times)
					print("Mia: ...")
				try:
					you = mia_ear.recognize_google(audio, language="vi-VN")
				except:
					if stopai == 2:
						you=input("Nhập câu lệnh: ")
					else:
						stopai=stopai+1
						tryagainVN()
						continue		
				
				print("You: " + you)

				if you != "":
					file1 = open("you.txt","w")
					file1.writelines(you)
					file1.close()
					checksubfile=subfileVN.compare()
					if checksubfile != None:
						mia_brain=checksubfile
					else: # Xuất hiện từ lạ chưa được lập trình sẵn (Input Error)
						mia_brain="Xin lỗi! Mình chưa được dạy về nó, hãy thử lại nhé."
				else:
					tryagain()
					continue

				stopfile1 = open("stopai.txt","r+")
				stopfile1.seek(0)
				stopai=int(stopfile1.read())

				continuefile1 = open("continueai.txt","r+")
				continuefile1.seek(0)
				continueai=int(continuefile1.read())

				if continueai == 0:
					print("Mia: "+ str(mia_brain))
					output = gTTS(mia_brain,lang='vi',slow=False)
					noi()

				else:
					writecontinueai("0")

			stopfile1 = open("stopai.txt","w")
			stopfile1.seek(0)
			stopfile1.writelines("0")

			writecontinueai("0")	

		elif you == "":
			print("Hệ thống: Nhập 'Hi Mia' hoặc 'Hey Mia")
			you = input()
			if "Hi Mia" in you or "HI MIA" in you or "hi mia" in you or "Hi mia" in you or "himia" in you or "hi Mia" in you or "hey Mia" in you or "Hey Mia" in you or "Hey" in you or "hey" in you:
				print("You: " + you)

				o=2
				stopai=0	

				# Get current volume 
				currentVolumeDb = volume.GetMasterVolumeLevel()
				currentVol=currentVolumeDb
				volume.SetMasterVolumeLevel(-28, None)
				currentVolumeDb2 = volume.GetMasterVolumeLevel()
				times=currentVolumeDb - currentVolumeDb2
				volume.SetMasterVolumeLevel(currentVolumeDb, None)
				
				if thoigian >= 23 or thoigian <= 3: #Ngủ đei
					ans = doyouwanttosleepVN()
					if "có" in ans or "Có" in ans:
						shutdown()
						break
					else:
						contVN()
				
				mia_brain = loichao + ", Mình là Mia. Bạn cần gì?" 
				print("Mia: ",mia_brain)
				output = gTTS(mia_brain,lang='vi',slow=False)
				noi()

				
				#Vòng lặp chính của chương trình (Dừng khi 3 lần lặp lỗi)
				while stopai<3:
					with sr.Microphone() as mic:
						mia_brain = "Mình đang nghe đây"
						print("Mia: ",mia_brain)
						output = gTTS(mia_brain,lang='vi',slow=False)
						noi()
						# audio = mia_ear.listen(mic)
						while currentVolumeDb>=currentVolumeDb2:
							currentVolumeDb=currentVolumeDb - 1
							volume.SetMasterVolumeLevel(currentVolumeDb -0.4, None) # decreases the system volume by 1
							time.sleep(1/times)
						audio = mia_ear.listen(mic,timeout=5, phrase_time_limit=5)
						while currentVolumeDb<=currentVol:
							currentVolumeDb=currentVolumeDb + 1
							volume.SetMasterVolumeLevel(currentVolumeDb, None) # decreases the system volume by 1
							time.sleep(1/times)
						print("Mia: ...")
					try:
						you = mia_ear.recognize_google(audio, language="vi-VN")
					except:
						if stopai == 2:
							you=input("Nhập câu lệnh: ")
						else:
							stopai=stopai+1
							tryagainVN()
							continue
					
					print("You: " + you)

					if you != "":
						file1 = open("you.txt","w")
						file1.writelines(you)
						file1.close()
						checksubfile=subfileVN.compare()
						if checksubfile != None:
							mia_brain=checksubfile
						else: # Xuất hiện từ lạ chưa được lập trình sẵn (Input Error)
							mia_brain="Xin lỗi! Mình chưa được dạy về nó, hãy thử lại nhé."
					else:
						tryagain()
						continue

					stopfile1 = open("stopai.txt","r+")
					stopfile1.seek(0)
					stopai=int(stopfile1.read())

					continuefile1 = open("continueai.txt","r+")
					continuefile1.seek(0)
					continueai=int(continuefile1.read())

					if continueai == 0:
						print("Mia: "+ str(mia_brain))
						output = gTTS(mia_brain,lang='vi',slow=False)
						noi()

					else:
						writecontinueai("0")

				stopfile1 = open("stopai.txt","w")
				stopfile1.seek(0)
				stopfile1.writelines("0")

				writecontinueai("0")

		else:
			mia_brain="Nếu bạn muốn khởi động Mia, hẫy nói hoặc nhập: 'Hi Mia' hoặc 'Hey Mia'"
			print("Mia: ",mia_brain)
			continue

else:
	tryagain()