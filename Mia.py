#Thư viện python của pythonweb
import speech_recognition as sr
import pyttsx3
from gtts import gTTS
import playsound
import pyaudio
import os
from datetime import datetime
from datetime import date
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
from youtube_search import YoutubeSearch
import sys
sys.path.append('.\\data')
#Thư viện python của developer
import new
from users_compare import users_compare

mia_ear = sr.Recognizer()
mia_mouth = pyttsx3.init()
mia_brain = ""

def EN_doyouwanttosleep(): #Hỏi người dùng có muốn đi ngủ không?
	mia_brain ="Do you want to sleep?"
	print(f"Mia: {mia_brain}")
	say(mia_brain)
	print("Answer 'Yes' or 'No'")
	with sr.Microphone() as mic:
		audio = mia_ear.listen(mic,timeout=5, phrase_time_limit=5)
		# audio = mia_ear.adjust_for_ambient_noise(mic)
	try:
		you = mia_ear.recognize_google(audio)
	except:
		you = input("Your answer: ")
	print("You: "+ you)
	return you

def VN_doyouwanttosleep():	#Hỏi người dùng có muốn đi ngủ không?VN
	mia_brain= "Bạn có muốn đi ngủ không??"
	print("Mia: " + mia_brain)
	noi(gTTS(mia_brain,lang='vi',slow=False))
	print("Answer 'Có' or 'Không'")
	with sr.Microphone() as mic:
		audio = mia_ear.listen(mic,timeout=5, phrase_time_limit=5)
		# audio = mia_ear.adjust_for_ambient_noise(mic)
	try:
		you = mia_ear.recognize_google(audio, language="vi-VN")
	except:
		you = input("Câu trả lời của bạn: ")
	print("You: "+ you)
	return you

def EN_tryagain():	#Lệnh input sai -> Nhập lại
	you = ""
	print("You ->>: {}".format(you))
	mia_brain = "Sorry, I don't know what do you mean. Let's try again!"
	print("Mia: " + mia_brain)
	say(mia_brain)

def VN_tryagain():	#Lệnh input sai -> Nhập lại
	you = ""
	print("You ->>: {}".format(you))
	mia_brain = "Mình xin lỗi, mình nghe không rõ. Bạn nói lại nhé!"
	print("Mia: " + mia_brain)
	noi(gTTS(mia_brain,lang='vi',slow=False))

def VNshutdown(): #Tắt máy
	mia_brain='Tắt máy'
	print("Mia:",mia_brain + " sau 5 giây")
	noi(gTTS(mia_brain + " sau 5 giây",lang='vi',slow=False))
	i=5
	while 0<i<=5:
		print("Mia: " + str(i))
		noi(gTTS(str(i),lang='vi',slow=False))
		i=i-1
	print("Mia: Tắt máy")
	noi(gTTS("Tắt máy",lang='vi',slow=False))
	os.system('shutdown -s')

def ENshutdown(): #Tắt máy
	mia_brain='Shut down'
	print("Mia: ",mia_brain + " the computer after 5 seconds")
	say(mia_brain + " the computer after 5 seconds")
	i=5
	while 0<i<=5:
		print("Mia: " + str(i))
		say(str(i))
		i=i-1
	print("Mia: Shutting down")
	say("Shutting down")
	os.system('shutdown -s')

def VNrestart():	#Khởi động lại
	mia_brain='Khởi động lại'
	print("Mia:",mia_brain + " sau 5 giây")
	noi(gTTS(mia_brain + " sau 5 giây",lang='vi',slow=False))
	i=5
	while 0<i<=5:
		print("Mia: " + str(i))
		noi(gTTS(str(i),lang='vi',slow=False))
		i=i-1
	print("Mia: Khởi động lại")
	noi(gTTS("Khởi động lại",lang='vi',slow=False))
	os.system('shutdown -r')

def ENrestart():	#Khởi động lại
	mia_brain='Restart'
	print("Mia: ",mia_brain + " the computer after 5 seconds")
	say(mia_brain + "the computer after 5 seconds")
	i=5
	while 0<i<=5:
		print("Mia: " + str(i))
		say(str(i))
		i=i-1
	print("Mia: Restarting")
	say("Restarting")
	os.system('shutdown -r')

