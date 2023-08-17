

from tkinter import *
from tkinter import ttk

from train import Train
from PIL import Image, ImageTk
import tkinter
from student import Student
from train import Train
from face_recognition import Face_Recognition
from attendance import Attendance
from developer import Developer
import os
from time import strftime
from datetime import datetime
from helpsupport import Helpsupport
# from main import Face_Recognition_System
from login import Login
# .........
from sys import path
from PIL import Image, ImageTk
import os
import mysql.connector
import cv2
import numpy as np
from tkinter import messagebox
from chatbot import chat
from request import Request



class Frontview:

    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face_Recogonition_System")

# This part is image labels setting start
        # first header image  E:\Final_yar_project\Python_Test_Projects\Images_GUI
        img = Image.open(
            r"E:\Final_yar_project\Python_Test_Projects\Images_GUI\bg3.jpg")
        img = img.resize((1766, 130), Image.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img)

        # set image as lable
        f_lb1 = Label(self.root, image=self.photoimg)
        f_lb1.place(x=0, y=0, width=1766, height=130)

        # #header title section
        # title_lb = Label(f_lb1,text="Welcome",font=("verdana",30,"bold"),bg="black",fg="white")
        # title_lb.place(x=0,y=0,width=266,height=45)

        # backgorund image
        bg1 = Image.open(r"E:\Final_yar_project\Python_Test_Projects\Images_GUI\anti-spoofing-techniques-face-recognition-1920x1080.jpg")
        bg1 = bg1.resize((1546, 710), Image.LANCZOS)
        self.photobg1 = ImageTk.PhotoImage(bg1)

        # set image as lable
        bg_img = Label(self.root, image=self.photobg1)
        bg_img.place(x=0, y=10, width=1546, height=710)

        # banner title section
#====================================PROJECT TITLE==================================================================
        txt = "ace IdentifierF"
        title_lb1 = Label(bg_img, text=txt, font=(
            "verdana", 25, "bold"), bg="orange", fg="black")
        title_lb1.place(x=0, y=0, width=1550, height=45)
        
        index = 0
        text = ''

        def slider():
            nonlocal index,text
            if index >= len(txt):
                index =-1
                text = ''
                title_lb1.configure(text=text)
            else:
                text = text + txt[index]
                title_lb1.configure(text=text)
                index += 1
            title_lb1.after(100, slider)
        
        slider() 
         
   
    #     self.title_lb1 = Label(bg_img, text="", font=("verdana", 30, "bold"), bg="orange", fg="black")
    #     self.title_lb1.place(x=0, y=0, width=500, height=50)

    #     self.text = "Identify People In Institution Using Facial Recognition"
    #     self.index = 0
    #     self.count = 0
    #     self.max_count = 5

    #     self.slider()

    # def slider(self):
    #     if self.count < self.max_count:
    #         if self.index >= len(self.text):
    #             self.index = -1
    #             self.title_lb1.configure(text="")
    #         else:
    #             text = self.text[self.index:]
    #             self.title_lb1.configure(text=text)
    #             self.index += 1
    #         root.after(100, self.slider)
    #     else:
    #         root.destroy()    
    #=========================================TIME FUNCTION==================================================        
        # TIME
        def time():
            string = strftime('%H:%M:%S %p')
            lbl.config(text=string)
            lbl.after(1000, time)

        lbl = Label(bg_img, font=('times new roman', 14, 'bold'),
                    background='brown', foreground='white')
        lbl.place(x=0, y=(-5), width=110, height=50)
        time()

        # Create buttons below the section
        # -------------------------------------------------------------------------------------------------------------------
