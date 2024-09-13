import tkinter as tk
from tkinter import messagebox, filedialog
from pytubefix import YouTube

class YouTubeDownloader:
    def __init__(self, root):
        self.root = root
        self.root.title("Rex YouTube Downloader")
        self.root.geometry("500x250")
        self.create_widgets()

    def create_widgets(self):
        # Label for URL input
        self.label = tk.Label(self.root, text="Please Enter YouTube Video URL: ")
        self.label.pack(pady=10)

        # Entry box for URL input
        self.url_entry = tk.Entry(self.root, width=50)
        self.url_entry.pack(pady=10)

        # Download Button
        self.download_button = tk.Button(self.root, text="Download", command=self.download_video)
        self.download_button.pack(pady=20)

    def download_video(self):
        link = self.url_entry.get()
        if link:
            try:
                yt = YouTube(link)
                stream = yt.streams.filter(progressive=True, file_extension='mp4').get_highest_resolution()
                
                # Ask the user to select a download location
                download_location = filedialog.askdirectory()
                
                if download_location:
                    stream.download(download_location)
                    messagebox.showinfo("Success", f"Downloaded '{yt.title}' successfully!")
                else:
                    messagebox.showwarning("Cancelled", "Download location not selected.")
            except Exception as e:
                messagebox.showerror("Error", f"Failed to download video. Error: {str(e)}")
        else:
            messagebox.showwarning("Input Error", "Please enter a valid YouTube URL.")

root = tk.Tk()
app = YouTubeDownloader(root)
root.mainloop()
