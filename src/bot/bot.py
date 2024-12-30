import asyncio
from src.bot.bot import TranscriberBot
from config import DISCORD_TOKEN

async def main():
    bot = TranscriberBot()
    await bot.start(DISCORD_TOKEN)

if __name__ == "__main__":
    asyncio.run(main())
