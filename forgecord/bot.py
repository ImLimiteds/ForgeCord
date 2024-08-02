import json
import discord
from discord.ext import commands
from forgecord.command_handler import CommandHandler


class ForgeBot(commands.Bot):
    def __init__(self, config_path):
        with open(config_path, 'r') as file:
            self.config = json.load(file)

        intents = discord.Intents.all() if self.config["intents"] == "all" else discord.Intents.default()
        super().__init__(command_prefix=self.config["prefix"], intents=intents)

        self.command_handler = CommandHandler(self, self.config["commands"])

    def run(self):
        super().run(self.config["token"])


def create_bot(config_path='config.json'):
    return ForgeBot(config_path)
