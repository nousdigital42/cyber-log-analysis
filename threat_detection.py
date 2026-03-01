import sqlite3
import pandas as pd


THRESHOLD_FAILED = 15


def load_data():
    conn = sqlite3.connect("security_logs.db")
    df = pd.read_sql_query("SELECT * FROM logs", conn)
    conn.close()
    return df


def detect_bruteforce(df):
    failed = df[df["status"] == "FAILED"]

    grouped = (
        failed.groupby("ip_address")
        .size()
        .reset_index(name="failures")
    )

    attackers = grouped[grouped["failures"] > THRESHOLD_FAILED]

    print("\n🚨 Brute Force Detection")
    print("-" * 30)

    if attackers.empty:
        print("No brute force detected.")
    else:
        for _, row in attackers.iterrows():
            print(f"⚠️ IP {row['ip_address']} → {row['failures']} failures")


def targeted_user_attack(df):
    failed = df[df["status"] == "FAILED"]

    grouped = (
        failed.groupby("username")
        .size()
        .reset_index(name="attempts")
    )

    targets = grouped[grouped["attempts"] > 10]

    print("\n🎯 Targeted Accounts")
    print("-" * 30)

    for _, row in targets.iterrows():
        print(f"User {row['username']} targeted ({row['attempts']} attempts)")


if __name__ == "__main__":
    data = load_data()
    detect_bruteforce(data)
    targeted_user_attack(data)
