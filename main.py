from tkinter import *
import tkinter as tk
from tkinter import filedialog
from tkinter.filedialog import askopenfile
from PIL import Image, ImageTk
import subprocess

root = Tk()
root.wm_attributes('-transparentcolor', 'grey')
root.overrideredirect(1)
root.geometry('445x77+380+0')

def change_path():
    f_types = [('App', '*.exe')]
    filename = filedialog.askopenfilename(filetypes=f_types)
    def open_spotify():
        subprocess.run([filename])
    spotify_label.configure(command=open_spotify)

def change_path_chrome():
    f_types = [('App', '*.exe')]
    filename = filedialog.askopenfilename(filetypes=f_types)
    def open_chrome():
        subprocess.run([filename])
    chrome_label.configure(command=open_chrome)

def change_path_edge():
    f_types = [('App', '*.exe')]
    filename = filedialog.askopenfilename(filetypes=f_types)
    def open_edge():
        subprocess.run([filename])
    edge_label.configure(command=open_edge)
    
def change_path_photoshop():
    f_types = [('App', '*.exe')]
    filename = filedialog.askopenfilename(filetypes=f_types)
    def open_photoshop():
        subprocess.run([filename])
    photoshop_label.configure(command=open_photoshop)

def change_path_offic():
    f_types = [('App', '*.exe')]
    filename = filedialog.askopenfilename(filetypes=f_types)
    def open_offic():
        subprocess.run([filename])
    offic_label.configure(command=open_offic)

def move_app(e):
    root.geometry(f'+{e.x_root}+{e.y_root}')
frame_photo = PhotoImage(file='menu.png')
frame_label = Label(root,border=0,bg='grey',image=frame_photo)
frame_label.bind('<B1-Motion>',move_app)
frame_label.pack()

m = Menu(root, tearoff = 0)
m.add_command(label ="Exit",command=root.quit)

def do_popup(event):
	try:
		m.tk_popup(event.x_root, event.y_root)
	finally:
		m.grab_release()

frame_label.bind("<Button-3>", do_popup)


spotify = PhotoImage(file='spotify.png')
spotify_label = tk.Button(root,image=spotify,border=0,bg='#00E0FF',activebackground='#00E0FF')
spotify_label.place(x=30,y=6)

chrome = PhotoImage(file='chrome.png')
chrome_label = Button(root,image=chrome,border=0,bg='#00E0FF',activebackground='#00E0FF')
chrome_label.place(x=110,y=6)

edge = PhotoImage(file='edge.png')
edge_label = Button(root,image=edge,border=0,bg='#00E0FF',activebackground='#00E0FF')
edge_label.place(x=185,y=6)

photoshop = PhotoImage(file='photoshop.png')
photoshop_label = Button(root,image=photoshop,border=0,bg='#00E0FF',activebackground='#00E0FF')
photoshop_label.place(x=260,y=6)

offic = PhotoImage(file='offic.png')
offic_label = Button(root,image=offic,border=0,bg='#00E0FF',activebackground='#00E0FF')
offic_label.place(x=340,y=6)

def change_icon():
    global img
    f_types = [('Png Files', '*.Png')]
    filename = filedialog.askopenfilename(filetypes=f_types)
    img=Image.open(filename)
    img_resized=img.resize((65,65)) # new width & height
    img=ImageTk.PhotoImage(img_resized)
    spotify_label.configure(image=img)

S = Menu(root, tearoff = 0)
S.add_command(label ="Change Icon",command=change_icon)
S.add_command(label ="Change App",command=change_path)


def do_popup(event):
	try:
		S.tk_popup(event.x_root, event.y_root)
	finally:
		S.grab_release()

spotify_label.bind("<Button-3>", do_popup)

#2
def change_icon_chrome():
    global chrome_icon
    f_types = [('Png Files', '*.Png')]
    filename = filedialog.askopenfilename(filetypes=f_types)
    chrome_icon=Image.open(filename)
    img_resized=chrome_icon.resize((65,65)) # new width & height
    chrome_icon=ImageTk.PhotoImage(img_resized)
    chrome_label.configure(image=chrome_icon)

c = Menu(root, tearoff = 0)
c.add_command(label ="Change Icon",command=change_icon_chrome)
c.add_command(label ="Change App",command=change_path_chrome)

def do_popup_1(event):
	try:
		c.tk_popup(event.x_root, event.y_root)
	finally:
		c.grab_release()

chrome_label.bind("<Button-3>", do_popup_1)


#3
def change_icon_photo():
    global photshop_icon
    f_types = [('Png Files', '*.Png')]
    filename = filedialog.askopenfilename(filetypes=f_types)
    photshop_icon=Image.open(filename)
    img_resized=photshop_icon.resize((65,65)) # new width & height
    photshop_icon=ImageTk.PhotoImage(img_resized)
    photoshop_label.configure(image=photshop_icon)

p = Menu(root, tearoff = 0)
p.add_command(label ="Change Icon",command=change_icon_photo)
p.add_command(label ="Change App",command=change_path_photoshop)

def do_popup_1(event):
	try:
		p.tk_popup(event.x_root, event.y_root)
	finally:
		p.grab_release()

photoshop_label.bind("<Button-3>", do_popup_1)

#4
def change_icon_edge():
    global edge_icon
    f_types = [('Png Files', '*.Png')]
    filename = filedialog.askopenfilename(filetypes=f_types)
    edge_icon=Image.open(filename)
    img_resized=edge_icon.resize((65,65)) # new width & height
    edge_icon=ImageTk.PhotoImage(img_resized)
    edge_label.configure(image=edge_icon)

e = Menu(root, tearoff = 0)
e.add_command(label ="Change Icon",command=change_icon_edge)
e.add_command(label ="Change App",command=change_path_edge)

def do_popup_1(event):
	try:
		e.tk_popup(event.x_root, event.y_root)
	finally:
		e.grab_release()

edge_label.bind("<Button-3>", do_popup_1)

#5
def change_icon_offic():
    global offic_icon
    f_types = [('Png Files', '*.Png')]
    filename = filedialog.askopenfilename(filetypes=f_types)
    offic_icon=Image.open(filename)
    img_resized=offic_icon.resize((65,65)) # new width & height
    offic_icon=ImageTk.PhotoImage(img_resized)
    offic_label.configure(image=offic_icon)

f = Menu(root, tearoff = 0)
f.add_command(label ="Change Icon",command=change_icon_offic)
f.add_command(label ="Change App",command=change_path_offic)

def do_popup_1(event):
	try:
		f.tk_popup(event.x_root, event.y_root)
	finally:
		f.grab_release()

offic_label.bind("<Button-3>", do_popup_1)

root.mainloop()