#==============================Admin Pannel==========================================================================
        img_size=(320,120)
        
        def on_enter(e):
            # std_b1.configure(cursor="hand2")
            std_b1_1.configure(image=self.std_img2)
            # std_b1_1.configure(bg="green")
        def on_leave(e):
            std_b1_1.configure(image=self.std_img1)
            # std_b1_1.configure(bg="lightblue")
        
        
        std_img_btn = Image.open(r"E:\Final_yar_project\Python_Test_Projects\Images_GUI\Adminpannelnew_blue.png")
        std_img_btn = std_img_btn.resize(img_size, resample=Image.LANCZOS)
        self.std_img1 = ImageTk.PhotoImage(std_img_btn)
        
        std_img_btn1 = Image.open(r"E:\Final_yar_project\Python_Test_Projects\Images_GUI\Adminpannelnew_orange.png")
        std_img_btn1 = std_img_btn1.resize(img_size, resample=Image.LANCZOS)
        self.std_img2 = ImageTk.PhotoImage(std_img_btn1)
     
        # label_button=Label(root,image=std_img_btn,cursor="hand2")
        # label_button.place(x=200, y=70, width=160, height=100)
        # std_b1 =Button(bg_img, command=self.main_pannels,image= self.std_img1, cursor="hand2")
        # std_b1.place(x=100, y=100, width=280, height=180)
        
        
        # std_b1.bind("<Enter>",on_enter)
        # std_b1.bind("<Leave>",on_leave)
        frame1 = Frame(bg_img, borderwidth=2, relief="sunken", bg="black")
        frame1.place(x=100, y=100, width=320, height=100)

        std_b1_1 = Button(frame1, command=self.main_pannels,borderwidth=0,image= self.std_img1, text="Admin Pannel",cursor="hand2", font=("Monotype", 15, "bold"), bg="lightblue", fg="black",highlightthickness=0)
        # std_b1_1.place(x=100, y=120, width=320, height=100)
        std_b1_1.pack(fill="both", expand=True)
        
        std_b1_1.bind("<Enter>",on_enter)
        std_b1_1.bind("<Leave>",on_leave)
        
