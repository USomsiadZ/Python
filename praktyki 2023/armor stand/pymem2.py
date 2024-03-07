from cvzone.PoseModule import PoseDetector
import cv2
from math import hypot
poslist = []
cap = cv2.VideoCapture(0)
detector = PoseDetector()
from mcrcon import MCRcon as r
mcr = r('localhost', '123')
mcr.connect()
while True:
    success, img = cap.read()
    img = detector.findPose(img)
    lmList, bboxInfo = detector.findPosition(img)

    cv2.imshow("Image", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    if bboxInfo:
        lmString = ""
       
        #print(lmList[15],'lewy nadgarstek',lmList[16],'prawy nadgarstek')
        x1,y1 = lmList[15][1],lmList[15][2]
        x2,y2 = lmList[16][1],lmList[16][2]
        #print(x1,y1)
        
        #l = mcr.command('/execute as @e[tag=stare] at @s run execute as @s facing entity @p eyes run tp ~ ~1 ~')
        mcr.command('data merge entity @e[type=armor_stand,limit=1,tag=stare] {Pose:{LeftArm:['+ str(int(180 - int(y1 / 3))) +'f,'+ str(int (180 - (  int(x1 / 3)) + 90)) +'f,0f]},ShowArms:1}')
        mcr.command('data merge entity @e[type=armor_stand,limit=1,tag=stare] {Pose:{RightArm:['+ str(int(180 - int(y2 / 3))) +'f,'+ str(int (180 - (  int(x2 / 3)) + 90)) +'f,0f]},ShowArms:1}')
        length = hypot(x2-x1,y2-y1)
        print(length)

        #print(lmList[0],lmList[1])
    x1,y1 = lmList[0][1],lmList[0][2]  #thumb
    cv2.circle(img,(x1,y1),13,(255,0,0),cv2.FILLED)
cap.release()
cv2.destroyAllWindows()