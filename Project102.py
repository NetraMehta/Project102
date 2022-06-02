from time import time
import cv2
import time
import dropbox
import random

name = input('Enter your name here: ')
id = input('Enter your ID here: ')

if ((name == 'Netra') and (id == '123')):

	def save_details():
		with open('name.txt', 'a') as n:
			n.write(name)

		with open('id.txt', 'a') as i:
			i.write(id)

	save_details()

	startTime = time.time()

	def take_snapshot():
		number = random.randint(0,100)

		videoCaptureObject = cv2.VideoCapture(0)

		result = True

		while(result):
			ret,frame = videoCaptureObject.read()
			img_name = 'img'+str(number)+'.png'

			cv2.imwrite(img_name, frame)

			result = False

		print('snapshot taken')

		videoCaptureObject.release()
		cv2.destroyAllWindows()

		return img_name

	def upload_files(img_name):
		access_token = 'sl.BIzSlA6T19P6Fs9saMk954rf3pRS8Uw4BaHB7d7RadcUsT_5r0jsCIMy12va4mepP0xxpWxxctzW1cPFE7LlfV8p8PyUv1hhPDzeLGEOkIOB5qLEDwJ_JSjuoZv9uNHjAXLVEKiSTQvc'

		file = img_name
		file_from = file
		file_to = '/newFolder1/'+(img_name)

		dbx = dropbox.Dropbox(access_token)

		with open(file_from, 'rb') as f:
			dbx.files_upload(f.read(), file_to, mode = dropbox.files.WriteMode.overwrite)
			print('File uploaded')

	def main():
		while(True):
			if((time.time()-startTime)>=3):
				name = take_snapshot()
				upload_files(name)

	main()

else:
	print('Name or password is incorrect')