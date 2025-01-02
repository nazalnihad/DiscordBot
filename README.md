# 🤖 Available Commands- `/word-status` - Shows the 10 most used words in the server- `/user-status @user` - Shows the 10 most used words by a specific user- `/select-role` - Choose your role from available options##  Setup Guide### Prerequisites1. Python 3.8 or higher2. MySQL database3. Discord Bot Token### Installation Steps1. Clone this repo2. Create a virtual environment:   ```bash   python -m venv venv   source venv/bin/activate  # On Windows use: venv\Scripts\activate   ```3. Install required packages:   ```bash   pip install -r requirements.txt   ```4. Create a `.env` file in the project root with:   ```   DISCORD_TOKEN=your_bot_token_here   WELCOME_CHANNEL_ID=your_channel_id   DB_HOST=localhost   DB_USER=your_database_user
   DB_PASSWORD=your_database_password
   DB_NAME=your_database_name
   ```
5. Set up your MySQL database using the provided schema

### Running the Bot
1. Activate your virtual environment
2. Run the bot:
   ```bash
   python bot.py
   ```
3. [Add the bot to your server](https://discord.com/oauth2/authorize?client_id=1324246172176617503)

## 💡 Note
This bot needs to be run locally on your computer. Make sure to keep it running to maintain functionality!

## 🤝 Need Help?
If you encounter any issues:
1. Check if your database is properly configured
2. Verify your `.env` file settings
3. Ensure all required roles exist in your server