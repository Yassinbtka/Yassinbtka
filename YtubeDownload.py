from pytube import  YouTube

def Download(link):
    yt = YouTube(link)
    yt = yt.streams.get_highest_resolution()
    try:
        yt.download()
    except:
           print("there has been error in Download your  youtube Vedio ")
    print("this download has completed! ")

link = input("Put your youtube link here !! URL: ")
Download(link)
