import tkinter as tk
import yt_dlp

window = tk.Tk() # main window or frame

window.title("Downloader") # title of the main frame or window
window.geometry("800x300") # size of the frame 

# Add a label to the window
label = tk.Label(window, text="Music and Video Download", font = ('Times New Roman', 14)) # there are additional arguments like width and height for explicitly setting up the size, otherwise the area covered of by the text will be the size of the label
label.grid(row = 0, column = 0, padx = 10, pady = 5)

label2 = tk.Label(window, text = "Enter Youtube link: ", font = ("Times New Roman", 12) )
label2.grid(row = 1, column = 0)

entry = tk.Entry(window, width = 50) # it is a single line textbox
entry.grid(row = 1, column = 1, padx = 10, pady = 5)

def download_video():
    ydl_opts = {
        'ffmpeg_location': r'E:\Python\Downloader\ffmpeg-master-latest-win64-gpl-shared\bin',
        'format': 'bestvideo+bestaudio/best',
        'merge_output_format': 'mp4',
        'outtmpl': 'C:/Users/ACER/Downloads/%(title)s.%(ext)s'
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([entry.get()])
    
def download_audio():
    ydl_opts = {
        'ffmpeg_location': r'E:\Python\Downloader\ffmpeg-master-latest-win64-gpl-shared\bin',
        'format': 'bestaudio/best',
        'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
        'outtmpl': 'C:/Users/ACER/Downloads/%(uploader)s - %(title)s.%(ext)s'  # saves with video title
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([entry.get()])
    

def clear():
    entry.delete(0, tk.END)   # delete from index 0 to END

button = tk.Button(window, text="Download video", command = download_video)
button.grid(row = 4, column = 0, pady = 10)

button1 = tk.Button(window, text="Download MP3", command = download_audio)
button1.grid(row = 4, column = 1, pady = 10)

button2 = tk.Button(window, text="Clear", command = clear)
button2.grid(row = 4, column = 2, pady = 10)

window.mainloop() # Start the main event loop

