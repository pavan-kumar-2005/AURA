import yt_dlp
import webbrowser
from urllib.parse import quote
def play_music(command):
    song=command.removeprefix("play ")
    ydl_opts={
        "quiet":True,
        "extract_flat":True
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        result=ydl.extract_info(f"ytsearch1:{song}",download=False)
    entries=result["entries"]
    video=entries[0]
    video_url=video.get("url")
    webbrowser.open(video_url)
    return f"Playing {song}"
