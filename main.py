import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Bot configuration
DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')
COMMAND_PREFIX = '!'

# Paths configuration
TEMP_DIR = 'temp'
AUDIO_DIR = f'{TEMP_DIR}/audio'