#=============================SCAN BUTTON=======================================================================
        # Detect Face  button 2
        det_img_btn=Image.open(r"E:\Final_yar_project\Python_Test_Projects\Images_GUI\Scanhere_blue.png")
        # det_img_btn=det_img_btn.resize((400,200),Image.LANCZOS)
        self.det_img1=ImageTk.PhotoImage(det_img_btn)
        
        det_img_btn1=Image.open(r"E:\Final_yar_project\Python_Test_Projects\Images_GUI\Scanhere_red.png")
        self.det_img2=ImageTk.PhotoImage(det_img_btn1)
        # det_b1 = Button(bg_img,command=self.face_rec,image=self.det_img1,cursor="hand2")
        # det_b1.place(x=800,y=100,width=280,height=180)
        def on_enter(e):
            # std_b1.configure(cursor="hand2")
           
            det_b1_1.configure(image=self.det_img1)
        def on_leave(e):
            det_b1_1.configure(image=self.det_img2) 
            
        # det_b1_1 = Button(bg_img,image-self.det_img1,command=self.face_rec,text="Face Detector",cursor="hand2",font=("Monotype",15,"bold"),bg="lightblue",fg="black")
        # det_b1_1 = Button(bg_img,command=self.face_rec")
        # det_b1_1 = Label(bg_img,image=self.det_img1,cursor="hand2")
        # det_b1_1.place(x=700,y=610,width=420,height=58)
        # round=PhotoImage(file='E:\Final_yar_project\Python_Test_Projects\Resources\download.jpg')
        # det_b1_1 = Button(bg_img, image=self.det_img1,border="2px solid black", cursor="hand2", highlightthickness=0,command=self.face_rec)
        # det_b1_1.place(x=710,y=610,width=400, height=75)
        frame = Frame(bg_img, borderwidth=2, relief="sunken", bg="black")
        frame.place(x=710, y=610, width=400, height=75)

        det_b1_1 = Button(frame, image=self.det_img2, borderwidth=0, cursor="hand2", highlightthickness=0, command=self.face_rec)
        det_b1_1.pack(fill="both", expand=True)
        # det_b1_1.pack(pady=20)
        # det_b1_1.pack(pady=20)
        
        det_b1_1.bind("<Enter>",on_enter)
        det_b1_1.bind("<Leave>",on_leave)
        # Attendance System  button 3
        # att_img_btn = Image.open(
        #     r"E:\Final_yar_project\Python_Test_Projects\Images_GUI\i12.jfif")
        # att_img_btn = att_img_btn.resize((180, 180), Image.ANTIALIAS)
        # self.att_img1 = ImageTk.PhotoImage(att_img_btn)

        # att_b1 = Button(bg_img, command=self.student_pannels,
        #                 image=self.att_img1, cursor="hand2",)
        # att_b1.place(x=900, y=100, width=280, height=180)

        # att_b1_1 = Button(bg_img, command=self.student_pannels, text="Request for Register",
        #                   cursor="hand2", font=("Monotype", 15, "bold"), bg="lightblue", fg="black")
        # att_b1_1.place(x=900, y=280, width=280, height=50)
        
        # adding button.................
    #     std_img_btn = Image.open(r"Images_GUI\i7.jfif")
    #     std_img_btn = std_img_btn.resize((180, 180), Image.ANTIALIAS)
    #     self.std_img1 = ImageTk.PhotoImage(std_img_btn)

    #     std_b1 = Button(bg_img, command=self.face_recog,
    #                     image=self.std_img1, cursor="hand2")
    #     std_b1.place(x=600, y=170, width=180, height=180)

    #     std_b1_1 = Button(bg_img, command=self.face_recog, text="Face Detector",
    #                       cursor="hand2", font=("tahoma", 15, "bold"), bg="white", fg="black")
    #     std_b1_1.place(x=600, y=350, width=180, height=45)
    # # =====================Attendance===================

    # def mark_attendance(self, i, r, n):
    #     with open("attendance.csv", "r+", newline="\n") as f:
    #         myDatalist = f.readlines()
    #         name_list = []
    #         for line in myDatalist:
    #             entry = line.split((","))
    #             name_list.append(entry[0])

    #         if ((i not in name_list)) and ((r not in name_list)) and ((n not in name_list)):
    #             now = datetime.now()
    #             d1 = now.strftime("%d/%m/%Y")
    #             dtString = now.strftime("%H:%M:%S")
    #             f.writelines(f"\n{i}, {r}, {n}, {dtString}, {d1}, Present")

    # # ================face recognition==================

    # def face_recog(self):
    #     def draw_boundray(img, classifier, scaleFactor, minNeighbors, color, text, clf):
    #         gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    #         featuers = classifier.detectMultiScale(
    #             gray_image, scaleFactor, minNeighbors)

    #         coord = []

    #         for (x, y, w, h) in featuers:
    #             cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 3)
    #             id, predict = clf.predict(gray_image[y:y+h, x:x+w])

    #             confidence = int((100*(1-predict/300)))

    #             conn = mysql.connector.connect(
    #                 username='root', password='SQLconnect@123', host='localhost', database='face_recognition', port=3306)
    #             cursor = conn.cursor()

    #             cursor.execute(
    #                 "select Name from student where Student_ID="+str(id))
    #             n = cursor.fetchone()
    #             # n="+".join(n)
    #             n = str(n)

    #             cursor.execute(
    #                 "select Roll_No from student where Student_ID="+str(id))
    #             r = cursor.fetchone()
    #            # r="+".join(r)
    #             r = str(r)

    #             cursor.execute(
    #                 "select Student_ID from student where Student_ID="+str(id))
    #             i = cursor.fetchone()
    #            # i="+".join(i)
    #             i = str(i)

    #             if confidence > 77:
    #                 cv2.putText(
    #                     img, f"Student_ID:{i}", (x, y-80), cv2.FONT_HERSHEY_COMPLEX, 0.8, (64, 15, 223), 2)
    #                 cv2.putText(
    #                     img, f"Name:{n}", (x, y-55), cv2.FONT_HERSHEY_COMPLEX, 0.8, (64, 15, 223), 2)
    #                 cv2.putText(
    #                     img, f"Roll-No:{r}", (x, y-30), cv2.FONT_HERSHEY_COMPLEX, 0.8, (64, 15, 223), 2)
    #                 self.mark_attendance(i, r, n)
    #             else:
    #                 cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 3)
    #                 cv2.putText(img, "Unknown Face", (x, y-5),
    #                             cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 0), 3)

    #             coord = [x, y, w, y]

    #         return coord

    #     # ==========
    #     def recognize(img, clf, faceCascade):
    #         coord = draw_boundray(img, faceCascade, 1.1,
    #                               10, (255, 25, 255), "Face", clf)
    #         return img

    #     faceCascade = cv2.CascadeClassifier(
    #         "haarcascade_frontalface_default.xml")
    #     clf = cv2.face.LBPHFaceRecognizer_create()
    #     clf.read("clf.xml")

    #     videoCap = cv2.VideoCapture(0)

    #     while True:
    #         ret, img = videoCap.read()
    #         img = recognize(img, clf, faceCascade)
    #         cv2.imshow("Welcome to Face Detector", img)

    #         if cv2.waitKey(1) & 0xff == ord('q'):
    #             break
    #     videoCap.release()
    #     cv2.destroyAllWindows()

        #  # Help  Support  button 4
        # hlp_img_btn=Image.open(r"E:\Final_yar_project\Python_Test_Projects\Images_GUI\i15.jfif")
        # hlp_img_btn=hlp_img_btn.resize((280,180),Image.ANTIALIAS)
        # self.hlp_img1=ImageTk.PhotoImage(hlp_img_btn)

        # hlp_b1 = Button(bg_img,command=self.helpSupport,image=self.hlp_img1,cursor="hand2")
        # hlp_b1.place(x=940,y=100,width=280,height=180)

        # hlp_b1_1 = Button(bg_img,command=self.helpSupport,text="Help Support",cursor="hand2",font=("Monotype",15,"bold"),bg="lightblue",fg="black")
        # hlp_b1_1.place(x=940,y=280,width=280,height=45)

        # # Top 4 buttons end.......
        # # ---------------------------------------------------------------------------------------------------------------------------
        #=======================================Request Button=============================================
        def on_enter(e):
            req_b1_1.configure(image=self.req_imggg)
        def on_leave(e):
            req_b1_1.configure(image=self.req_imgg) 
            
        req_img=Image.open(r"E:\Final_yar_project\Python_Test_Projects\Images_GUI\Request_darkblue.png")
        req_img=req_img.resize((300,70),Image.ANTIALIAS)
        self.req_imgg=ImageTk.PhotoImage(req_img)
        
        req_img1=Image.open(r"E:\Final_yar_project\Python_Test_Projects\Images_GUI\Request_blue.png")
        req_img1=req_img1.resize((300,70),Image.ANTIALIAS)
        self.req_imggg=ImageTk.PhotoImage(req_img1)
        
        req_b1_1 = Button(text="Request", cursor="hand2",image=self.req_imgg, command=self.request)
        req_b1_1.place(x=110, y=260, width=300, height=60)
            
        req_b1_1.bind("<Enter>",on_enter)
        req_b1_1.bind("<Leave>",on_leave)
        # Start below buttons.........
        #  # Train   button 5
        # tra_img_btn=Image.open(r"E:\Final_yar_project\Python_Test_Projects\Images_GUI\i14.jfif")
        # tra_img_btn=tra_img_btn.resize((280,180),Image.ANTIALIAS)
        # self.tra_img1=ImageTk.PhotoImage(tra_img_btn)

        # tra_b1 = Button(bg_img,command=self.train_pannels,image=self.tra_img1,cursor="hand2",)
        # tra_b1.place(x=250,y=370,width=280,height=180)

        # tra_b1_1 = Button(bg_img,command=self.train_pannels,text="Data Train",cursor="hand2",font=("Monotype",15,"bold"),bg="lightblue",fg="black")
        # tra_b1_1.place(x=250,y=510,width=280,height=45)

        # # # Photo   button 6
        # # pho_img_btn=Image.open(r"E:\Final_yar_project\Python_Test_Projects\Images_GUI\qr1.png")
        # # pho_img_btn=pho_img_btn.resize((180,180),Image.ANTIALIAS)
        # # self.pho_img1=ImageTk.PhotoImage(pho_img_btn)

        # # pho_b1 = Button(bg_img,command=self.open_img,image=self.pho_img1,cursor="hand2",)
        # # pho_b1.place(x=480,y=370,width=180,height=180)

        # # pho_b1_1 = Button(bg_img,command=self.open_img,text="QR-Codes",cursor="hand2",font=("Monotype",15,"bold"),bg="lightblue",fg="black")
        # # pho_b1_1.place(x=480,y=510,width=180,height=45)

        # # Developers   button 7  710-370  ; 710-510
        # dev_img_btn=Image.open(r"E:\Final_yar_project\Python_Test_Projects\Images_GUI\dev.jpg")
        # dev_img_btn=dev_img_btn.resize((280,180),Image.ANTIALIAS)
        # self.dev_img1=ImageTk.PhotoImage(dev_img_btn)

        # dev_b1 = Button(bg_img,command=self.developr,image=self.dev_img1,cursor="hand2",)
        # dev_b1.place(x=100,y=370,width=280,height=180)

        # dev_b1_1 = Button(bg_img,command=self.developr,text="Developers",cursor="hand2",font=("Monotype",15,"bold"),bg="lightblue",fg="black")
        # dev_b1_1.place(x=100,y=510,width=280,height=45)
        
        # exit_resize=(250,50)
        # exitImage1 = Image.open(r"E:\Final_yar_project\Python_Test_Projects\Resources\Exitgreen.png")
        # exitImage1 = exitImage1.resize(exit_resize, resample=Image.LANCZOS)
        # exitImage1 = ImageTk.PhotoImage(exitImage1)
        
        
        # exitImage2= Image.open(r"E:\Final_yar_project\Python_Test_Projects\Resources\Exitblue.png")
        # exitImage2 = exitImage2.resize((270,70), resample=Image.LANCZOS)
        # exitImage2 = ImageTk.PhotoImage(exitImage2)
        #================================Developer button======================================================
        def on_enter(e):
            dev_b1_1.configure(image=self.dev_img2)
        def on_leave(e):
            dev_b1_1.configure(image=self.dev_img1) 
            
        dev_img_btn=Image.open(r"E:\Final_yar_project\Python_Test_Projects\Images_GUI\developer_light.png")
        dev_img_btn=dev_img_btn.resize((300,70),Image.ANTIALIAS)
        self.dev_img1=ImageTk.PhotoImage(dev_img_btn)
        
        dev_img_btn1=Image.open(r"E:\Final_yar_project\Python_Test_Projects\Images_GUI\developer_red.png")
        dev_img_btn1=dev_img_btn1.resize((300,70),Image.ANTIALIAS)
        self.dev_img2=ImageTk.PhotoImage(dev_img_btn1)
        
        dev_b1_1 = Button(text="Developers", cursor="hand2",borderwidth=0,image=self.dev_img1 ,font=("Monotype", 15, "bold"), bg="lightblue", fg="black", command=self.developr)
        dev_b1_1.place(x=110, y=490, width=300, height=60)
            
        dev_b1_1.bind("<Enter>",on_enter)
        dev_b1_1.bind("<Leave>",on_leave)

        

        # # exit   button 8  940-370;940-510
       

        # exi_b1 = Button(bg_img,command=self.Close,image=self.exi_img1,cursor="hand2",)
        # exi_b1.place(x=940,y=370,width=280,height=180)
