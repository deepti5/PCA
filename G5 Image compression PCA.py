
# coding: utf-8

# In[6]:


import sys
from sklearn.decomposition import RandomizedPCA
from sklearn.decomposition import PCA as RandomizedPCA
import matplotlib.image as mpimg
import numpy as np
import matplotlib.pyplot as plt
import cv2
from tkinter import *
import tkinter as tk
from tkinter import simpledialog, messagebox
from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog
import os

root = Tk()
text = Text(root)

root.title('PCA Implementation')
root.geometry("1600x900")
root.resizable(width=True, height=True)
root.configure(background='light blue')


Label(root, text = "   ",bg='light blue').grid(row=1)
Label(root, text=" PCA Algorithm!",bg="#FF3366",fg="white", relief="solid", font="Times 20 bold", padx=20, pady=10).grid(row=10 ,column=7 )


def open_img():
    x = filedialog.askopenfilenames(
    	parent=root,
    	initialdir='/',
    	initialfile='tmp',
    	filetypes=[
    		("All files", "*")])
    
    img = Image.open(x[0])
    img = img.resize((250, 250), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img)
    panel = tk.Label(root, image=img)
    panel.image = img
    panel.grid(row=70, column=1)
            
    image = cv2.imread(x[0])
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    cv2.imwrite("grey.jpeg", gray)
    gray.shape
    img = mpimg.imread("grey.jpeg")

    f=compo()
    ipca = RandomizedPCA(f)
    ipca.fit(img)
    img_c = ipca.transform(img)
    print(img_c.shape)
    temp = ipca.inverse_transform(img_c)
    
    print(temp.shape)
    cv2.imwrite("pca1.jpg", temp)
    print(np.sum(ipca.explained_variance_ratio_))
    plt.plot(np.cumsum(ipca.explained_variance_ratio_))
    plt.xlabel('number of components')
    plt.ylabel('cumulative explained variance');
    plt.savefig("graph.jpg")

#Graph function#

def grp():
    img = Image.open("graph.jpg")
    img = img.resize((250, 250), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img)
    panel = Label(root, image=img)
    panel.image = img
    panel.grid(row=70 ,column=50)
    
def displayimg():
    img = Image.open("pca1.jpg")
    img = img.resize((250, 250), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img)
    panel = Label(root, image=img)
    panel.image = img
    panel.grid(row=70 ,column=7)
    
def compo():
    a=int(entry.get())
    print(a)
    return(a)
###############################################################################################################
Label(root, text = "   ",bg='light blue').grid(row=40, column=3)


Label(root, text = "   ",bg='light blue').grid(row=42, column=3)

Label(root, text = "                   ",bg='light blue').grid(row=70, column=6)
Label(root, text = "           ",bg='light blue').grid( row=70, column=0)
Label(root, text = "               ",bg='light blue').grid( row=70, column=8)
Label(root, text = "               ",bg='light blue').grid( row=38, column=8)
Label(root, text = "               ",bg='light blue').grid( row=38, column=1)
Label(root, text = "               ",bg='light blue').grid( row=40, column=1)
Label(root, text = "               ",bg='light blue').grid( row=41, column=1)
Label(root, text = "               ",bg='light blue').grid( row=39, column=8)
Label(root, text = "               ",bg='light blue').grid( row=70, column=49)
Label(root, text = "                       ",bg='light blue').grid( row=70, column=48)
Label(root, text = "       ",bg='light blue').grid( row=46, column=1)
Label(root, text = "            ",bg='light blue').grid( row=47, column=48)
Label(root, text="Enter Number of components: ", font="Times 15 bold", bg='light blue').grid(row=40, column=1, pady=5)
entry = Entry(root, width=20, font="Times 15 bold")
entry.grid(row=40, column=2)

btn = Button(root, text='Open Image', command = open_img, font="Times 15 bold").grid(row= 45, column=1, pady=4)
B = Button(root, text ="Apply PCA & Display Image", command = displayimg, font="Times 15 bold").grid(row= 45, column=7, pady=4)

frame1 = tk.Frame(root, highlightbackground="green", highlightcolor="green", highlightthickness=1, width=250, height=250, bd= 0).grid(row=70, column=7)
frame2 = tk.Frame(root, highlightbackground="green", highlightcolor="green", highlightthickness=1, width=250, height=250, bd= 0).grid(row=70, column=50)
frame3 = tk.Frame(root, highlightbackground="green", highlightcolor="green", highlightthickness=1, width=250, height=250, bd= 0).grid(row=70, column=1)

b1=Button(root, text ="Display graph", command = grp, font="Times 15 bold").grid(row= 45, column=50, pady=4)
root.mainloop()

