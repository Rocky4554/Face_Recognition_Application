import tkinter as tk

class Button(tk.Button):
    def __init__(self, parent, text):
        tk.Button.__init__(self, parent, text=text, font=("verdana", 25, "bold"), bg="orange", fg="black")
        self.slider()
        
    def slider(self):
        index = 0
        text = self['text']
        def update_text():
            nonlocal index, text
            if index >= len(text):
                index = -1
                text = ''
                self.configure(text=text)
            else:
                text = text[:index] + text[index].upper() + text[index+1:]
                self.configure(text=text)
                index += 1
            self.after(100, update_text)
        update_text()
