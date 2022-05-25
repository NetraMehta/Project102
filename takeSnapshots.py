import cv2
import time
import random
import dropbox

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
    access_token = 'sl.BIQSWz64ekfICnI0Hw_yeDgmtPCXa7n4WUlqNAcmnLuNWc6gVeFUjGJL9T6IyaT4UOfoF1ztct3w0nRSJh4Ou5utkJPlItBZYkyxueE30TjX1xjrCVtgrlK7nCxBlP8YTdHCvTw'

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