def VN_cont():	#Continue (Tiếp tục)
	mia_brain="Ok! Cùng tiếp tục công việc nào."
	print("Mia: " + mia_brain)
	noi(gTTS(mia_brain,lang='vi',slow=False))

def EN_cont():	#Continue (Tiếp tục)
	mia_brain="Ok! Let's continue our work!"
	print("Mia: " + mia_brain)
	say(mia_brain)

def noi(output): #Nói Tiếng Việt
	output.save('output.mp3')
	playsound.playsound('output.mp3')
	os.remove('output.mp3') 

def say(output): #Nói Tiếng Anh
	mia_mouth.say(output)
	mia_mouth.runAndWait() 

def VN_time(username): #Xác định lời chào
	x = datetime.now()
	thoigian = int(x.strftime("%H"))
	if 5 < thoigian < 12:
		loichao = "Chào buổi sáng " + str(username)
	elif 12 <= thoigian < 13:
		loichao = str(username) + ", Mình nghỉ bạn nên nghỉ ngơi một tí!"
	elif 13 <= thoigian < 17:
		loichao = "Chào buổi chiều " + str(username)
	elif 17 <= thoigian < 23:
		loichao = "Chào buổi tối " + str(username)
	elif thoigian >= 23 or thoigian <= 5: #Khi vượt quá 11h đêm thì máy sẽ hỏi bạn có nên đi ngủ không?
		now = datetime.now()
		x = now.strftime("%H giờ %M phút %S giây")
		loichao = "Chào buổi tối, " + str(username) + ". Hiện tại đang là " + str(x)
	return loichao

def EN_time(username): #Xác định lời chào
	x = datetime.now()
	thoigian = int(x.strftime("%H"))
	if 5 < thoigian < 12:
		loichao = "Good morning " + str(username)
	elif 12 <= thoigian < 13:
		loichao = str(username) + ", i think you should take a break"
	elif 13 <= thoigian < 17:
		loichao = "Good afternoon " + str(username)
	elif 17 <= thoigian < 23:
		loichao = "Good evening " + str(username)
	elif thoigian >= 23 or thoigian <= 5: #Khi vượt quá 11h đêm thì máy sẽ hỏi bạn có nên đi ngủ không?
		now = datetime.now()
		x = now.strftime("%H hours %M minutes %S seconds")
		loichao = "Good evening, " + str(username) + ". It's " + str(x)
	return loichao

def VN_hi(loichao): #Chào người dùng
	mia_brain = loichao + ", Mình là Mia - trợ lý ảo của bạn. Bạn cần gì?"
	return mia_brain

def EN_hi(loichao): #Chào người dùng
	mia_brain = loichao + ", I'm Mia - your assistant. Can i help you?"
	return mia_brain

def VN_trans(): #Dịch
	mia_brain = "Phần mềm dịch đang được mở"
	print("Mia: ",mia_brain)
	noi(gTTS(mia_brain,lang='vi',slow=False))
	time.sleep(5)
	os.chdir('.\\data')
	os.system("py Translator.py")
	os.chdir('..')
	runai=1
	return runai

def EN_trans(): #Dịch
	mia_brain = "Translator is opening"
	print("Mia: ",mia_brain)
	say(mia_brain)
	time.sleep(5)
	os.chdir('.\\data')
	os.system("py Translator.py")
	os.chdir('..')
	runai=1
	return runai

def VN_Flappybird(): #Flappybird
	mia_brain = "Flappy Bird đang được mở"
	print("Mia: ",mia_brain)
	noi(gTTS(mia_brain,lang='vi',slow=False))
	time.sleep(5)
	os.chdir('.\\data')
	os.system("game.exe")
	os.chdir('..')
	runai=1
	return runai

def EN_Flappybird(): #Flappybird
	mia_brain = "Flappy Bird is opening"
	print("Mia: ",mia_brain)
	say(mia_brain)
	time.sleep(5)
	os.chdir('.\\data')
	os.system("game.exe")
	os.chdir('..')
	runai=1
	return runai

