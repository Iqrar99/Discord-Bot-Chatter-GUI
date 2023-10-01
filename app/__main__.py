import asyncio

from app.src.bot import BotClient


def main():
    bot = BotClient()
    try:
        asyncio.run(bot.start())
    except KeyboardInterrupt:
        print("Logging Out...")


if __name__ == "__main__":
    main()
