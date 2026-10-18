import yt_dlp

def download(url, out="."):
    ydl_opts = {
        "format": "bestvideo+bestaudio/best",
        "outtmpl": f"{out}/%(title)s.%(ext)s",
        "merge_output_format": "mp4",
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=True)
        print("Downloaded:", info["title"])

if __name__ == "__main__":
    download(input("Youtube URL: "))