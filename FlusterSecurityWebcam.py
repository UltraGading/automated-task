import opencv

def take_snapshot():
    #initializing cv2
    videoCaptureObject = opencv.cv2.VideoCapture(0)
    result = True
    while(result):
        #read the frames while the camera is on
        frame = videoCaptureObject.read()
        #cv2.imwrite() method is used to save an image to any storage device
        opencv.cv2.imwrite("NewPicture1.jpg",frame)
        result = False

    # releases the camera
    videoCaptureObject.release()
    #closes all the window that might be opened while this process
    opencv.cv2.destroyAllWindows()

take_snapshot()