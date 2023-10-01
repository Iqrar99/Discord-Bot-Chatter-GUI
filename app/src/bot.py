import logging

import aiohttp
import discord
from discord.ext.commands import Bot

from app import __version__
from app.config import BOT_PREFIX, BOT_TOKEN

discord.utils.setup_logging(level=logging.INFO, root=False)


class BotClient(Bot):
    def __init__(self) -> None:
        super().__init__(
            command_prefix=BOT_PREFIX,
            strip_after_prefix=True,
            intents=discord.Intents.all(),
            help_command=None,
        )
        self.session: aiohttp.ClientSession = None
        self.version = __version__

    async def on_ready(self) -> None:
        print("The bot is online!")
        print("Logged in as {}".format(self.user))
        print("------------------")

    async def setup_hook(self) -> None:
        if not self.session:
            self.session = aiohttp.ClientSession()

        self.bot_app_info = await self.application_info()
        self.owner_id = self.bot_app_info.owner.id

    async def close(self) -> None:
        await self.session.close()
        await super().close()

    async def start(self) -> None:
        return await super().start(BOT_TOKEN, reconnect=True)
