import tkinter as tk 
from tkinter import ttk

HONEYDEW = '#f0fff0'

class App():
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry('700x400')
        self.root.title('EOS Coefficient Predictor')
        self.mainframe = tk.Frame(self.root, background='#B00B13')
        self.mainframe.pack(fill='both', expand=True)

        self.text = ttk.Label(self.mainframe, text='Hello World', background='#B00B13', font=("Times New Roman", 30))
        self.text.grid(row=0, column=0)

        self.set_text_field = ttk.Entry(self.mainframe)
        self.set_text_field.grid(row=1, column=0, pady=10, sticky='NWES')
        set_text_button = ttk.Button(self.mainframe, text='Set Text', command=self.set_text)
        set_text_button.grid(row=1, column=1, pady=10)

        color_options = ['red', 'blue', 'green', 'black', 'honeydew']
        self.set_color_field = ttk.Combobox(self.mainframe, values=color_options)
        self.set_color_field.grid(row=2, column=0, sticky='NWES', pady=0)
        set_color_button = ttk.Button(self.mainframe, text='Set Color', command=self.set_color)
        set_color_button.grid(row=2, column=1, pady=0)
        self.root.mainloop()
        return
    
    def set_text(self):
        newtext = self.set_text_field.get()
        self.text.config(text=newtext)

    def set_color(self):
        newcolor = self.set_color_field.get()
        self.text.config(foreground=newcolor)
if __name__ == '__main__':
    App()