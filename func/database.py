import sqlite3

class send_channel:
    def __init__(self) -> None:
        db_file = "database/send_channel.db"

        self.conn = sqlite3.connect(db_file)
        self.cursor = self.conn.cursor()

        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS send (
                channel_id TEXT,
                server_id TEXT
            )
        ''')
        self.conn.commit()