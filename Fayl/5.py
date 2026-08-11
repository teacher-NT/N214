import os
os.system("cls")

from pytubefix import YouTube

link = input("Youtube video linkini kiriting: ")

try:
    yt = YouTube(link)
    video = yt.streams.get_highest_resolution()
    # video2 = yt.streams.get_lowest_resolution()
    print("Video yuklanmoqda...")
    video.download(".")
    print("Video yuklandi.")
except:
    print("Video yuklashda xatolik")