def VN_love(): #Love
	mia_brain = "Mình cũng yêu bạn. Đặc biệt là bố mình - Thearesia"
	return mia_brain

def EN_love(): #Love
	mia_brain = "Yes, i love you too. Especially my father - Thearesia"
	return mia_brain

def VN_day(): #Ngày tháng năm
	now = datetime.now()
	mia_brain=("Hôm nay là ngày %d tháng %d năm %d" % (now.day, now.month, now.year))
	return mia_brain

def EN_day(): #Ngày tháng năm
	today = date.today()
	mia_brain = today.strftime("%B %d, %Y")
	return mia_brain

def VN_clock(): #Đồng hồ
	now = datetime.now()
	mia_brain = now.strftime("%H giờ %M phút %S giây")
	return mia_brain

def EN_clock(): #Đồng hồ
	now = datetime.now()
	mia_brain = now.strftime("%H hours %M minutes %S seconds")
	return mia_brain

def VN_music(you): #Music
	x = you[you.index(" "):]
	results = YoutubeSearch(x, max_results=10).to_dict()
	webbrowser.open('https://www.youtube.com' + str(results[0]['url_suffix']))
	mia_brain = f"Đang bật {x}"
	print("Mia: "+ str(mia_brain))
	noi(gTTS(mia_brain,lang='vi',slow=False))
	time.sleep(240)
	runai=1
	return runai

def EN_music(you): #Music
	x = you[you.index(" "):]
	results = YoutubeSearch(x, max_results=10).to_dict()
	webbrowser.open('https://www.youtube.com' + str(results[0]['url_suffix']))
	mia_brain = f"Playing {x}"
	print("Mia: "+ str(mia_brain))
	say(mia_brain)
	time.sleep(240)
	runai=1
	return runai

def VN_browser(): #Chạy web
	webbrowser.open('https://www.google.com.vn/',new=1)
	mia_brain="Webbrowser đang được bật!"
	print('Mia: ',mia_brain)
	noi(gTTS(mia_brain,lang='vi',slow=False))
	runai=2
	return runai

def EN_browser(): #Chạy web
	webbrowser.open('https://www.google.com.vn/',new=1)
	mia_brain="Webbrowser is opening!"
	print('Mia: ',mia_brain)
	say(mia_brain)
	runai=2
	return runai

def VN_search(): #Google search
	with sr.Microphone() as mic:
		mia_brain="Bạn cần tìm gì?"
		noi(gTTS(mia_brain,lang='vi',slow=False))
		audio = mia_ear.listen(mic,timeout=5, phrase_time_limit=5)
		# audio = mia_ear.adjust_for_ambient_noise(mic)
	try:
		query = mia_ear.recognize_google(audio)
	except:
		query = input("Nhập thông tin cần tìm: ")
	final_url = "https://www.google.com/search?&q=" + query.replace(" ","%20")
	webbrowser.open_new(final_url)
	mia_brain = "tìm kiếm xong"
	noi(gTTS(mia_brain,lang='vi',slow=False))
	time.sleep(5)
	runai=1
	return runai

def EN_search(): #Google search
	with sr.Microphone() as mic:
		mia_brain="Google Search"
		say(mia_brain)
		audio = mia_ear.listen(mic,timeout=5, phrase_time_limit=5)
		# audio = mia_ear.adjust_for_ambient_noise(mic)
	try:
		query = mia_ear.recognize_google(audio)
	except:
		query = input("What to search: ")
	final_url = "https://www.google.com/search?&q=" + query.replace(" ","%20")
	webbrowser.open_new(final_url)
	mia_brain = "Done"
	say(mia_brain)
	time.sleep(5)
	runai=1
	return runai

def VN_facebook(): #Facebook
	webbrowser.open('https://www.facebook.com/',new=1)
	mia_brain="Facebook đang được bật"
	print('you: ',you)
	print('Mia: ',mia_brain)
	noi(gTTS(mia_brain,lang='vi',slow=False))
	runai=2
	return runai

