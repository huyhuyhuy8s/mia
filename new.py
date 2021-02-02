def language():
	file1 = open("language.txt","w") 
	L= input("VI for Vietnamese or EN for English.\nVI cho Tiếng Việt hoặc EN cho Tiếng Anh. \nSelect language (Chọn ngôn ngữ): ")
	file1.writelines(L) 
	file1.close() #to change file access modes 
	  
	file1 = open("language.txt","r+")  
	  
	print ("Output of Read function is (Kết quả ghi được): ")
	# print (file1.read()) 
	file1.seek(0)  
	if file1 == "":
		# print(file1)
		file1.close()
	else:
		language=file1.read()
		print(language)

def theme():	
	file1 = open("theme.txt","w") 
	L= input("Choose your theme <Dark or Light>: \n Chọn giao diện <Tối(D) hoặc Sáng(L)>")
	file1.writelines(L) 
	file1.close() #to change file access modes 
	  
	file1 = open("theme.txt","r+")  
	  
	print ("Output of Read function is (Kết quả ghi được): ")
	# print (file1.read()) 
	file1.seek(0)  
	if file1 == "":
		# print(file1)
		file1.close()
	else:
		user=file1.read()
		print(user)

def username():
	file1 = open("username.txt","w") 
	L= input("Enter User_name (Nhập tên người dùng): ")
	file1.writelines(L) 
	file1.close() #to change file access modes 
	  
	file1 = open("username.txt","r+")  
	  
	print ("Output of Read function is (Kết quả ghi được): ")
	# print (file1.read()) 
	file1.seek(0)  
	if file1 == "":
		# print(file1)
		file1.close()
	else:
		user=file1.read()
		print(user)

def main():
	language()
	username()
	theme()
	
if __name__ == "__main__":
	main()