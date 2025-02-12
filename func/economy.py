import sqlite3
import discord
from discord.ext import commands

conn = sqlite3.connect('tb.db')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS user_tb (
        user_id TEXT PRIMARY KEY,
        amount INTEGER DEFAULT 0
    )
''')
conn.commit()

def get_user_tb(user_id):
    cursor.execute('SELECT amount FROM user_tb WHERE user_id = ?', (user_id,))
    result = cursor.fetchone()
    return result[0] if result else 0

def update_user_tb(user_id, amount):
    if get_user_tb(user_id) == 0:
        cursor.execute('INSERT INTO user_tb (user_id, amount) VALUES (?, ?)', (user_id, amount))
    else:
        cursor.execute('UPDATE user_tb SET amount = ? WHERE user_id = ?', (amount, user_id))
    conn.commit()

