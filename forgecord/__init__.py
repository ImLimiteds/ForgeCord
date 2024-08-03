from .bot import create_bot

def start(config_path='config.json'):
    bot = create_bot(config_path)
    bot.run()
