import discord

class CommandHandler:
    def __init__(self, bot, commands_config):
        self.bot = bot
        self.commands_config = commands_config
        self._load_commands()

    def _load_commands(self):
        for command_name, command_details in self.commands_config.items():
            response_config = command_details["response"]

            @self.bot.command(name=command_name)
            async def dynamic_command(ctx):
                if "embed" in response_config:
                    embed_config = response_config["embed"]
                    embed = discord.Embed(
                        title=embed_config.get("title", ""),
                        description=embed_config.get("description", ""),
                        color=discord.Color.blue() if embed_config.get("color") == "BLUE" else discord.Color.default()
                    )

                    if "fields" in embed_config:
                        for field in embed_config["fields"]:
                            embed.add_field(
                                name=field["name"],
                                value=field["value"],
                                inline=field.get("inline", False)
                            )

                    if "footer" in embed_config:
                        footer = embed_config["footer"]
                        embed.set_footer(
                            text=footer.get("text", ""),
                            icon_url=footer.get("icon_url", "")
                        )

                    if response_config.get("reply", False):
                        await ctx.reply(embed=embed)
                    else:
                        await ctx.send(embed=embed)
                else:
                    content = response_config.get("content", "")
                    if response_config.get("reply", False):
                        await ctx.reply(content)
                    else:
                        await ctx.send(content)