def EN_facebook(): #Facebook
	webbrowser.open('https://www.facebook.com/',new=1)
	mia_brain="Facebook is opening"
	print('you: ',you)
	print('Mia: ',mia_brain)
	say(mia_brain)
	runai=2
	return runai

def VN_wikipedia(): #Wikipedia
	with sr.Microphone() as mic:
		mia_brain="Xin chào tôi là Wikipedia! Mời bạn nói."
		print("Wikipedia: " + mia_brain)
		noi(gTTS(mia_brain,lang='vi',slow=False))
		audio = mia_ear.listen(mic,timeout=10, phrase_time_limit=10)
	try:
		wiki = mia_ear.recognize_google(audio,language="vi-VI")
	except:
		wiki = "Mình xin lỗi!!"
		print("Wikipedia: " + wiki)
		noi(gTTS(wiki,lang='vi',slow=False))
		mia_brain="Mời Mia!"
		print("Wikipedia: " + mia_brain)
		noi(gTTS(mia_brain,lang='vi',slow=False))
		runai=1
		return runai

	if wiki != "Mình xin lỗi":
		wikipedia.set_lang("vi")
		wiki=wikipedia.summary(wiki)
		print("Wikipedia: " + wiki)
		noi(gTTS(wiki,lang='vi',slow=False))
		mia_brain="Đây là cuối của bản tin."
		print("Wikipedia: " + mia_brain)
		noi(gTTS(mia_brain,lang='vi',slow=False))
		mia_brain="Mời Mia!"
		print("Wikipedia: " + mia_brain)
		noi(gTTS(mia_brain,lang='vi',slow=False))
		return runai

def EN_wikipedia(): #Wikipedia
	with sr.Microphone() as mic:
		mia_brain="Hi I'm Wikipedia! How can i help you?"
		print("Wikipedia: " + mia_brain)
		say(mia_brain)
		audio = mia_ear.listen(mic,timeout=10, phrase_time_limit=10)
	try:
		wiki = mia_ear.recognize_google(audio)
	except:
		wiki = "I'm so sorry!!"
		print("Wikipedia: " + wiki)
		say(wiki)
		mia_brain="Mia turn!"
		print("Wikipedia: " + mia_brain)
		say(mia_brain)
		runai=1
		return runai

	if wiki != "I'm so sorry!!":
		wikipedia.set_lang("en")
		wiki=wikipedia.summary(wiki)
		print("Wikipedia: " + wiki)
		say(wiki)
		mia_brain="It's the end."
		print("Wikipedia: " + mia_brain)
		say(mia_brain)
		mia_brain="Mia turn!"
		print("Wikipedia: " + mia_brain)
		say(mia_brain)
		runai=1
		return runai

def VN_ays(): #Are you sure
	mia_brain="Bạn có chắc không?"
	print("Mia: " + mia_brain)
	noi(gTTS(mia_brain,lang='vi',slow=False))
	print("Hệ thống: Trả lời 'Có' hoặc 'Không'")
	with sr.Microphone() as mic:
		audio = mia_ear.listen(mic,timeout=5, phrase_time_limit=5)
		# audio = mia_ear.adjust_for_ambient_noise(mic)
	try:
		you = mia_ear.recognize_google(audio, language="vi-VN")
	except:
		you = input("Câu trả lời của bạn: ")
	print("You: "+ you)
	return you

def EN_ays(): #are you sure
	mia_brain="Are you sure?"
	print("Mia: " + mia_brain)
	say(mia_brain)
	print("System: Answer 'Yes' or 'No'")
	with sr.Microphone() as mic:
		audio = mia_ear.listen(mic,timeout=5, phrase_time_limit=5)
		# audio = mia_ear.adjust_for_ambient_noise(mic)
	try:
		you = mia_ear.recognize_google(audio)
	except:
		you = input("Your answer: ")
	print("You: "+ you)
	return you

def VN_shutdown(): #tắt máy
	ans = VN_ays()
	if "Có" in ans or "có" in ans:
		VNshutdown()
		runai=2
		return runai
	else:
		VN_cont()
		runai=1
		return runai

