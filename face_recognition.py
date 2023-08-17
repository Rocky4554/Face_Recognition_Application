# import re
from sys import path
from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
import os
import mysql.connector
import cv2
import numpy as np
from tkinter import messagebox
from time import strftime
from datetime import datetime
import pyttsx3 as textspeech
# voice=textspeech.init()
class Face_Recognition:
    
    
    def __init__(self,root):
        self.root=root
        self.root.geometry("1366x768+0+0")
        self.root.title("Face Recognition Pannel")

        # This part is image labels setting start 
        # first header image  
        img=Image.open(r"E:\Final_yar_project\Python_Test_Projects\Images_GUI\bg3.jpg")
        img=img.resize((1366,130),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        # set image as lable
        f_lb1 = Label(self.root,image=self.photoimg)
        f_lb1.place(x=0,y=0,width=1366,height=130)

        # backgorund image 
        bg1=Image.open(r"E:\Final_yar_project\Python_Test_Projects\Images_GUI\bg2.jpg")
        bg1=bg1.resize((1366,768),Image.ANTIALIAS)
        self.photobg1=ImageTk.PhotoImage(bg1)

        # set image as lable
        bg_img = Label(self.root,image=self.photobg1)
        bg_img.place(x=0,y=130,width=1366,height=768)


        #title section
        title_lb1 = Label(bg_img,text="Welcome to Face Recognition Pannel",font=("verdana",30,"bold"),bg="orange",fg="black")
        title_lb1.place(x=0,y=0,width=1366,height=45)

        # Create buttons below the section 
        # ------------------------------------------------------------------------------------------------------------------- 
        # Training button 1
        std_img_btn=Image.open(r"E:\Final_yar_project\Python_Test_Projects\Images_GUI\i7.jfif")
        std_img_btn=std_img_btn.resize((180,180),Image.ANTIALIAS)
        self.std_img1=ImageTk.PhotoImage(std_img_btn)

        std_b1 = Button(bg_img,command=self.face_recog,image=self.std_img1,cursor="hand2")
        std_b1.place(x=600,y=170,width=180,height=180)

        std_b1_1 = Button(bg_img,command=self.face_recog,text="Face Detector",cursor="hand2",font=("tahoma",15,"bold"),bg="white",fg="black")
        std_b1_1.place(x=600,y=350,width=180,height=45)
    #============================================Attendance=================================================

    def mark_attendance(self,i,r,n):
        with open("attendance.csv","r+",newline="\n") as f:
            myDatalist=f.readlines()
            name_list=[]
            for line in myDatalist:
                entry=line.split((", "))
                name_list.append(entry[0])

            if((i not in name_list)) and ((r not in name_list)) and ((n not in name_list)):
                now=datetime.now()
                d1=now.strftime("%d/%m/%Y")
                dtString=now.strftime("%H:%M:%S")
                f.writelines(f"\n{i}, {r}, {n}, {dtString}, {d1}, Present")


    #==============================================face recognition=============================================
    def face_recog(self):
        
        def draw_boundray(img,classifier,scaleFactor,minNeighbors,color,text,clf):
            gray_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            featuers=classifier.detectMultiScale(gray_image,scaleFactor,minNeighbors)

            coord=[]
            
            for (x,y,w,h) in featuers:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
                id,predict=clf.predict(gray_image[y:y+h,x:x+w])

                confidence=int((100*(1-predict/300)))

                conn = mysql.connector.connect(username='root', password='SQLconnect@123',host='localhost',database='face_recognition',port=3306)
                cursor = conn.cursor()

                cursor.execute("select Name from student where Student_ID="+str(id))
                n=cursor.fetchone()
                n="+".join(n)
                # n=str(n)
               
                
                cursor.execute("select Roll_No from student where Student_ID="+str(id))
                r=cursor.fetchone()
                r="+".join(r)
                # r=str(r)
              

                cursor.execute("select Student_ID from student where Student_ID="+str(id))
                i=cursor.fetchone()
                # i="+".join(i)
                # i=str(i)
                i = map(str, i)
                i = "+".join(i)



                if confidence > 77:
                    
                    cv2.putText(img,"Face_matches",(x,y-80),cv2.FONT_HERSHEY_COMPLEX,0.8,(64,15,223),2)
                    cv2.putText(imgBackground,f"Student_ID: {i}",(950,500),cv2.FONT_HERSHEY_COMPLEX,0.5,(0,0,0),2)
                    cv2.putText(imgBackground,f"Roll_no: {r}",(950,565),cv2.FONT_HERSHEY_COMPLEX,0.5,(0,0,0),2)
                    cv2.putText(imgBackground,f"Name: {n}",(950,625),cv2.FONT_HERSHEY_COMPLEX,0.5,(0,0,0),2)  
                    self.mark_attendance(i,r,n)
                    # voice.say('Welcome to class'+ n)
                    # voice.runAndWait()
                else:
                    # imgBackground[44: 44 + 633, 808 : 808 + 414]=imgModeslist[3]
                    # cv2.imshow("Unkown",imgBackground1)
                    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
                    cv2.putText(img,"Unknown Face",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,0),3)    
                       
                    
                coord=[x,y,w,y]
            
            return coord    


        #==========
        def recognize(img,clf,faceCascade):
            coord=draw_boundray(img,faceCascade,1.1,10,(255,25,255),"Face",clf)
            return img
        
        faceCascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.read("clf.xml")

        videoCap=cv2.VideoCapture(0)
        videoCap.set(3,640)
        videoCap.set(4,480)
        
        folderpath= "E:\Final_yar_project\Python_Test_Projects\Resources\modes"
        modepath = os.listdir(folderpath)
        imgModeslist= []
        
        for path in modepath:
            imgModeslist.append(cv2.imread(os.path.join(folderpath,path)))
        
        print(imgModeslist)

        imgBackground = cv2.imread(r"E:\Final_yar_project\Python_Test_Projects\Images_GUI\scanBack.png")
        # imgBackground1 = cv2.imread(r"E:\Final_yar_project\Python_Test_Projects\Resources\background2.png")
        # modevalue=0
        while True:
            ret,img=videoCap.read()  
            
            img=recognize(img,clf,faceCascade)
        
            imgBackground[162: 162 + 480, 55 : 55 + 640]=img
            # imgBackground1[162: 162 + 480, 55 : 55 + 640]=img
            # imgBackground1[162: 162 + 480, 55 : 55 + 640]=img
            # imgBackground[44: 44 + 633, 808 : 808 + 414]=imgModeslist[modevalue]
            # cv2.imshow("Welcome to Face Detector",img)
            cv2.imshow("face",imgBackground)

            if cv2.waitKey(1) & 0xff == ord('q'):
                break
        videoCap.release()
        cv2.destroyAllWindows()




if __name__ == "__main__":
    root=Tk()
    obj=Face_Recognition(root)
    root.mainloop()