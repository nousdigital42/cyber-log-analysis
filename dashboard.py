import sqlite3
import pandas as pd
import matplotlib.pyplot as plt


def load_data():
    conn = sqlite3.connect("security_logs.db")
    df = pd.read_sql_query("SELECT * FROM logs", conn)
    conn.close()
    return df


def login_status_chart(df):
    counts = df["status"].value_counts()

    plt.figure()
    counts.plot(kind="bar")

    plt.title("Login Status Distribution")
    plt.xlabel("Status")
    plt.ylabel("Count")

    plt.show()


def failed_attempts_by_ip(df):
    failed = df[df["status"] == "FAILED"]
    grouped = failed["ip_address"].value_counts()

    plt.figure()
    grouped.plot(kind="bar")

    plt.title("Failed Login Attempts by IP")
    plt.xlabel("IP Address")
    plt.ylabel("Failures")

    plt.show()


if __name__ == "__main__":
    data = load_data()
    login_status_chart(data)
    failed_attempts_by_ip(data)
