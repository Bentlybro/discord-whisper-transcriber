import discord
from discord.ext import commands
import os
import asyncio
from ..utils.youtube_handler import YoutubeHandler
from ..utils.transcriber import WhisperTranscriber
from config import DISCORD_TOKEN, COMMAND_PREFIX, AUDIO_DIR

class TranscriberBot(commands.Bot):
    def __init__(self):
        intents = discord.Intents.default()
        intents.message_content = True
        super().__init__(command_prefix=COMMAND_PREFIX, intents=intents)
        
        self.youtube_handler = YoutubeHandler(AUDIO_DIR)
        self.transcriber = WhisperTranscriber()
        
        # Ensure temp directories exist
        os.makedirs(AUDIO_DIR, exist_ok=True)
        
    async def setup_hook(self):
        await self.add_cog(TranscriberCog(self))

class TranscriberCog(commands.Cog):
    def __init__(self, bot: TranscriberBot):
        self.bot = bot
    
    @commands.command(name="transcribe")
    async def transcribe(self, ctx: commands.Context, url: str):
        """
        Command to transcribe YouTube videos
        Usage: !transcribe <youtube-url>
        """
        async with ctx.typing():
            try:
                # Download audio
                audio_path, title = await self.bot.youtube_handler.download_audio(url)
                
                # Transcribe audio
                transcription = await self.bot.transcriber.transcribe(audio_path)
                
                # Clean up
                os.remove(audio_path)
                
                # Send results
                await ctx.reply(f"Transcription for '{title}':\n{transcription}")
                
            except Exception as e:
                await ctx.reply(f"Error processing video: {str(e)}")
