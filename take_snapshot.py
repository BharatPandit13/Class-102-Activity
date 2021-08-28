import cv2

def take_snapshot():
    # read the frames while the camera is on
    videoCaptureObject = cv2.VideoCapture(0)
    result = True
    while(result):
        # cv2.imwrite() method is used to save anything in a storage device
        ret,frame = videoCaptureObject.read()
        cv2.imwrite("NewPicture1.jpg", frame)
        result = False
        # realeases the camera


    videoCaptureObject = release()

    cv2.destroyAllWindows()
    # closes all the window while the process is happening

take_snapshot()
          
