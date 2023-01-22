from pytube import YouTube
import subprocess
import threading
from time import sleep
import sys
import os


class YouTubeSnagger:
    def __init__(self, link):
        self.link = link

    def convert_to_mp4(self,file_name):
        def print_loading():
            while True:
                for i in range(5):
                    if kill_thread:
                        break
                    print(".",end='',flush=True)
                    sleep(0.5)
                print('\r                               \r',end='',flush=True)
                if kill_thread:
                    break

        try:

            kill_thread = False
            loading_thread = threading.Thread(target=print_loading)
            loading_thread.start()

            yt = YouTube(self.link)

            video = yt.streams.filter(type = "video", video_codec = "vp9", progressive = False).order_by("resolution")[-1]
            audio = yt.streams.filter(type = "audio", audio_codec = ("mp4a.40.2" or "mp4a.40.5"), progressive = False).order_by('abr')[-1]

            video.download(output_path = "temp", filename = "video.mp4")
            audio.download(output_path = "temp", filename = "audio.mp4")

            subprocess.run("ffmpeg -i temp/video.mp4 -i temp/audio.mp4 -c copy downloads/mp4s/"+file_name+".mp4")

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
    
    def convert_to_mp3(self,file_name):
        def print_loading():
            while True:
                for i in range(5):
                    if kill_thread:
                        break
                    print(".",end='',flush=True)
                    sleep(0.5)
                print('\r                               \r',end='',flush=True)
                if kill_thread:
                    break

        kill_thread = False
        loading_thread = threading.Thread(target=print_loading)
        loading_thread.start()

        yt = YouTube(self.link)
        audio = yt.streams.filter(type = "audio", audio_codec = ("mp4a.40.2" or "mp4a.40.5"), progressive = False).order_by('abr')[-1]
        audio.download(output_path = "downloads/mp3s", filename = ""+file_name+".mp3")
        kill_thread = True
        print("Your MP3 file is downloaded")
        sys.exit(0)

if __name__ == "__main__":
    
    link = input("LINK:")
    output_name = input("OUTPUT FILE NAME:")
    youtube = YouTubeSnagger(link)

    if (len(sys.argv) > 1):
        file_ext = sys.argv[1]
    else:
        file_ext = "mp3"

    if file_ext == "mp3":
        youtube.convert_to_mp3(output_name)
    elif file_ext == "mp4":
        youtube.convert_to_mp4(output_name)
    else:
        print("help")