def EN_shutdown(): #Tắt máy
	ans = EN_ays()
	if "Yes" in ans or "yes" in ans:
		ENshutdown()
		runai=2
		return runai
	else:
		EN_cont()
		runai=1
		return runai

def VN_restart(): #Khởi động lại
	ans = VN_ays()
	if "Có" in ans or "có" in ans:
		VNrestart()
		runai=2
		return runai
	else:
		VN_cont()
		runai=1
		return runai

def EN_restart(): #Khởi động lại
	ans = EN_ays()
	if "Yes" in ans or "yes" in ans:
		ENrestart()
		runai=2
		return runai
	else:
		EN_cont()
		runai=1
		return runai

def VN_break(): #Nghỉ ngơi
	mia_brain='Mia sẽ dừng hoạt động trong 15p'
	print("Mia: ",mia_brain)
	noi(gTTS(mia_brain,lang='vi',slow=False))
	time.sleep(900)
	runai=1
	return runai

def EN_break(): #Nghỉ ngơi
	mia_brain='Mia will stop for 15 minutes'
	print("Mia: ",mia_brain)
	say(mia_brain)
	time.sleep(900)
	runai=1
	return runai

def VN_bye(): #Tắt AI
	mia_brain="Goodbye, hẹn gặp lại"
	print("Mia: ",mia_brain)
	noi(gTTS(mia_brain,lang='vi',slow=False))
	runai=2
	return runai

def EN_bye(): #Tắt AI
	mia_brain="Goodbye, see you later"
	print("Mia: ",mia_brain)
	say(mia_brain)
	runai=2
	return runai

def VN_goodnight(): #Ngủ
	mia_brain="Good night"
	print("Mia: ",mia_brain)
	noi(gTTS(mia_brain,lang='vi',slow=False))
	runai=2
	return runai

def EN_goodnight(): #Ngủ
	mia_brain="Good night"
	print("Mia: ",mia_brain)
	say(mia_brain)
	runai=2
	return runai

def VN_volumedown(): #Giảm volume
	mia_brain="Volume đang được giảm: 25!"
	volume.SetMasterVolumeLevel(-20, None)
	return mia_brain

def EN_volumedown(): #Giảm volume
	mia_brain="Volume is decreasing: 25!"
	volume.SetMasterVolumeLevel(-20, None)
	return mia_brain

def VN_volumeup(): #Tăng volume
	mia_brain="Volume đang được tăng: 75!"
	volume.SetMasterVolumeLevel(-4.4, None)
	return mia_brain

def EN_volumeup(): #Tăng volume
	mia_brain="Volume is raising: 75!"
	volume.SetMasterVolumeLevel(-4.4, None)
	return mia_brain

def VN_teach(): #Dạy AI - Machine Learning
	learn = input("Nếu mình nghe <input>: ")
	answer = input("Mình sẽ trả lời <output>: ")
	if learn != "" and answer != "":
		file1 = open("mia3.py","a+")
		file1.seek(157)
		file1.write("\n" + '	' + 'elif ' + '"' + str(learn) + '"' + ' in you:\n')
		file1.writelines('		mia_brain = ' + '"' + str(answer) + '"' + '\n')
		file1.writelines('		return mia_brain')
		mia_brain = "Dạy học thành công! Cảm ơn bạn đã giúp đỡ!"
	else:
		mia_brain = "Dạy học thất bại"
	return mia_brain

def EN_teach(): #Dạy AI - Machine Learning
	learn = input("When i hear <input>: ")
	answer = input("i will say <output>: ")
	if learn != "" and answer != "":
		file1 = open("mia3.py","a+")
		file1.seek(157)
		file1.write("\n" + '	' + 'elif ' + '"' + str(learn) + '"' + ' in you:\n')
		file1.writelines('		mia_brain = ' + '"' + str(answer) + '"' + '\n')
		file1.writelines('		return mia_brain')
		mia_brain = "Learning succeed! Thanks for your teaching!"
	else:
		mia_brain = "Learning failed"
	return mia_brain

