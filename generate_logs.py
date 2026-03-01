import sqlite3
import random
from datetime import datetime, timedelta

ips = ["192.168.1.10", "10.0.0.5", "45.33.12.90", "203.0.113.7"]
users = ["admin", "user1", "guest", "root"]

def random_time():
    now = datetime.now()
    delta = timedelta(minutes=random.randint(0, 500))
    return (now - delta).strftime("%Y-%m-%d %H:%M:%S")

def generate_logs(n=100):
    conn = sqlite3.connect("security_logs.db")
    cursor = conn.cursor()

    for _ in range(n):
        ip = random.choice(ips)
        user = random.choice(users)

        # simular ataques
        if ip == "45.33.12.90":
            status = random.choice(["FAILED", "FAILED", "FAILED", "SUCCESS"])
        else:
            status = random.choice(["SUCCESS", "FAILED"])

        cursor.execute("""
        INSERT INTO logs (timestamp, ip_address, username, status)
        VALUES (?, ?, ?, ?)
        """, (random_time(), ip, user, status))

    conn.commit()
    conn.close()

if __name__ == "__main__":
    generate_logs()