#====================================LIVE CHAT====================================================
        def on_enter(e):
            exi_b1_1.configure(image=self.exi_img1)
        def on_leave(e):
            exi_b1_1.configure(image=self.exi_img2) 
            
        exi_img_btn=Image.open(r"E:\Final_yar_project\Python_Test_Projects\Images_GUI\livechat_pink.png")
        exi_img_btn=exi_img_btn.resize((300,70),Image.ANTIALIAS)
        self.exi_img1=ImageTk.PhotoImage(exi_img_btn)
        
        exi_img_btn1=Image.open(r"E:\Final_yar_project\Python_Test_Projects\Images_GUI\livechat_green.png")
        exi_img_btn1=exi_img_btn1.resize((300,70),Image.ANTIALIAS)
        self.exi_img2=ImageTk.PhotoImage(exi_img_btn1)
        
        exi_b1_1 = Button(bg_img,command=self.chat,image=self.exi_img2,borderwidth=0,text="CHAT ME",cursor="hand2",font=("Monotype",15,"bold"),bg="lightblue",fg="black")
        exi_b1_1.place(x=110,y=360,width=300,height=60)
        
        exi_b1_1.bind("<Enter>",on_enter)
        exi_b1_1.bind("<Leave>",on_leave)

#=======================================EXIT BUTTON=============================================================
        exit_resize=(250,50)
        exitImage1 = Image.open(r"E:\Final_yar_project\Python_Test_Projects\Images_GUI\Exitgreen.png")
        exitImage1 = exitImage1.resize(exit_resize, resample=Image.LANCZOS)
        exitImage1 = ImageTk.PhotoImage(exitImage1)
        
        
        exitImage2= Image.open(r"E:\Final_yar_project\Python_Test_Projects\Images_GUI\Exitblue.png")
        exitImage2 = exitImage2.resize((270,70), resample=Image.LANCZOS)
        exitImage2 = ImageTk.PhotoImage(exitImage2)

        # def butt(text, bgcolor, fgcolor,cmd):
        def butt(cmd):

            def on_enter(e):
                mybutton.configure(image=exitImage1)
                

            def on_leave(e):
                mybutton.configure(image=exitImage2)
                


            mybutton=Button(bg_img,borderwidth=0, 
                   
                    command=cmd,
                    image=exitImage2)
    
            mybutton.bind("<Enter>",on_enter)
            mybutton.bind("<Leave>",on_leave)
    
            mybutton.place(x=130,y=590,width=220,height=45)
        
        butt(self.Close)   

      