def main():
	ok=False
	os.system('cls' if os.name=='nt' else 'clear')
	os.chdir('.\\data')
	# Ngôn ngữ người dùng
	while ok == False:
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
			ok=True

	#Nhập tên người dùng
	while ok == True:
		file1 = open("username.txt","r+")
		file1.seek(0)  
		if file1 == "":
			# print(file1)
			new.username()
		else:
			username=file1.read()
			if "EN" in l or "en" in l or "En" in l or "eN" in l:
				print("User's name: " + username)
			else:
				print("Tên người dùng: " + username)
			ok=False

	#Nhập giao diện người dùng
	while ok == False:
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
			ok=True

	os.chdir('..')
	# Đổi màu giao diện
	if "light" in theme or "Light" in theme or "l" in theme or "L" in theme:
		color ( text = "black" , bg = "bright white" , delay = 0.67 ,repeat = -1 , dict = {} )
	else:
		color ( text = "bright white" , bg = "black" , delay = 0.67 ,repeat = -1 , dict = {} )

	if "EN" in l or "en" in l or "En" in l or "eN" in l:
		EN(username)
	else:
		VN(username)

def VN(username):
	# Các biến số ban đầu
	mia_ear = sr.Recognizer()
	mia_mouth = pyttsx3.init()
	mia_brain = ""

	# Get default audio device using PyCAW
	devices = AudioUtilities.GetSpeakers()
	interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
	volume = cast(interface, POINTER(IAudioEndpointVolume))

	loichao=VN_time(username)
	x = datetime.now()
	thoigian = int(x.strftime("%H"))
	o=0 
	stopai=0

	while True:
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
			# Get current volume 
			currentVolumeDb = volume.GetMasterVolumeLevel()
			currentVol=currentVolumeDb
			volume.SetMasterVolumeLevel(-28, None)
			currentVolumeDb2 = volume.GetMasterVolumeLevel()
			times=currentVolumeDb - currentVolumeDb2
			volume.SetMasterVolumeLevel(currentVolumeDb, None)

			if thoigian >= 23 or thoigian <= 3: #Ngủ đei
				ans = VN_doyouwanttosleep()
				if "có" in ans or "Có" in ans:
					VNshutdown()
					break
				else:
					VN_cont()

			mia_brain = loichao + ", Mình là Mia. Bạn cần gì?" 
			print("Mia: ",mia_brain)
			noi(gTTS(mia_brain,lang='vi',slow=False))

			#Vòng lặp chính của chương trình (Dừng khi 3 lần lặp lỗi)
			while stopai<3:
				with sr.Microphone() as mic:
					mia_brain = "Mình đang nghe đây"
					print("Mia: ",mia_brain)
					noi(gTTS(mia_brain,lang='vi',slow=False))
					# audio = mia_ear.listen(mic)
					while currentVolumeDb>=currentVolumeDb2:
						currentVolumeDb=currentVolumeDb - 1
						volume.SetMasterVolumeLevel(currentVolumeDb -0.4, None) # decreases the system volume by 1
						time.sleep(0.7/times)
					audio = mia_ear.listen(mic,timeout=5, phrase_time_limit=5)
					while currentVolumeDb<=currentVol:
						currentVolumeDb=currentVolumeDb + 1
						volume.SetMasterVolumeLevel(currentVolumeDb, None) # decreases the system volume by 1
						time.sleep(0.7/times)
					print("Mia: ...")
				try:
					you = mia_ear.recognize_google(audio, language="vi-VN")
				except:
					if stopai == 2:
						you=input("Nhập câu lệnh: ")
					else:
						stopai=stopai+1
						VN_tryagain()
						continue		
			
				print("You: " + you)

				if you != '':
					mia_brain = VN_compare(you,username,loichao)
					if mia_brain == None:
						mia_brain = users_compare(you,username,loichao)
						if mia_brain == None:
							print(f"Mia: Bạn có thể xem qua các kết quả tìm kiếm của {you}\n" + str('"https://www.google.com/search?&q="' + you.replace(" ","%20")))
							mia_brain="Xin lỗi! Mình chưa được dạy về nó, hãy thử lại nhé."
				else:
					VN_tryagain()
					continue

				if mia_brain == 2:
					break
				elif mia_brain == 1:
					continue
				else:
					print("Mia: "+ str(mia_brain))
					noi(gTTS(mia_brain,lang='vi',slow=False))

