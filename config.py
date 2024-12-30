import yt_dlp
import os
from typing import Tuple

class YoutubeHandler:
    def __init__(self, output_dir: str):
        self.output_dir = output_dir
        
    async def download_audio(self, url: str) -> Tuple[str, str]:
        """
        Downloads audio from YouTube video and returns file path and title
        """
        ydl_opts = {
            'format': 'bestaudio/best',
            'outtmpl': f'{self.output_dir}/%(title)s.%(ext)s',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'wav',
            }],
        }
        
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)
            title = info['title']
            filepath = f"{self.output_dir}/{title}.wav"
            
        return filepath, title