# ==================Funtion for Open Images Folder==================
    def open_img(self):
        os.startfile("dataset")

    def Close(self):
        self.Close = tkinter.messagebox.askyesno(
            "Face Recognition", "Are you sure You want to exit", parent=self.root)
        if self.Close > 0:
            self.root.destroy()
        else:
            return
# ==================Functions Buttons=====================

    def main_pannels(self):
        # from login import Login  # import here instead of at the top
        # login = Login()
        self.new_window = Toplevel(self.root)
        self.app = Login(self.new_window)
       

    def train_pannels(self):
        self.new_window = Toplevel(self.root)
        self.app = Train(self.new_window)

    def face_rec(self):
        self.new_window = Toplevel(self.root)
        self.app = Face_Recognition(self.new_window)

    def attendance_pannel(self):
        self.new_window = Toplevel(self.root)
        self.app = Attendance(self.new_window)

    def developr(self):
        self.new_window = Toplevel(self.root)
        self.app = Developer(self.new_window)

    def helpSupport(self):
        self.new_window = Toplevel(self.root)
        self.app = Helpsupport(self.new_window)

    def student_pannels(self):
        self.new_window = Toplevel(self.root)
        self.app = Student(self.new_window)

    def chat(self):
        self.new_window=Toplevel(self.root)
        self.app= chat(self.new_window)
        
    def request(self):
        self.new_window=Toplevel(self.root)
        self.app=Request(self.new_window)
            
        
if __name__ == "__main__":
    root = Tk()
    obj = Frontview(root)
    root.mainloop()
