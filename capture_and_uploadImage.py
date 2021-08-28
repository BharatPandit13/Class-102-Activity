import cv2
import dropBox
import time
import random

start_time=time.time()

def take_snapshot():
    number = number.randint(0,100)
    #initizalized cv2
    videoCaptureObject = cv2.VideoCapture(0)
    result = True
    while(result):
        #read the frames while the camera is on
        ret,frame = videoCaptureObject.read()
        #cv2.imwrite() method is used to save an image to any storage device
        img_name = "img"+str(number)+".png"
        cv2.imwrite(img_name,frame)
        start_time = time.time()
        result = False
    return img_name
    #realases the camera
    print("snapshot_taken")
    # closes all the windows that might be open while this process is happening
    cv2.destroyAllWindows()

def upload_file(img_name):
    access_token = "riFu6Ybhc9AAAAAAAAAALaZlr0KQZp4W5yPr5fRlLudO7HyuxSz5BpczxsAwjvTN"
    file=img_name
    file_to = "/testFolder/"+(img_name)
    dbx = dropbox.Dropbox(access_token)

    with open(file_from,"rb") as f:
        dbx.files_upload(f.read(), file_to,mode=dropbox.files.WriteMode.overWrite)
        print("file uploaded")

def main():
    while(True):
        if((time.time() - start_time) >= 5):
            name=take_snapshot
            upload_file(name)

main()