def EN(username):
	# Các biến số ban đầu
	mia_ear = sr.Recognizer()
	mia_mouth = pyttsx3.init()
	mia_brain = ""

	# Get default audio device using PyCAW
	devices = AudioUtilities.GetSpeakers()
	interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
	volume = cast(interface, POINTER(IAudioEndpointVolume))

	loichao=EN_time(username)
	x = datetime.now()
	thoigian = int(x.strftime("%H"))
	o=0 
	stopai=0

	while True:
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
		
		if "Hi Mia" in you or "hi Mia" in you or "hey Mia" in you or "Hey Mia" in you or "Hey" in you or "hey" in you or "Chào Mia" in you:
			o=2
			# Get current volume 
			currentVolumeDb = volume.GetMasterVolumeLevel()
			currentVol=currentVolumeDb
			volume.SetMasterVolumeLevel(-28, None)
			currentVolumeDb2 = volume.GetMasterVolumeLevel()
			times=currentVolumeDb - currentVolumeDb2
			volume.SetMasterVolumeLevel(currentVolumeDb, None)

			if thoigian >= 23 or thoigian <= 3: #Ngủ đei
				ans = EN_doyouwanttosleep()
				if "yes" in ans or "Yes" in ans:
					ENshutdown()
					break
				else:
					EN_cont()

			mia_brain = loichao + ", I'm Mia. Can i help you?" 
			print("Mia: ",mia_brain)
			say(mia_brain)

			#Vòng lặp chính của chương trình (Dừng khi 3 lần lặp lỗi)
			while stopai<3:
				with sr.Microphone() as mic:
					mia_brain = "I'm listening"
					print("Mia: ",mia_brain)
					say(mia_brain)
					# audio = mia_ear.listen(mic)
					while currentVolumeDb>=currentVolumeDb2:
						currentVolumeDb=currentVolumeDb - 1
						volume.SetMasterVolumeLevel(currentVolumeDb -0.4, None) # decreases the system volume by 1
						time.sleep(0.7/times)
					audio = mia_ear.listen(mic,timeout=5, phrase_time_limit=5)
					while currentVolumeDb<=currentVol:
						currentVolumeDb=currentVolumeDb + 1
						volume.SetMasterVolumeLevel(currentVolumeDb, None) # decreases the system volume by 1
						time.sleep(0.7/times)
					print("Mia: ...")
				try:
					you = mia_ear.recognize_google(audio)
				except:
					if stopai == 2:
						you=input("Your command: ")
					else:
						stopai=stopai+1
						EN_tryagain()
						continue		
			
				print("You: " + you)

				if you != '':
					mia_brain = EN_compare(you,username,loichao)
					if mia_brain == None:
						mia_brain = users_compare(you,username,loichao)
						if mia_brain == None:
							print(f"Mia: You can check these search for {you}\n" + str('"https://www.google.com/search?&q="' + you.replace(" ","%20")))
							mia_brain="Sorry, I haven't learnt it yet! Let's try something else."
				else:
					EN_tryagain()
					continue

				if mia_brain == 2:
					break
				elif mia_brain == 1:
					continue
				else:
					print("Mia: "+ str(mia_brain))
					say(mia_brain)

