from .bot import create_bot

def start_bot(config_path='config.json'):
    bot = create_bot(config_path)
    bot.run()
