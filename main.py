from tkinter import*
from tkinter import ttk
from train import Train
from PIL import Image,ImageTk
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

class Face_Recognition_System:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face_Recogonition_System")

# This part is image labels setting start 
        # first header image  E:\Final_yar_project\Python_Test_Projects\Images_GUI
        img=Image.open(r"E:\Final_yar_project\Python_Test_Projects\Images_GUI\bg3.jpg")
        img=img.resize((1766,130),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        # set image as lable
        f_lb1 = Label(self.root,image=self.photoimg)
        f_lb1.place(x=0,y=0,width=1766,height=130)

        # #header title section
        # title_lb = Label(f_lb1,text="Welcome",font=("verdana",30,"bold"),bg="black",fg="white")
        # title_lb.place(x=0,y=0,width=266,height=45)

        # backgorund image 
        bg1=Image.open(r"E:\Final_yar_project\Python_Test_Projects\Images_GUI\college.jpg")
        bg1=bg1.resize((1546,710),Image.ANTIALIAS)
        self.photobg1=ImageTk.PhotoImage(bg1)

        #set image as lable
        bg_img = Label(self.root,image=self.photobg1)
        bg_img.place(x=0,y=130,width=1546,height=710)


        #banner title section
        title_lb1 = Label(bg_img,text="Identify People In Institution Using Facial Recognition",font=("verdana",30,"bold"),bg="orange",fg="black")
        title_lb1.place(x=0,y=0,width=1550,height=45)

        #TIME
        def time():
            string = strftime('%H:%M:%S %p')
            lbl.config(text=string)
            lbl.after(1000,time)

        lbl=Label(title_lb1,font=('times new roman',14,'bold'),background='orange',foreground='blue')
        lbl.place(x=0,y=(-15),width=110,height=50)
        time()

        # Create buttons below the section 
        # ------------------------------------------------------------------------------------------------------------------- 
        # student button 1
        std_img_btn=Image.open(r"E:\Final_yar_project\Python_Test_Projects\Images_GUI\i8.jfif")
        std_img_btn=std_img_btn.resize((280,180),Image.ANTIALIAS) 
        self.std_img1=ImageTk.PhotoImage(std_img_btn)

        std_b1 = Button(bg_img,command=self.student_pannels,image=self.std_img1,cursor="hand2")
        std_b1.place(x=250,y=100,width=280,height=180)

        std_b1_1 = Button(bg_img,command=self.student_pannels,text="Student Pannel",cursor="hand2",font=("Monotype",15,"bold"),bg="lightblue",fg="black")
        std_b1_1.place(x=250,y=280,width=280,height=45)

        # Detect Face  button 2
        det_img_btn=Image.open(r"E:\Final_yar_project\Python_Test_Projects\Images_GUI\i7.jfif")
        det_img_btn=det_img_btn.resize((280,180),Image.ANTIALIAS)
        self.det_img1=ImageTk.PhotoImage(det_img_btn)

        det_b1 = Button(bg_img,command=self.face_rec,image=self.det_img1,cursor="hand2",)
        det_b1.place(x=580,y=100,width=280,height=180)

        det_b1_1 = Button(bg_img,command=self.face_rec,text="Face Detector",cursor="hand2",font=("Monotype",15,"bold"),bg="lightblue",fg="black")
        det_b1_1.place(x=580,y=280,width=280,height=45)

        #  # Attendance System  button 3
        # att_img_btn=Image.open(r"E:\Final_yar_project\Python_Test_Projects\Images_GUI\i12.jfif")
        # att_img_btn=att_img_btn.resize((180,180),Image.ANTIALIAS)
        # self.att_img1=ImageTk.PhotoImage(att_img_btn)

        # att_b1 = Button(bg_img,command=self.attendance_pannel,image=self.att_img1,cursor="hand2",)
        # att_b1.place(x=710,y=100,width=180,height=180)

        # att_b1_1 = Button(bg_img,command=self.attendance_pannel,text="Attendance",cursor="hand2",font=("Monotype",15,"bold"),bg="lightblue",fg="black")
        # att_b1_1.place(x=710,y=280,width=180,height=45)

         # Help  Support  button 4
        hlp_img_btn=Image.open(r"E:\Final_yar_project\Python_Test_Projects\Images_GUI\i15.jfif")
        hlp_img_btn=hlp_img_btn.resize((280,180),Image.ANTIALIAS)
        self.hlp_img1=ImageTk.PhotoImage(hlp_img_btn)

        hlp_b1 = Button(bg_img,command=self.helpSupport,image=self.hlp_img1,cursor="hand2")
        hlp_b1.place(x=940,y=100,width=280,height=180)

        hlp_b1_1 = Button(bg_img,command=self.helpSupport,text="Help Support",cursor="hand2",font=("Monotype",15,"bold"),bg="lightblue",fg="black")
        hlp_b1_1.place(x=940,y=280,width=280,height=45)

        # Top 4 buttons end.......
        # ---------------------------------------------------------------------------------------------------------------------------
        # Start below buttons.........
         # Train   button 5
        tra_img_btn=Image.open(r"E:\Final_yar_project\Python_Test_Projects\Images_GUI\i14.jfif")
        tra_img_btn=tra_img_btn.resize((280,180),Image.ANTIALIAS)
        self.tra_img1=ImageTk.PhotoImage(tra_img_btn)

        tra_b1 = Button(bg_img,command=self.train_pannels,image=self.tra_img1,cursor="hand2",)
        tra_b1.place(x=250,y=370,width=280,height=180)

        tra_b1_1 = Button(bg_img,command=self.train_pannels,text="Data Train",cursor="hand2",font=("Monotype",15,"bold"),bg="lightblue",fg="black")
        tra_b1_1.place(x=250,y=510,width=280,height=45)

        # # Photo   button 6
        # pho_img_btn=Image.open(r"E:\Final_yar_project\Python_Test_Projects\Images_GUI\qr1.png")
        # pho_img_btn=pho_img_btn.resize((180,180),Image.ANTIALIAS)
        # self.pho_img1=ImageTk.PhotoImage(pho_img_btn)

        # pho_b1 = Button(bg_img,command=self.open_img,image=self.pho_img1,cursor="hand2",)
        # pho_b1.place(x=480,y=370,width=180,height=180)

        # pho_b1_1 = Button(bg_img,command=self.open_img,text="QR-Codes",cursor="hand2",font=("Monotype",15,"bold"),bg="lightblue",fg="black")
        # pho_b1_1.place(x=480,y=510,width=180,height=45)

        # Developers   button 7  710-370  ; 710-510
        dev_img_btn=Image.open(r"E:\Final_yar_project\Python_Test_Projects\Images_GUI\dev.jpg")
        dev_img_btn=dev_img_btn.resize((280,180),Image.ANTIALIAS)
        self.dev_img1=ImageTk.PhotoImage(dev_img_btn)

        dev_b1 = Button(bg_img,command=self.developr,image=self.dev_img1,cursor="hand2",)
        dev_b1.place(x=580,y=370,width=280,height=180)

        dev_b1_1 = Button(bg_img,command=self.developr,text="Developers",cursor="hand2",font=("Monotype",15,"bold"),bg="lightblue",fg="black")
        dev_b1_1.place(x=580,y=510,width=280,height=45)

        # exit   button 8  940-370;940-510
        exi_img_btn=Image.open(r"E:\Final_yar_project\Python_Test_Projects\Images_GUI\i16.jfif")
        exi_img_btn=exi_img_btn.resize((280,180),Image.ANTIALIAS)
        self.exi_img1=ImageTk.PhotoImage(exi_img_btn)

        exi_b1 = Button(bg_img,command=self.Close,image=self.exi_img1,cursor="hand2",)
        exi_b1.place(x=940,y=370,width=280,height=180)

        exi_b1_1 = Button(bg_img,command=self.Close,text="Exit",cursor="hand2",font=("Monotype",15,"bold"),bg="lightblue",fg="black")
        exi_b1_1.place(x=940,y=510,width=280,height=45)

# ==================Funtion for Open Images Folder==================
    def open_img(self):
        os.startfile("dataset")

    def Close(self):
        self.Close=tkinter.messagebox.askyesno("Face Recognition", "Are you sure You want to exit", parent=self.root)
        if self.Close > 0:
            self.root.destroy()
        else:
            return
# ==================Functions Buttons=====================
    def student_pannels(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)

    def train_pannels(self):
        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window)
    
    def face_rec(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_Recognition(self.new_window)
    
    def attendance_pannel(self):
        self.new_window=Toplevel(self.root)
        self.app=Attendance(self.new_window)
    
    def developr(self):
        self.new_window=Toplevel(self.root)
        self.app=Developer(self.new_window)
    
    def helpSupport(self):
        self.new_window=Toplevel(self.root)
        self.app=Helpsupport(self.new_window)

    # def Close(self):
    #     root.destroy()

    
        
    
    





if __name__ == "__main__":
    root=Tk()
    obj=Face_Recognition_System(root)
    root.mainloop()
