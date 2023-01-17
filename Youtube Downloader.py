from tkinter import *
from tkinter import filedialog
from pytube import YouTube
import threading

root=Tk()
root.title("Youtube Downloader")
root.geometry("600x320")
root.resizable(FALSE,FALSE)

# my function

def browse():
    directory = filedialog.askdirectory(title="Save Video")
    folderLink.delete(0,"end")
    folderLink.insert(0,directory)
def down_yt():
    status.config(text="Status: Downloading ...")
    link = ytLink.get()
    folder = folderLink.get()
    YouTube(link,on_complete_callback=finish).streams.filter(progressive=True, file_extension="mp4").order_by("resolution").desc().first().download(folder)

def finish(stream=None,chunk=None,file_handle=None, remaining=None):
    status.config(text="Status: Complete")

#Youtube logo
ytLogo = PhotoImage(file="YouTube_Logo_(2013-2017).svg.png")
ytTitle = Label(root, image=ytLogo)
ytTitle.place(relx=0.5, rely=0.25 , anchor="center")

#Youtube Link

ytLabel = Label(root , text="Youtube Link")
ytLabel.place(x=25,y=150)

ytLink = Entry(root, width=60)
ytLink.place(x=140 , y=150)

#Download Folder

folderLabel = Label(root, text="Download Folder")
folderLabel.place(x=25 , y=183)

folderLink = Entry(root, width=50)
folderLink.place(x=140 , y=183)

#Browse Buttom

browse = Button(root,text="Browse", command=browse)
browse.place(x=455,y=180)

#Download Button

download = Button(root, text="Download", command=threading.Thread(target=down_yt).start)
download.place(x=280 , y=220)

#Status bar

status = Label(root,text="Status: Ready",font="Calibre 10 italic",fg="black",bg="white",anchor="w")
status.place(rely=1,anchor="sw",relwidth=1)


root.mainloop()