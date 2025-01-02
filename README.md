# Discord Word Tracker Bot

A simple bot that tracks word usage and handles roles in your Discord server.

## What it does
- Tracks words used in your server
- Shows stats about word usage
- Lets users pick their own roles
- Welcomes new members

## Commands
- `/word-status` - See the top 10 most used words in the server
- `/user-status @user` - See someone's most used words
- `/select-role` - Pick a role (Developer, Gamer, or Lurker)

## Setup

1. Install Python 3.8 or newer
2. Install MySQL

3. Set up the database:
```sql
CREATE DATABASE discord_bot;
CREATE TABLE user_words (
    discord_id BIGINT,
    word VARCHAR(255)
);
CREATE TABLE user_role (
    discord_id BIGINT,
    role_id BIGINT
);
```

4. Download the files and install requirements:
```bash
git clone <your-repo-url>
cd DiscordBot
pip install -r requirements.txt
```

5. Create a `.env` file with:
```
DISCORD_TOKEN=your_bot_token
WELCOME_CHANNEL_ID=your_welcome_channel_id
DB_HOST=localhost
DB_USER=your_db_user
DB_PASSWORD=your_db_password
DB_NAME=discord_bot
```

6. Start the bot:
```bash
python bot.py
```

7. Add to your server:
[Click here to add bot](https://discord.com/oauth2/authorize?client_id=1324246172176617503)

## Need help?
- Make sure MySQL is running
- Check if your `.env` file is set up correctly
- Create the roles: Developer, Gamer, and Lurker in your server