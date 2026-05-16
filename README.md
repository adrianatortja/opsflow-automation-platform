# OpsFlow Automation Platform

OpsFlow is a Python automation project for ecommerce operations, ad performance tracking, supplier monitoring, alerts, notifications, and reporting workflows.

It reads operations data, calculates key business metrics, detects issues, sends Slack-style alert notifications, and exports dated daily reports.

```text
data source → ingestion → metrics → alerts → notifications/reporting
```

---

## Why I Built This

I built OpsFlow to practice Python automation for technical operations work.

The project is based on common ecommerce and operations tasks like:

- checking order data
- reviewing ad spend
- calculating ROAS
- spotting failed orders
- monitoring supplier delays
- tracking fulfillment issues
- preparing daily reports
- sending operational alerts
- running workflows automatically

This project connects backend/Python development with real business operations problems.

---

## Features

- Read order data from CSV
- Read fake Shopify-style JSON order data
- Normalize external data into one internal format
- Simulate API-style Meta Ads data integration
- Simulate supplier and fulfillment data integration
- Calculate operations, ads, and supplier metrics
- Detect operational issues across multiple data sources
- Generate Slack-style alert notifications
- Export dated daily CSV reports
- Run the automation manually or with a scheduler
- Configure the scheduler interval from the command line
- Safely handle invalid scheduler input

---

## Metrics

OpsFlow calculates operations metrics such as:

- total revenue
- total ad spend
- ROAS
- failed order rate
- pending fulfillment count

It also calculates Meta Ads metrics such as:

- total Meta Ads spend
- total Meta Ads revenue
- Meta Ads ROAS
- total clicks
- total conversions
- conversion rate

It also calculates supplier metrics such as:

- total supplier orders
- delayed supplier orders
- pending supplier orders
- supplier delay rate
- average supplier delay days

---

## Alerts

OpsFlow creates alerts when business rules detect problems.

Examples:

- failed order rate is too high
- ROAS is too low
- Meta Ads conversion rate is too low
- supplier delay rate is too high
- supplier backlog is detected

These alerts are included in both the report and the Slack-style notification output.

---

## Project Structure

```text
opsflow-automation-platform/
├── data/
│   ├── orders.csv
│   ├── ads.csv
│   ├── fake_shopify_orders.json
│   ├── fake_meta_ads.json
│   └── fake_supplier_status.json
├── reports/
│   └── daily_ops_report_YYYY-MM-DD.csv
├── opsflow/
│   ├── __init__.py
│   ├── ingestion.py
│   ├── metrics.py
│   ├── alerts.py
│   ├── reporting.py
│   └── notifications.py
├── main.py
├── run_scheduler.py
├── README.md
└── requirements.txt
```

---

## How To Run

Clone the repository:

```bash
git clone https://github.com/adrianatortja/opsflow-automation-platform.git
cd opsflow-automation-platform
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

Run the automation pipeline manually:

```bash
python main.py
```

A dated report will be created inside the `reports/` folder:

```text
reports/daily_ops_report_YYYY-MM-DD.csv
```

Example:

```text
reports/daily_ops_report_2026-05-16.csv
```

---

## Scheduling

OpsFlow includes a scheduler runner that can automatically execute the full automation pipeline at a fixed interval.

Start the scheduler with the default interval of 60 seconds:

```bash
python run_scheduler.py
```

Run the scheduler with a custom interval by passing the number of seconds:

```bash
python run_scheduler.py 10
```

This runs the OpsFlow pipeline every 10 seconds.

If an invalid interval is provided, the scheduler safely falls back to the default interval:

```bash
python run_scheduler.py abc
```

Example fallback behavior:

```text
Invalid interval value. Using default interval.
The workflow will run every 60 seconds.
```

Stop the scheduler manually with:

```text
CTRL + C
```

This keeps the project flexible:

- `main.py` runs the pipeline once
- `run_scheduler.py` handles repeated scheduled execution
- the interval can be changed from the command line

---

## Example Terminal Output

```text
--- Slack-style Notification ---
🚨 OpsFlow Alert

Total Alerts: 5

Operations:
- High failed order rate detected
- Low ROAS detected

Meta Ads:
- Meta Ads conversion rate is too low

Supplier:
- Supplier delay rate is high
- Supplier backlog detected

--- End Notification ---

Report generated: reports/daily_ops_report_2026-05-16.csv

Daily operations metrics:
{
  'total_revenue': 415.0,
  'total_ad_spend': 650.0,
  'roas': 0.6384615384615384,
  'failed_order_rate': 0.4,
  'pending_fulfillment': 2
}
```

---

## Example Scheduler Output

```text
OpsFlow scheduler started.
The workflow will run every 60 seconds.
Press CTRL + C to stop the scheduler.

==============================
Running OpsFlow pipeline at 2026-05-16 12:30:00
==============================

OpsFlow pipeline completed successfully.

Next run in 60 seconds...
```

---

## Skills Practiced

- Python scripting
- CSV processing
- JSON processing
- data normalization
- API-style integration simulation
- business metric calculation
- alert logic
- notification formatting
- report generation
- scheduler logic
- command-line arguments
- defensive input validation
- modular project structure
- Git and GitHub

---

## What This Project Demonstrates

This project demonstrates how Python can be used to automate technical operations workflows.

It shows how data can move through a clean automation pipeline:

```text
input data → processing → business rules → alerts → reports
```

It also demonstrates separation of responsibility:

- ingestion code reads data
- metrics code calculates KPIs
- alerts code detects problems
- notifications code formats alert messages
- reporting code exports business-readable reports
- scheduler code runs the workflow automatically

---

## Future Improvements

- Streamlit dashboard
- SQLite database storage
- alert history tracking
- automated tests
- Docker setup
- GitHub Actions
- PostgreSQL support
- optional Django version

---

## Author

Adriana Tortja