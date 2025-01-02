import re
from discord.ext import commands
from db.database import get_db_connection

class WordCounter(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        # List of words to ignore
        self.ignored_words = {'the', 'a', 'an', 'and', 'or', 'but', 'in', 'on', 'at', 'to', 'for', 'of'}

    def clean_word(self, word):
        # Remove any non-alphanumeric characters
        word = re.sub(r'[^a-zA-Z0-9]', '', word)
        return word.lower()

    def is_valid_word(self, word):
        # Check if the word should be stored
        if not word or len(word) <= 2:  # Skip empty or very short words
            return False
        if word in self.ignored_words:  # Skip common words
            return False
        if any(word.startswith(prefix) for prefix in ['!', '/', '<@', 'http', 'https']):  # Skip commands, mentions, links
            return False
        if word.isdigit():  # Skip pure numbers
            return False
        return True

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.bot:
            return

        ctx = await self.bot.get_context(message)
        if ctx.valid or message.content.startswith(('!', '/')):
            return

        words = message.content.lower().split()
        valid_words = []
        
        for word in words:
            cleaned_word = self.clean_word(word)
            if self.is_valid_word(cleaned_word):
                valid_words.append(cleaned_word)
                
        if not valid_words:
            return

        try:
            print(f"Processing valid words: {valid_words}")
            conn = get_db_connection()
            cursor = conn.cursor()

            for word in valid_words:
                print(f"Storing word: {word} for user: {message.author.name}")
                cursor.execute(
                    'INSERT INTO user_words (discord_id, word) VALUES (%s, %s)',
                    (message.author.id, word)
                )

            conn.commit()
            cursor.close()
            conn.close()
            print(f"Successfully stored {len(valid_words)} words")
            
        except Exception as e:
            print(f"Error storing words in database: {str(e)}")

    @commands.hybrid_command(name="word-status")
    async def word_status(self, ctx):
        """Shows the 10 most used words in the server"""
        try:
            conn = get_db_connection()
            cursor = conn.cursor()

            cursor.execute('''
                SELECT word, COUNT(*) as count
                FROM user_words
                WHERE LENGTH(word) > 2
                GROUP BY word
                HAVING count > 1
                ORDER BY count DESC
                LIMIT 10
            ''')

            results = cursor.fetchall()
            cursor.close()
            conn.close()

            if not results:
                await ctx.send("No words have been tracked yet!")
                return

            response = "Top 10 most used words:\n```"
            for word, count in results:
                response += f"{word}: {count} times\n"
            response += "```"

            await ctx.send(response)
        except Exception as e:
            await ctx.send(f"Error retrieving word status: {str(e)}")

    @commands.hybrid_command(name="user-status")
    async def user_status(self, ctx, user: commands.UserConverter):
        """Shows the 10 most used words by a specific user"""
        conn = get_db_connection()
        cursor = conn.cursor()

        cursor.execute('''
            SELECT word, COUNT(*) as count
            FROM user_words
            WHERE discord_id = %s
            GROUP BY word
            ORDER BY count DESC
            LIMIT 10
        ''', (user.id,))

        results = cursor.fetchall()
        cursor.close()
        conn.close()

        if not results:
            await ctx.send(f"No words have been tracked for {user.name} yet!")
            return

        response = f"Top 10 most used words by {user.name}:\n```"
        for word, count in results:
            response += f"{word}: {count} times\n"
        response += "```"

        await ctx.send(response)

async def setup(bot):
    await bot.add_cog(WordCounter(bot))
