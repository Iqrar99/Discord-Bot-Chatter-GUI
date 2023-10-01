import asyncio

from app.gui import GUIApp
from app.src.bot import BotClient


def main():
    bot = BotClient()
    try:
        asyncio.run(bot.start(GUIApp))
    except KeyboardInterrupt:
        print("Logging Out...")


if __name__ == "__main__":
    main()
