import cv2
import dropbox
import time
import random

startTime = time.time()
def takeSnapshot():
    num = random.randint(0,100)
    videoCaptureObject = cv2.VideoCapture(0)
    result = True
    while(result):
        ret,frame = videoCaptureObject.read()
        imageName = "img"+str(num)+".png"
        cv2.imwrite(imageName,frame)
        startTime = time.time
        result = False
    return imageName
    print("Snapshot Taken")
    videoCaptureObject.release()
    cv2.destroyAllWindows()

def upload_file(imageName):
    access_token = "RRmnQD7JTaIAAAAAAAAAAe392FipwJ1fOawE7J-3Oy2K87I9drMqNYqEyLfjG3QS"
    file = img_counter
    file_from = file
    file_to = "/Security/"+(imageName)
    dbx = dropbox.Dropbox(access_token)
    f = open(file_from,'rb')
    dbx.files_upload(f.read(),file_to,mode = dropbox.files.WriteMode.overwrite)
    print("Files Uploaded")

def main():
    while(True):
        if((time.time()-startTime) >= 300):
            name = takeSnapshot()
            upload_file(name)

main()