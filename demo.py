from tkinter import *
root=Tk()
root.geometry("1366x768+0+0")

# bg1 = (r"E:\Final_yar_project\Python_Test_Projects\Resources\anti-spoofing-techniques-face-recognition-1920x1080.jpg")
# bg1 = bg1.resize((1546, 710), Image.LANCZOS)
# photobg1 = ImageTk.PhotoImage(bg1)

# # set image as lable
# bg_img = Label(root, image=photobg1)
# bg_img.place(x=0, y=10, width=1546, height=710)
root.configure(bg="#141414")

def butt(x,y,text,bgcolor,fgcolor):
    
    def on_enter(e):
        mybutton['background']=bgcolor
        mybutton['foreground']=fgcolor
    def on_leave(e):
        mybutton['background']=fgcolor
        mybutton['foreground']=bgcolor
        
        
    mybutton=Button(root,width=50,height=4,text=text,
                    fg=bgcolor,
                    bg=fgcolor,
                    activef=fgcolor,
                    activeb=bgcolor,
                    border=0)
    
    mybutton.bind("<Enter>",on_enter)
    mybutton.bind("<Leave>",on_leave)
    
    mybutton.place(x=x,y=y)
    
    
    

    
     
butt(0,0,"raunak",'#ffcc66','#141414')    
root.mainloop()



