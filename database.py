import sqlite3

def create_database():
    conn = sqlite3.connect("security_logs.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS logs (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        timestamp TEXT,
        ip_address TEXT,
        username TEXT,
        status TEXT
    )
    """)

    conn.commit()
    conn.close()

if __name__ == "__main__":
    create_database()
