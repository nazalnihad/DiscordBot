import mysql.connector
from config.database import DB_CONFIG

def get_db_connection():
    return mysql.connector.connect(**DB_CONFIG)

def setup_database():
    conn = get_db_connection()
    cursor = conn.cursor()
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS user_words (
            id INT AUTO_INCREMENT PRIMARY KEY,
            discord_id BIGINT,
            word VARCHAR(255),
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    
    conn.commit()
    cursor.close()
    conn.close()
