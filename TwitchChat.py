#Creates a GUI for the display of a single twitch chat by connecting 
#to the twitch API, Chat is also printed to terminal and logged in 
#a chat.log

import socket
import logging
import threading
from emoji import demojize
import tkinter as tk
from tkinter import *

#GUI root
root = tk.Tk()
root.title('Twitch Chat')

#API connection parameters
server = 'irc.chat.twitch.tv'
port = 6667
nickname = 'YOUR TWITCH NAME HERE'
token = 'YOUR AUTH TOKEN HERE'
channel = '#STREAM NANME HERE, KEEEP # AT START'

def startConnect():
    tempMsg=''
    tempMsg1=''
    tempMsg2=''
    tempMsg3=''
    tempMsg4=''
    tempMsg5=''
    tempMsg6=''
    tempMsg7=''
    tempMsg8=''
    tempMsg9=''
    #socket connection
    sock = socket.socket()
    sock.connect((server, port))

    sock.send(f"PASS {token}\n".encode('utf-8'))
    sock.send(f"NICK {nickname}\n".encode('utf-8'))
    sock.send(f"JOIN {channel}\n".encode('utf-8'))

    logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(message)s',
                    datefmt='%Y-%m-%d_%H:%M:%S',
                    handlers=[logging.FileHandler('chat.log',encoding='utf-8')])
        
    while True:
        response = sock.recv(2048).decode('utf-8')

        if response.startswith('PING'):
            sock.send('PONG\n'.encode('utf-8'))
        
        elif len(response) > 0:
            logging.info(demojize(response))
            tempMsg9=tempMsg8
            tempMsg8=tempMsg7
            tempMsg7=tempMsg6
            tempMsg6=tempMsg5
            tempMsg5=tempMsg4
            tempMsg4=tempMsg3
            tempMsg3=tempMsg2
            tempMsg2=tempMsg1
            tempMsg1=tempMsg
            tempMsg= response.split(':')[2]

            message0.config(text=tempMsg)
            message1.config(text=tempMsg1)
            message2.config(text=tempMsg2)
            message3.config(text=tempMsg3)
            message4.config(text=tempMsg4)
            message5.config(text=tempMsg5)
            message6.config(text=tempMsg6)
            message7.config(text=tempMsg7)
            message8.config(text=tempMsg8)
            message9.config(text=tempMsg9)
            print(response)


chat = threading.Thread(target=startConnect)
chat.start()

#Create the GUI
canvas = tk.Canvas(root, height=650, width=500, bg='#222222')
canvas.pack()

frame = tk.Frame(root, bg='#222222', borderwidth = 2 ,relief='sunken')
frame.place(relheight=.85, relwidth=.85, relx=.075, rely=.075)

#Set up message stream
txtFont = 'Roobert'
txtColor = '#faf9f6'
backColor = '#222222'
msgAspect = 520

message0 = Message(frame)
message0.config(font=txtFont ,aspect=msgAspect, fg=txtColor, bg=backColor,pady=0)
message0.place(x=0,y=540)

message1 = Message(frame)
message1.config(font=txtFont, aspect=msgAspect, fg=txtColor, bg=backColor,pady=0)
message1.place(x=0,y=480)

message2 = Message(frame)
message2.config(font=txtFont ,aspect=msgAspect, fg=txtColor, bg=backColor,pady=0)
message2.place(x=0,y=420)

message3 = Message(frame)
message3.config(font=txtFont, aspect=msgAspect, fg=txtColor, bg=backColor,pady=0)
message3.place(x=0,y=360)

message4 = Message(frame)
message4.config(font=txtFont ,aspect=msgAspect, fg=txtColor, bg=backColor, pady=0)
message4.place(x=0,y=300)

message5 = Message(frame)
message5.config(font=txtFont, aspect=msgAspect, fg=txtColor, bg=backColor, pady=0)
message5.place(x=0,y=240)

message6 = Message(frame)
message6.config(font=txtFont ,aspect=msgAspect, fg=txtColor, bg=backColor,pady=0)
message6.place(x=0,y=180)

message7 = Message(frame)
message7.config(font=txtFont, aspect=msgAspect, fg=txtColor, bg=backColor,pady=0)
message7.place(x=0,y=120)

message8 = Message(frame)
message8.config(font=txtFont ,aspect=msgAspect, fg=txtColor, bg=backColor,pady=0)
message8.place(x=0,y=60)

message9 = Message(frame)
message9.config(font=txtFont, aspect=msgAspect, fg=txtColor, bg=backColor,pady=0)
message9.place(x=0,y=0)

#initialize message text to ''
message0.config(text='')
message1.config(text='')
message2.config(text='')
message3.config(text='')
message4.config(text='')
message5.config(text='')
message6.config(text='')
message7.config(text='')
message8.config(text='')
message9.config(text='')

root.mainloop()




