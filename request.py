
from tkinter import* 
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import os
from chatbot import chat


class Request:
    def __init__(self,root):
        self.root=root
        self.root.title("Reguest")
        self.root.geometry("1366x768+0+0")

        # ============ Variables =================
        self.var_fname=StringVar()
        self.var_student_id=StringVar()
        self.var_dept=StringVar()
        self.var_sess=StringVar()
        self.var_issue=StringVar()
        self.var_prob=StringVar()
        self.var_email=StringVar()
        self.var_phone=StringVar()
        # self.var_check=IntVar()

        self.bg=ImageTk.PhotoImage(file=r"E:\Final_yar_project\Python_Test_Projects\Images_GUI\bgReg.jpg")
        
        lb1_bg=Label(self.root,image=self.bg)
        lb1_bg.place(x=0,y=0, relwidth=1,relheight=1)

        frame= Frame(self.root,bg="#F2F2F2")
        frame.place(x=100,y=80,width=900,height=580)
        

        # img1=Image.open(r"E:\Final_yar_project\Python_Test_Projects\Images_GUI\reg1.png")
        # img1=img1.resize((450,100),Image.ANTIALIAS)
        # self.photoimage1=ImageTk.PhotoImage(img1)
        # lb1img1 = Label(image=self.photoimage1,bg="#F2F2F2")
        # lb1img1.place(x=300,y=100, width=500,height=100)
        

        get_str = Label(frame,text="User Request Page",font=("times new roman",30,"bold"),fg="#002B53",bg="#F2F2F2")
        get_str.place(x=350,y=130)

        #label1 
        fname =lb1= Label(frame,text="Student Name:",font=("times new roman",15,"bold"),fg="#002B53",bg="#F2F2F2")
        fname.place(x=100,y=200)

        #entry1 
        self.txtuser=ttk.Entry(frame,textvariable=self.var_fname,font=("times new roman",15,"bold"))
        self.txtuser.place(x=103,y=225,width=270)


        #label2 
        lname =lb1= Label(frame,text="Student ID",font=("times new roman",15,"bold"),fg="#002B53",bg="#F2F2F2")
        lname.place(x=100,y=270)

        #entry2 
        self.txtpwd=ttk.Entry(frame,textvariable=self.var_student_id,font=("times new roman",15,"bold"))
        self.txtpwd.place(x=103,y=295,width=270)

        # ==================== section 2 -------- 2nd Columan===================

        #label1 
        cnum =lb1= Label(frame,text="Department",font=("times new roman",15,"bold"),fg="#002B53",bg="#F2F2F2")
        cnum.place(x=530,y=200)

        #entry1 
        self.txtuser=ttk.Entry(frame,textvariable=self.var_dept,font=("times new roman",15,"bold"))
        self.txtuser.place(x=533,y=225,width=270)


        #label2 
        email =lb1= Label(frame,text="Session",font=("times new roman",15,"bold"),fg="#002B53",bg="#F2F2F2")
        email.place(x=530,y=270)

        #entry2 
        self.txtpwd=ttk.Entry(frame,textvariable=self.var_sess,font=("times new roman",15,"bold"))
        self.txtpwd.place(x=533,y=295,width=270)

        # ========================= Section 3 --- 1 Columan=================

        #label1 
        ssq =lb1= Label(frame,text="Problem Type",font=("times new roman",15,"bold"),fg="#002B53",bg="#F2F2F2")
        ssq.place(x=100,y=350)

        #Combo Box1
        self.combo_security = ttk.Combobox(frame,textvariable=self.var_issue,font=("times new roman",15,"bold"),state="readonly")
        self.combo_security["values"]=("Select","Request for Registration","Having trouble in registration","Having trouble in face detection")
        self.combo_security.current(0)
        self.combo_security.place(x=103,y=375,width=270)


        #label2 
        sa =lb1= Label(frame,text="Problem Description:",font=("times new roman",15,"bold"),fg="#002B53",bg="#F2F2F2")
        sa.place(x=100,y=420)

        #entry2 
        self.txtpwd=ttk.Entry(frame,textvariable=self.var_prob,font=("times new roman",15,"bold"))
        self.txtpwd.place(x=103,y=445,width=300)

        # ========================= Section 4-----Column 2=============================

        #label1 
        pwd =lb1= Label(frame,text="Email:",font=("times new roman",15,"bold"),fg="#002B53",bg="#F2F2F2")
        pwd.place(x=530,y=350)

        #entry1 
        self.txtuser=ttk.Entry(frame,textvariable=self.var_email,font=("times new roman",15,"bold"))
        self.txtuser.place(x=533,y=375,width=270)


        #label2 
        cpwd =lb1= Label(frame,text="Phone No:",font=("times new roman",15,"bold"),fg="#002B53",bg="#F2F2F2")
        cpwd.place(x=530,y=420)

        #entry2 
        self.txtpwd=ttk.Entry(frame,textvariable=self.var_phone,font=("times new roman",15,"bold"))
        self.txtpwd.place(x=533,y=445,width=270)

        # # Checkbutton
        # checkbtn = Checkbutton(frame,variable=self.var_check,text="I Agree the Terms & Conditions",font=("times new roman",13,"bold"),fg="#002B53",bg="#F2F2F2")
        # checkbtn.place(x=100,y=480,width=270)


        # Creating Button Register
        loginbtn=Button(frame,command=self.reg,text="Submit Request",font=("times new roman",15,"bold"),bd=0,relief=RIDGE,fg="#fff",bg="#002B53",activeforeground="white",activebackground="#007ACC")
        loginbtn.place(x=103,y=510,width=270,height=35)

        # Creating Button Login
        livechat=Button(frame,text="Live Chat",font=("times new roman",15,"bold"),bd=0,relief=RIDGE,fg="white",bg="ForestGreen",activeforeground="white",activebackground="#007ACC",command=self.chat)
        livechat.place(x=533,y=510,width=270,height=35)




    def reg(self):
        if (self.var_fname.get()=="" or self.var_dept.get()=="" or self.var_student_id.get()=="" or self.var_email.get()=="" or self.var_issue.get()=="Select" or self.var_sess.get()=="" or self.var_phone.get()=="" or self.var_prob.get()==""):
            messagebox.showerror("Error","All Field Required!",parent=self.root)
        # elif(self.var_pwd.get() != self.var_cpwd.get()):
        #     messagebox.showerror("Error","Please Enter Password & Confirm Password are Same!")
        # elif(self.var_check.get()==0):
        #     messagebox.showerror("Error","Please Check the Agree Terms and Conditons!")
        else:
            # messagebox.showinfo("Successfully","Successfully Register!")
            try:
                conn = mysql.connector.connect(username='root', password='SQLconnect@123',host='localhost',database='face_recognition',port=3306)
                mycursor = conn.cursor()
                query=("select * from request where email=%s")
                value=(self.var_email.get(),)
                mycursor.execute(query,value)
                row=mycursor.fetchone()
                if row!=None:
                    messagebox.showerror("Error","User already exist,please try another email")
                else:
                    mycursor.execute("insert into request values(%s,%s,%s,%s,%s,%s,%s,%s)",(
                    self.var_fname.get(),
                    self.var_student_id.get(),
                    self.var_dept.get(),
                    self.var_sess.get(),
                    self.var_issue.get(),
                    self.var_email.get(),
                    self.var_phone.get(),
                    self.var_prob.get()
                    ))

                    conn.commit()
                    conn.close()
                    messagebox.showinfo("Success","Request places succesfully!",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due to: {str(es)}",parent=self.root)

    def chat(self):
        self.new_window=Toplevel(self.root)
        self.app= chat(self.new_window)


if __name__ == "__main__":
    root=Tk()
    app=Request(root)
    root.mainloop()