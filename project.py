######## Importing modules for Tkinter ###########
from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk

######## Importing modules for mediapipe ############
import cv2
from PoseModule import PoseDetector
import numpy as np
import time



########### Accessing Video ###########


def clear():
    global counter
    counter=0


def camselect(cam=1, file1=NONE):
    global cap
    
    if cam:
        
        cap = cv2.VideoCapture(0)
        clear()

    else:
        cap = cv2.VideoCapture(file1)
        if cap==None:
            camvideo()

        clear()

camselect()

detector =PoseDetector()

counter=0
stage = None
pTime=0



def test2():
    global counter
    global pTime
    global stage
    global t

    success, img = cap.read()
    img = cv2.resize(img,(990,640))
    
    img = detector.findPose(img)
    
    hipL=detector.hipL()
    kneeL=detector.kneeL()
    ankleL=detector.ankleL()
    hipR=detector.hipR()
    kneeR=detector.kneeR()
    ankleR=detector.ankleR()


    angle_knee_L=180
    angle_knee_R=180

    if(hipL and kneeL and ankleL):
        
        angle_knee_L=round(detector.calculate_angle(hipL, kneeL, ankleL),2)
        angle_knee_R=round(detector.calculate_angle(hipR, kneeR, ankleR),2)


        if angle_knee_L > 150 and angle_knee_R > 150:
                    stage = "UP"
        if angle_knee_L <= 90 and stage =='UP' and angle_knee_R <= 90:
                    stage="DOWN"
                    counter +=1

                
    cv2.putText(img,f'{angle_knee_L}*',(600,300),cv2.FONT_HERSHEY_COMPLEX,.5,(0,255,255),2, cv2.LINE_AA)
    cv2.putText(img,f'{angle_knee_R}*',(200,300),cv2.FONT_HERSHEY_COMPLEX,.5,(0,255,255),2, cv2.LINE_AA)
     
        # Rep data
    cv2.putText(img, 'REPS', (50,500), 
                cv2.FONT_HERSHEY_COMPLEX, .5, (255,255,255), 1, cv2.LINE_AA)
    cv2.putText(img, str(counter), 
                (50,550), 
                cv2.FONT_HERSHEY_COMPLEX, 1, (255,255,255), 2, cv2.LINE_AA)
    
    # Stage data
    cv2.putText(img, 'STAGE', (150,500), 
                cv2.FONT_HERSHEY_COMPLEX, .5, (255,255,255), 1, cv2.LINE_AA)
    cv2.putText(img, stage, 
                (150,550), 
                cv2.FONT_HERSHEY_COMPLEX, 1, (255,255,255), 2, cv2.LINE_AA)

                    
    #Displaying FPS
    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime
 
    cv2.putText(img, str(int(fps)), (70, 50), cv2.FONT_HERSHEY_PLAIN, 3,
                (255, 0, 0), 3)

    rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    return rgb


################################### Tkinter Code ##########################################


def openfile():
    file1 = filedialog.askopenfilename()
    cam = 0
    camselect(cam, file1)


def openV1():  
    file1 = 'videos/1.mp4'
    cam = 0
    camselect(cam, file1)
    

def openV2(): 
    file1 = 'videos/2.mp4'
    cam = 0
    camselect(cam, file1)
def openV3():  
    file1 = 'videos/3.mp4'
    cam = 0
    camselect(cam, file1)
def openV4():  
    file1 = 'videos/4.mp4'
    cam = 0
    camselect(cam, file1)
    


def camvideo():
    cam = 1
    camselect(cam)



    
def close():
    window.destroy()


# Window Creation
window = Tk()
window.configure(bg='blue')
window.title("Squat Exercise")
width = window.winfo_screenwidth()+10
height = window.winfo_screenheight()+10
window.geometry("%dx%d" % (width, height))
window.minsize(width, height)
window.maxsize(width, height)







################ Design ################
mainlabel = Label(window, text="Squat Exercise", font=(
    "Raleway", 20, "bold", "italic"), bg="blue", fg='yellow')
mainlabel.pack()

f1 = Frame(window, bg='blue')
f1.pack(side=LEFT, fill='y', anchor='nw')

explore = Button(f1, text="Browse File", bg='blue', fg='yellow', font=(
    "Calibri", 14, "bold"), command=openfile).pack(padx=50,pady=10)

livecam = Button(f1, text="Open Web Cam", bg='blue', fg='yellow', font=(
    "Calibri", 14, "bold"), command=camvideo).pack(pady=10)

v1 = Button(f1, text="Test Video 1", bg='blue', fg='yellow', font=(
    "Calibri", 14, "bold"), command=openV1).pack(padx=50,pady=10)
v2 = Button(f1, text="Test Video 2", bg='blue', fg='yellow', font=(
    "Calibri", 14, "bold"), command=openV2).pack(padx=50,pady=10)
v3 = Button(f1, text="Test Video 3", bg='blue', fg='yellow', font=(
    "Calibri", 14, "bold"), command=openV3).pack(padx=50,pady=10)
v4 = Button(f1, text="Test Video 4", bg='blue', fg='yellow', font=(
    "Calibri", 14, "bold"), command=openV4).pack(padx=50,pady=10)


CLR = Button(f1, text="CLear Screen", bg='blue', fg='yellow', font=(
    "Calibri", 14, "bold"), command=clear).pack(padx=50,pady=10)


Exit_Application = Button(f1, text="Exit the Application", bg='blue', fg='yellow', font=(
    "Calibri", 14, "bold"), command=close).pack(pady=50)


############### Video Player #######################


label1 = Label(window, width=960, height=640)
label1.place(x=240, y=50)


def select_img():
    image = Image.fromarray(test2())
    finalImage = ImageTk.PhotoImage(image)
    label1.configure(image=finalImage)
    label1.image = finalImage
    window.after(1, select_img)

select_img()
window.mainloop()