import mysql.connector
from config.database import DB_CONFIG

def get_db_connection():
    return mysql.connector.connect(**DB_CONFIG)

def setup_database():
    conn = get_db_connection()
    cursor = conn.cursor()
    
    # user_words table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS user_words (
            id INT AUTO_INCREMENT PRIMARY KEY,
            discord_id BIGINT,
            word VARCHAR(255),
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    
    #  user_role table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS user_role (
            id INT AUTO_INCREMENT PRIMARY KEY,
            discord_id BIGINT,
            role_id BIGINT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            UNIQUE KEY unique_user_role (discord_id, role_id)
        )
    ''')
    
    conn.commit()
    cursor.close()
    conn.close()
