import sqlite3
import pandas as pd
from sklearn.ensemble import IsolationForest


def load_data():
    conn = sqlite3.connect("security_logs.db")
    df = pd.read_sql_query("SELECT * FROM logs", conn)
    conn.close()
    return df


def prepare_features(df):
    # convertir status a número
    df["status_num"] = df["status"].map({"SUCCESS": 0, "FAILED": 1})

    # contar intentos por IP
    ip_counts = df.groupby("ip_address").size().reset_index(name="attempts")

    # contar fallos por IP
    failed = df[df["status"] == "FAILED"]
    failed_counts = failed.groupby("ip_address").size().reset_index(name="failures")

    features = pd.merge(ip_counts, failed_counts, on="ip_address", how="left")
    features.fillna(0, inplace=True)

    return features


def detect_anomalies(features):
    model = IsolationForest(contamination=0.2, random_state=42)
    features["anomaly"] = model.fit_predict(
        features[["attempts", "failures"]]
    )

    anomalies = features[features["anomaly"] == -1]

    print("\n🤖 ML Anomaly Detection")
    print("-" * 30)

    if anomalies.empty:
        print("No anomalies detected.")
    else:
        for _, row in anomalies.iterrows():
            print(
                f"⚠️ Suspicious IP {row['ip_address']} "
                f"(Attempts: {row['attempts']}, Failures: {row['failures']})"
            )


if __name__ == "__main__":
    df = load_data()
    features = prepare_features(df)
    detect_anomalies(features)
