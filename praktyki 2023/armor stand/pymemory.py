import cv2
import mediapipe as mp
from math import hypot
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
import numpy as np
import mediapipe as mp
from math import hypot
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
import numpy as np
from mcrcon import MCRcon as r

mcr = r('localhost', '123')
mcr.connect()

 
cap = cv2.VideoCapture(0) #Checks for camera
 
mpHands = mp.solutions.hands #detects hand/finger
hands = mpHands.Hands()   #complete the initialization configuration of hands
mpDraw = mp.solutions.drawing_utils
 
#To access speaker through the library pycaw 
#devices = AudioUtilities.GetSpeakers()
#interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
#volume = cast(interface, POINTER(IAudioEndpointVolume))
#volbar=400
#volper=0
 
#volMin,volMax = volume.GetVolumeRange()[:2]
x = 0
while True:
    success,img = cap.read() #If camera works capture an image
    imgRGB = cv2.cvtColor(img,cv2.COLOR_BGR2RGB) #Convert to rgb
    
    #Collection of gesture information
    results = hands.process(imgRGB) #completes the image processing.
 
    lmList = [] #empty list
    if results.multi_hand_landmarks: #list of all hands detected.
        #By accessing the list, we can get the information of each hand's corresponding flag bit
        for handlandmark in results.multi_hand_landmarks:
            for id,lm in enumerate(handlandmark.landmark): #adding counter and returning it
                # Get finger joint points
                h,w,_ = img.shape
                cx,cy = int(lm.x*w),int(lm.y*h)
                lmList.append([id,cx,cy]) #adding to the empty list 'lmList'
            mpDraw.draw_landmarks(img,handlandmark,mpHands.HAND_CONNECTIONS)
    
    if lmList != []:
        #getting the value at a point
                        #x      #y
        x1,y1 = lmList[12][1],lmList[12][2]  #thumb
        x2,y2 = lmList[4][1],lmList[4][2]  #index finger
        x3,y3 = lmList[8][1],lmList[8][2]  #thumb
        x4,y4 = lmList[16][1],lmList[16][2]
        x5,y5 = lmList[20][1],lmList[20][2]
        #creating circle at the tips of thumb and index finger
        #cv2.circle(img,(x1,y1),13,(255,0,0),cv2.FILLED) #image #fingers #radius #rgb
        #cv2.circle(img,(x2,y2),13,(255,0,0),cv2.FILLED) #image #fingers #radius #rgb
        cv2.line(img,(x1,y1),(x2,y2),(255,0,0),3)  #create a line b/w tips of index finger and thumb
        cv2.line(img,(x3,y3),(x2,y2),(255,0,0),3)
        cv2.line(img,(x4,y4),(x2,y2),(255,0,0),3)
        cv2.line(img,(x5,y5),(x2,y2),(255,0,0),3)
 
        length = hypot(x2-x1,y2-y1) #distance b/w tips using hypotenuse
        length2 = hypot(x2-x3,y2-y3)
        length3 = hypot(x2-x4,y2-y4)
        length4 = hypot(x2-x5,y2-y5)

 # from numpy we find our length,by converting hand range in terms of volume range ie b/w -63.5 to 0
        #vol = np.interp(length,[30,350],[volMin,volMax]) 
        #volbar=np.interp(length,[30,350],[400,150])
        #volper=np.interp(length,[30,350],[0,100])
        if int(length) < 20 and int(length2) < 20 and int(length3) <20 and int(length4) <20:
            mcr.command('execute as @e[tag=stare] at @s rotated as @p run teleport @s ~ ~ ~ ~'+ str(-180) +' ~')

        elif int(length) < 20 and int(length2) < 20 and int(length3) <20:
            mcr.command('execute as @e[type=armor_stand,tag=stare] at @s unless entity @p[distance=..0.5] facing entity @p feet positioned ^ ^ ^0.3 run tp @s ~ ~ ~')
        elif int(length) < 20 and int(length2) < 20:
        
            mcr.command('data merge entity @e[type=armor_stand,limit=1,tag=stare] {Pose:{LeftArm:['+ str( int(180 - int(y1 / 3))) +'f,'+ str(int (180 - (  int(x1 / 3)) + 90)) +'f,0f]},ShowArms:1}')
            mcr.command('data merge entity @e[type=armor_stand,limit=1,tag=stare] {Pose:{RightArm:['+ str(int(180 - int(y1 / 3))) +'f,'+ str(int (180 - (  int(x1 / 3)) + 90)) +'f,0f]},ShowArms:1}')
            #l = mcr.command('data merge entity @e[type=armor_stand,limit=1,tag=stare] {Pose:{Head:['+ str(int(y1)) +'f,'+ str(int(x1)) +'f,0f]},ShowArms:1}')
            #print()
        elif int(length) < 20:
            l = mcr.command('data merge entity @e[type=armor_stand,limit=1,tag=stare] {Pose:{RightArm:['+ str(int(180 - int(y1 / 3))) +'f,'+ str(int (180 - (  int(x1 / 3)) + 90)) +'f,0f]},ShowArms:1}')
            #print(l)
        elif int(length2) < 20:
            l = mcr.command('data merge entity @e[type=armor_stand,limit=1,tag=stare] {Pose:{LeftArm:['+ str( int(180 - int(y1 / 3))) +'f,'+ str(int (180 - (  int(x1 / 3)) + 90)) +'f,0f]},ShowArms:1}')
            #print(l)

        #print(int(length),'-',int(length2))
        #print(x1,y1)
        print(length,length2,length3,length4)

       
        #volume.SetMasterVolumeLevel(vol, None)
        
        # Hand range 30 - 350
        # Volume range -63.5 - 0.0
        #creating volume bar for volume level 
        #cv2.rectangle(img,(50,150),(85,400),(0,0,255),4) # vid ,initial position ,ending position ,rgb ,thickness
        #cv2.rectangle(img,(50,int(volbar)),(85,400),(0,0,255),cv2.FILLED)
        #cv2.putText(img,f"{int(volper)}%",(10,40),cv2.FONT_ITALIC,1,(0, 255, 98),3)
        #tell the volume percentage ,location,font of text,length,rgb color,thickness
    cv2.imshow('Image',img) #Show the video 
    if cv2.waitKey(1) & 0xff==ord(' '): #By using spacebar delay will stop
        break
mcr.disconnect()
cap.release()     #stop cam       
cv2.destroyAllWindows() #close window
