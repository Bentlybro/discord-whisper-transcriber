import whisper
from typing import Optional

class WhisperTranscriber:
    def __init__(self, model_name: str = "base"):
        self.model = whisper.load_model(model_name)
    
    async def transcribe(self, audio_path: str) -> str:
        """
        Transcribes audio file using Whisper model
        """
        result = self.model.transcribe(audio_path)
        return result["text"]
