
#Johnny Heuschmidt and Mason Clewis Visual Detection Program using opencv
#The end goal would be to code this into a car that has visual input so it knows when to stop. 

#this installs opencv
#!pip install opencv-python
# this is a test comment
import cv2
import numpy as np
import random 

def overall():
    bglist= ["signsnostop.png", "stopsign1.png", "stopsign2.png", "straighton.jfif","mansign.jfif","zeatles.jfif"]
    used = []
    bgindex = random.randint(0,len(bglist)-1)
    used.append(bgindex)
    background = bglist[bgindex]
    print(used)
    #background image 1 is the first stopsign image stopsign1
    back1_img = cv2.imread(background, cv2.IMREAD_UNCHANGED)

    #the needle image is the patch that is scanned across the background image
    needle_img = cv2.imread('needlesamesize.jpg', cv2.IMREAD_UNCHANGED)




    #This displays the needle for troubleshooting
    """
    cv2.imshow('Needle', needle_img)
    cv2.waitKey()
    cv2.destroyAllWindows()
    """

    #here I am making the background larger so the image scan works more accurately 
    resizedbg = cv2.resize(back1_img, (800,800), fx=2.5, fy=2.5)

    cv2.imshow('Background', resizedbg)
    cv2.waitKey(3000)

    cv2.destroyAllWindows()

    resizedneedle = cv2.resize(needle_img, (220,220), fx=2.5, fy=2.5)
    result = cv2.matchTemplate(resizedbg, resizedneedle, cv2.TM_CCOEFF_NORMED)

    #cv2.imshow('Result', result)
    #cv2.waitKey()
    #cv2.destroyAllWindows()

    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    #print(cv2.minMaxLoc(result))
    print(max_val)
    threshold = .30
    if np.any(result >= threshold):
        print("STOP BRO!")
    else:
        print("keep driving")
play = True
while play = True:
    again = input("Do you want to see another image? (y/n)")
    if again == "y":
        overall()
    else:
        print("thanks for playing")