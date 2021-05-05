import tkinter as tk
import os
from internet import internet
from gui import gui
import time

check = False


def bigLoop(internet, gui):
    global check
    if check == False:
        check = True
    else:
        check = False

    times = gui.getTimes(timesBox)
    link = gui.getLink(linkBox)
    mentions = gui.getMentions(mentionsBox)

    comments = []

    with open('comments.txt', 'r', newline='\n') as file:
        for line in file:
            if line.count("@") == int(mentions):
                comments.append(line)
                check = True
            else:
                pass

    # Failsafe for comments
    if len(comments) == 0:
        popupmsg(
            'There are no comments that meet the requirements. Please enter a different mentions number of add more comments')
        check = False

    with open('credentials.txt', 'r', newline='\n') as file:
        username = file.readline()
        password = file.readline()

    if check:
        internet.openBrowser(link, username, password)

    while check:
        internet.commenting(comments)
        time.sleep(times*60)

# Popup message


def popupmsg(msg):
    popup = tk.Tk()
    popup.wm_title("!")
    label = tk.Label(popup, text=msg)
    label.pack(side="top", fill="x", pady=10)
    B1 = tk.Button(popup, text="Okay", command=popup.destroy)
    B1.pack()
    popup.mainloop()


cwd = os.getcwd()

path = cwd+r"\chromedriver.exe"

# Defining the objects
internet = internet(path)
gui = gui(cwd)

root = tk.Tk()
canvas1 = tk.Canvas(root, width=600, height=700)
canvas1.pack()

# Dialog boxes

with open('credentials.txt', 'r', newline='\n') as file:
    userName = file.readline()
    passWord = file.readline()

# Checking whether they are full
if len(userName) > 1:
    pass
else:
    userName = 'Username...'

if len(passWord) > 1:
    pass
else:
    passWord = 'Password...'

userBox = tk.Entry(root)
userBox.place(
    x=150,
    y=60,
    width=300,
    height=30)
userBox.insert(0, userName)

passBox = tk.Entry(root)
passBox.place(
    x=150,
    y=100,
    width=300,
    height=30)
passBox.insert(0, (len(passWord)*('*')))

with open('link.txt', 'r', newline='\n') as file:
    for line in file:
        if len(line) < 1:
            link = 'Link...'
        else:
            link = line

linkBox = tk.Entry(root)
linkBox.place(
    x=150,
    y=140,
    width=300,
    height=30)
linkBox.insert(0, link)

timesBox = tk.Entry(root)
timesBox.place(
    x=150,
    y=190,
    width=100,
    height=30)
timesBox.insert(0, 'Minutes..')

mentionsBox = tk.Entry(root)
mentionsBox.place(
    x=300,
    y=190,
    width=100,
    height=30)
mentionsBox.insert(0, 'Mentions..')

commBox = tk.Entry(root)
commBox.place(
    x=150,
    y=240,
    width=300,
    height=200)
commBox.insert(0, 'Place your comment here!')

# Buttons
# Need to add the lambda command there to tell tkinter that it is an event but to not pass it in as an argument of the function
credButton = tk.Button(root, text='Credentials',
                       command=lambda: gui.getCred(userBox, passBox))
credButton.place(
    x=100,
    y=500,
    height=50,
    width=80,)

commButton = tk.Button(root, text='Add comment',
                       command=lambda: gui.getComments(commBox))
commButton.place(
    x=260,
    y=500,
    height=50,
    width=80,)

workButton = tk.Button(
    root, text='Work', command=lambda: bigLoop(internet, gui))
workButton.place(
    x=420,
    y=500,
    height=50,
    width=80,)

root.mainloop()
