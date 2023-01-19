from pytube import YouTube
import subprocess
import threading
from time import sleep
import sys
import os



def print_loading():
    while True:
        for i in range(5):
           print(".",end='',flush=True)
           sleep(0.5)
        print('\r                   \r', end = '', flush=True)

        if kill_thread:
            break



try:

    link = input("LINK:")
    output_name = input("OUTPUT FILE NAME:")

    kill_thread = False
    loading_thread = threading.Thread(target=print_loading)
    loading_thread.start()

    yt = YouTube(link)

    video = yt.streams.filter(type = "video", video_codec = "vp9", progressive = False).order_by("resolution")[-1]
    audio = yt.streams.filter(type = "audio", audio_codec = ("mp4a.40.2" or "mp4a.40.5"), progressive = False).order_by('abr')[-1]

    video.download(output_path = "temp", filename = "video.mp4")
    audio.download(output_path = "temp", filename = "audio.mp4")

    subprocess.run("ffmpeg -i temp/video.mp4 -i temp/audio.mp4 -c copy "+output_name+".mp4")

    kill_thread = True

    print("Video Downloaded")
    print("Clearing temp files")

    os.remove("temp/video.mp4")
    os.remove("temp/audio.mp4")

    print("All Done!")

    sys.exit(0)

except KeyboardInterrupt:
    kill_thread = True
    sys.exit(0)

except:
    kill_thread = True
    print("\r                       \r")
    print("Something Went Wrong")
    print("Check network settings or validity of link")
    sys.exit(0)