def VN_compare(you,username,loichao):
	if "Chào" in you or "Xin chào" in you or "hi" in you or "Hello" in you:
		mia_brain = VN_hi(loichao)
		return mia_brain
	elif "dịch" in you or "từ điển" in you:
		mia_brain = VN_trans()
		return mia_brain
	elif "Flappy Bird" in you:
		mia_brain = VN_Flappybird()
		return mia_brain
	elif "yêu" in you:
		mia_brain = VN_love()
		return mia_brain
	elif "ngày" in you:
		mia_brain = VN_day()
		return mia_brain
	elif "giờ" in you:
		mia_brain = VN_clock()
		return mia_brain
	elif "Play" in you or "play" in you or "nhạc" in you:
		if "music" in you:
			mia_brain = "Đang mở youtube"
			webbrowser.open('https://www.youtube.com/',new=1)
			return mia_brain
		else:
			mia_brain = VN_music(you)
			return mia_brain
	elif "Opera" in you or "Google" in you or "duyệt web" in you or "Duyệt web" in you: 
		mia_brain = VN_browser()
		return mia_brain
	elif "tìm kiếm" in you:
		mia_brain = VN_search()
		return mia_brain
	elif "Facebook" in you:
		mia_brain = VN_facebook()
		return mia_brain
	elif "Wikipedia" in you:
		mia_brain = VN_wikipedia()
		return mia_brain
	elif "tắt máy" in you or "Tắt máy" in you or "Shut down" in you or "shut down" in you:
		mia_brain = VN_shutdown()
		return mia_brain
	elif "khởi động lại" in you or "Khởi động lại" in you or "restart" in you or "Restart" in you:
		mia_brain = VN_restart()
		return mia_brain
	elif "ngủ" in you or "Ngủ" in you or "sleep" in you:
		mia_brain = VN_break()
		return mia_brain
	elif "bye" in you or "tạm biệt" in you or "Tạm biệt" in you:
		mia_brain = VN_bye()
		return mia_brain
	elif "Goodnight" in you or "goodnight" in you:
		mia_brain = VN_goodnight()
		return mia_brain
	elif "what the f***" in you:
		mia_brain = "fuck you"
		return mia_brain
	elif "giảm volume" in you:
		mia_brain = VN_volumedown()
		return mia_brain
	elif "tăng volume" in you:
		mia_brain = VN_volumeup()
		return mia_brain

def EN_compare(you,username,loichao):
	if "Hi" in you or "Hello" in you or "hi" in you or "hello" in you:
		mia_brain = EN_hi(loichao)
		return mia_brain
	elif "translate" in you or "Translate" in you:
		mia_brain = EN_trans()
		return mia_brain
	elif "Flappy Bird" in you:
		mia_brain = EN_Flappybird()
		return mia_brain
	elif "love" in you:
		mia_brain = EN_love()
		return mia_brain
	elif "today" in you or "date" in you or "day" in you:
		mia_brain = EN_day()
		return mia_brain
	elif "time" in you:
		mia_brain = EN_clock()
		return mia_brain
	elif "Play" in you or "play" in you:
		if "music" in you:
			mia_brain = "Opening Youtube"
			webbrowser.open('https://www.youtube.com/',new=1)
			return mia_brain
		else:
			mia_brain = EN_music(you)
			return mia_brain
	elif "Opera" in you or "Google" in you or "webbrowser" in you or "Webbrowser" in you: 
		mia_brain = EN_browser()
		return mia_brain
	elif "search" in you:
		mia_brain = EN_search()
		return mia_brain
	elif "Facebook" in you:
		mia_brain = EN_facebook()
		return mia_brain
	elif "Wikipedia" in you:
		mia_brain = EN_wikipedia()
		return mia_brain
	elif "Turn off" in you or "turn off" in you or "Shut down" in you or "shut down" in you:
		mia_brain = EN_shutdown()
		return mia_brain
	elif "restart" in you or "Restart" in you:
		mia_brain = EN_restart()
		return mia_brain
	elif "Sleep" in you or "break" in you or "sleep" in you:
		mia_brain = EN_break()
		return mia_brain
	elif "bye" in you or "Bye" in you:
		mia_brain = EN_bye()
		return mia_brain
	elif "Goodnight" in you or "goodnight" in you:
		mia_brain = EN_goodnight()
		return mia_brain
	elif "what the f***" in you:
		mia_brain = "fuck you"
		return mia_brain
	elif "volume down" in you:
		mia_brain = EN_volumedown()
		return mia_brain
	elif "volume up" in you:
		mia_brain = EN_volumeup()
		return mia_brain

if __name__ == "__main__":
	main()