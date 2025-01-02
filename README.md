# Discord Word Tracker Bot

A simple bot that tracks word usage and handles roles in your Discord server.

## Commands
- `/word-status` - See the top 10 most used words in the server
- `/user-status @user` - See someone's most used words
- `/select-role` - Pick a role (Developer, Gamer, or Lurker)

## Setup

1. Install Python 3.8 or newer
2. Install MySQL


4. Download the files and install requirements:
```bash
git clone https://github.com/nazalnihad/DiscordBot.git
cd DiscordBot
pip install -r requirements.txt
```

5. Create a `.env` file with:
```
DISCORD_TOKEN=your_bot_token
```

6. Start the bot
   
7. setup configs and db credentials
```bash
python main.py
```

7. Add to your server:
[Click here to add bot](https://discord.com/oauth2/authorize?client_id=1324246172176617503)

- Make sure MySQL is running
- Check if your `.env` file is set up correctly
- Create the roles: Developer, Gamer, and Lurker in your server
