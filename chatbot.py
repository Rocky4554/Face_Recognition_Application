from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk

class chat:

    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Welcome to ChatBot")
        self.root.bind('<Return>',self.enter_func)   
        
        main_frame=Frame(self.root,bd=4,bg="powder blue",width=610)
        main_frame.pack()
        
        img_chat=Image.open(r"E:\Final_yar_project\Python_Test_Projects\Images_GUI\chatfront.jpg")
        img_chat=img_chat.resize((200,70),Image.LANCZOS)
        self.photoimage=ImageTk.PhotoImage(img_chat)
        
        Title_label=Label(main_frame,bd=3,relief=RAISED,anchor="nw",width=800,compound=LEFT,image=self.photoimage,text="CHAT ME",font=('arial',30,'bold'),fg="white",bg="green") 
        Title_label.pack(side=TOP)
        
        self.scroll_y=ttk.Scrollbar(main_frame,orient=VERTICAL)
        self.text=Text(main_frame,width=65,height=20,bd=20,relief=RAISED,font=("ariel",14),yscrollcommand=self.scroll_y.set)
        self.scroll_y.pack(side=RIGHT,fill=Y)
        self.text.pack()
        
        btn_frame=Frame(self.root,bd=4,bg="white",width=730)
        btn_frame.pack()

        label=Label(btn_frame,text="TYPE HERE",font=("ariel",14,"bold"),fg="green",bg="white")
        label.grid(row=0,column=0,padx=5,sticky=W)
        
        self.entry=StringVar()
        self.entry1=ttk.Entry(btn_frame,textvariable=self.entry,width=40,font=("times new roman",20,"bold"))
        self.entry1.grid(row=0,column=1,padx=5,sticky=W)

        self.send=Button(btn_frame,text="SEND>>",command=self.send,font=("ariel",15,"bold"),width=8,bg="orange")
        self.send.grid(row=0,column=2,pady=5,sticky=W)
        
        self.clear=Button(btn_frame,text="CLEAR",command=self.clear_func,font=("ariel",15,"bold"),width=8,bg="blue")
        self.clear.grid(row=1,column=0,pady=5,stick=W)
        
        self.msg=''
        self.label_l=Label(btn_frame,text=self.msg,font=("ariel",14,"bold"),fg="red",bg="white")
        self.label_l.grid(row=1,column=1,padx=5,sticky=W)
    
        
        #================================Function DEclaration==============================/=
    def enter_func(self,e):
        self.send.invoke()
        self.entry.set('')
        
    def clear_func(self):
        self.text.delete('1.0',END)
        self.entry.set('')
    
           
    def send(self):
        send='\t\t\t'+'User: '+self.entry.get()
        self.text.insert(END,'\n'+ send)
        self.text.yview(END)
        if(self.entry.get()==''):
            self.msg='Please enter some input'
            self.label_l.config(text=self.msg,fg="red")
            
        else:
            self.msg=''
            self.label_l.config(text=self.msg,fg="red")
                
        if(self.entry.get()=="Hello"):
            self.text.insert(END,'\n\n'+ 'Bot: Hii Welcome to Face Auto Face Recognizer(Create by RAUNAK and MUSKAN)')
        elif(self.entry.get()=="who created you"):
            self.text.insert(END,'\n\n'+ 'Bot: I was created bt my developers RAUNAK and MUSKAN')
        elif(self.entry.get()=="my face is not Identified"):
            self.text.insert(END,'\n\n'+ 'Bot: Please Contact Admin to register yourself')
        elif(self.entry.get()=="How were you created"):
            self.text.insert(END,'\n\n'+ 'Bot: I was created using PYTHON ,TKINTER and MYSQL database')
        elif(self.entry.get()=="how are you"):
            self.text.insert(END,'\n\n'+ 'Bot: Fine and hope you are also doing great')
        elif(self.entry.get()=="bye"):
            self.text.insert(END,'\n\n'+ 'Bot: OK !Hope your problem was solved')
        elif(self.entry.get()=="how to register"):
            self.text.insert(END,'\n\n'+ 'Bot: Contact Admin to register.\n You will be registerd in a day')
           
        else:
            self.text.insert(END,"\n\n"+'Bot: Sorry i did not get what you are trying to say')  
                   
                  
        
        
if __name__ == "__main__":
    root = Tk()
    obj = chat(root)
    root.mainloop()