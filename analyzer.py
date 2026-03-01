import sqlite3

def suspicious_ips():
    conn = sqlite3.connect("security_logs.db")
    cursor = conn.cursor()

    query = """
    SELECT ip_address, COUNT(*) as failed_attempts
    FROM logs
    WHERE status = 'FAILED'
    GROUP BY ip_address
    HAVING failed_attempts > 10
    """

    cursor.execute(query)

    results = cursor.fetchall()

    print("\n🚨 Suspicious IPs:")
    for ip, count in results:
        print(f"{ip} → {count} failed attempts")

    conn.close()


def login_statistics():
    conn = sqlite3.connect("security_logs.db")
    cursor = conn.cursor()

    query = """
    SELECT status, COUNT(*)
    FROM logs
    GROUP BY status
    """

    cursor.execute(query)

    print("\n📊 Login Statistics:")
    for row in cursor.fetchall():
        print(row)

    conn.close()


if __name__ == "__main__":
    suspicious_ips()
    login_statistics()
