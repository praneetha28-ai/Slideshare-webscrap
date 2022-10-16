from random import randint
from bs4 import BeautifulSoup
import requests
import urllib.request
from PIL import Image
import tkinter as tk
from tkinter import ttk
import os
import numpy as np
completed = False
win = tk.Tk()
win.geometry("500x500")
parent_dir = os.getcwd()
k = (randint(0,1000))
dir = "content {}".format(k)
path = os.path.join(parent_dir,dir)
os.mkdir(path)
k=(randint(0,1000))
def retrieveData(url):
    text = requests.get(url=url).text
    soup = BeautifulSoup(text,'lxml')
    slides = soup.find_all('img',class_="slide-image")
    i=0
    images = []
    for slide in slides:
        urllib.request.urlretrieve(slide['src'],(r"{}\slide{}.jpg").format(path,i))
        images.append(Image.open(r"{}\slide{}.jpg".format(path,i)))
        i+=1
    for i in images[1:]:
        i = i.convert('RGB')
    images[0].save(r'{}\slides.pdf'.format(path),save_all =True,append_images = images)  
def click():
    retrieveData(name.get())
name = tk.StringVar()
urlEntered  = ttk.Entry(win,width=15,textvariable=name).grid(column=10,row=5)
button = ttk.Button(win, text = "submit", command = click).grid(column = 10, row = 10)
win.title("Slideshre Downloader")
lbl = ttk.Label(win,text="Place url").grid(column=10,row=0)
win.mainloop()