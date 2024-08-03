
# **ForgeCord** | Discord Made Simple

**ForgeCord** Is a simple and easy way to create Discord bots easily using the power of **Json**.

## Features

- **JSON Configuration:** Write bot commands, responses, and embeds and more through a simple JSON file.
- **Embed Support:** Easily create embeds with titles, descriptions, fields, colours and footers!

## Installation 

`pip install git+https://github.com/ImLimiteds/ForgeCord.git`


## Usage

**Create main.py**

```python
import forgecord

forgecord.start('config.json')
```

**Create config.json**

Creating a bot in **ForgeCord** is quite simple. Here is a basic example for a bot that responds with an embed if the user says `!demo`

```json
{
    "token": "{YourBotToken}",
    "intents": "all",
    "prefix": "!",
    "commands": {
        "demo": {
            "response": {
                "embed": {
                    "title": "This is a demo!",
                    "description": "This is a description!",
                    "color": "BLUE",
                    "fields": [
                        {
                            "name": "This is a field!",
                            "value": "This is the description of a field!",
                            "inline": true
                        },
                        {
                            "name": "This is a second field!",
                            "value": "This is the description of the second field!",
                            "inline": false
                        }
                    ],
                    "footer": {
                        "text": "Hello! I'm a footer!",
                        "icon_url": "iconurlinkgoeshere"
                    }    
                },
                "reply": true
            },
            "description": "Demonstration Command!"
        }
    }
}
```


## Support

- **[Discord Server](https://discord.gg/jAfKSgZyUf)**

## Requirements:

- **Discord.py**
- **Python 3.11 or Higher**
## Contributing

Contributions are always welcome, Just Create a Pull Request.

