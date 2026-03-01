# Cybersecurity Log Analysis with Python, SQL and Data Analytics

A cybersecurity data analysis project that simulates authentication logs, stores them in a SQL database, detects suspicious behavior, and visualizes potential security threats using Python.

This project demonstrates how data analysis techniques can be applied to cybersecurity monitoring and threat detection, similar to real Security Operations Center (SOC) workflows.

---

## Project Overview

Modern cybersecurity relies heavily on data analysis. Security analysts continuously monitor authentication logs to detect attacks such as brute-force attempts or targeted account abuse.

This project simulates that process by creating a complete security analytics pipeline:

logs → database → analysis → detection → visualization

---

## Features

- Simulated authentication log generation
- SQLite database storage
- SQL-based security queries
- Detection of suspicious IP addresses
- Brute-force attack identification
- Targeted account detection
- Security dashboards with visual analytics
- Machine learning–based anomaly detection
- Modular Python architecture

---

## Project Structure


cyber-log-analysis/
│
├── database.py # Creates SQL database
├── generate_logs.py # Simulates login activity
├── analyzer.py # SQL security analysis
├── threat_detection.py # Rule-based attack detection
├── dashboard.py # Data visualization
├── ml_anomaly_detection.py # Machine learning anomaly detection
├── requirements.txt
└── README.md


---

## Technologies Used

- Python
- SQLite
- Pandas
- Matplotlib
- Scikit-learn
- SQL
- Data Analysis for Cybersecurity

---

## Installation

Clone the repository:

```bash
git clone https://github.com/yourusername/cyber-log-analysis.git
cd cyber-log-analysis

Install dependencies:

pip install -r requirements.txt
How to Run
1. Create the database
python database.py
2. Generate simulated logs
python generate_logs.py
3. Perform SQL-based analysis
python analyzer.py
4. Detect threats using rule-based detection
python threat_detection.py
5. Visualize security activity
python dashboard.py
6. Run machine learning anomaly detection
python ml_anomaly_detection.py
Example Security Insights

Detection of IP addresses with excessive failed login attempts

Identification of targeted user accounts

Visualization of authentication behavior patterns

Automatic anomaly detection using machine learning

Cybersecurity Concepts Demonstrated

Security log analysis

Threat detection workflows

Brute-force attack modeling

Authentication monitoring

Data-driven cybersecurity analysis

SOC analyst methodology

Anomaly detection using machine learning

Learning Objective

This project explores the intersection between cybersecurity, data analysis, and automation using Python and SQL. It is designed as a practical demonstration of how security analysts can use data analytics techniques to identify suspicious activity.

Disclaimer

This project is intended for educational purposes only. All logs are simulated and do not represent real user data.

Author

Cybersecurity and Artificial Intelligence student focused on data-driven security analysis.
