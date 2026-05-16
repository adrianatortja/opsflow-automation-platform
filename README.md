# OpsFlow Automation Platform

OpsFlow is a Python automation project for ecommerce operations, ad performance tracking, supplier monitoring, alerts, scheduled workflows, reporting, and dashboard visualization.

It reads business data, calculates key metrics, detects operational issues, sends Slack-style alert notifications, exports daily reports, and displays results in a Streamlit dashboard.

```text
data source → ingestion → metrics → alerts → reports/notifications
                                      ↓
                                  dashboard
```

---

## Why I Built This

I built OpsFlow to practice Python automation for technical operations work.

The project is based on common ecommerce operations tasks:

- checking order and fulfillment data
- reviewing ad spend and ROAS
- monitoring supplier delays
- detecting operational issues
- preparing daily reports
- visualizing KPIs in a dashboard

This project connects Python development with real business operations problems.

---

## Features

- CSV and JSON data ingestion
- Shopify-style order normalization
- simulated Meta Ads data integration
- simulated supplier status integration
- operations, ads, and supplier KPI calculation
- alert detection across multiple data sources
- Slack-style notification output
- dated CSV report export
- configurable scheduler
- Streamlit dashboard with KPI cards, charts, and alert summaries

---

## Dashboard

The Streamlit dashboard shows:

- total revenue
- total ad spend
- ROAS
- failed order rate
- pending fulfillment count
- alert summary
- Meta Ads performance
- supplier health
- charts for operations, ads, and supplier metrics

Run it with:

```bash
streamlit run dashboard.py
```

---

## Metrics Tracked

Operations:

- total revenue
- total ad spend
- ROAS
- failed order rate
- pending fulfillment count

Meta Ads:

- spend
- revenue
- ROAS
- clicks
- conversions
- conversion rate

Supplier:

- total supplier orders
- delayed supplier orders
- pending supplier orders
- supplier delay rate
- average supplier delay days

---

## Project Structure

```text
opsflow-automation-platform/
├── data/
├── reports/
├── opsflow/
│   ├── ingestion.py
│   ├── metrics.py
│   ├── alerts.py
│   ├── reporting.py
│   ├── notifications.py
│   └── pipeline.py
├── dashboard.py
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

Create and activate a virtual environment:

```bash
python -m venv venv
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the automation pipeline once:

```bash
python main.py
```

Run the dashboard:

```bash
streamlit run dashboard.py
```

Run the scheduler:

```bash
python run_scheduler.py
```

Run the scheduler with a custom interval:

```bash
python run_scheduler.py 10
```

---

## Example Output

```text
Total Revenue: $415.00
Total Ad Spend: $650.00
ROAS: 0.64
Failed Order Rate: 40.0%
Pending Fulfillment: 2
Total Alerts: 5
```

Example alerts:

```text
Operations:
- High failed order rate detected
- Low ROAS detected

Meta Ads:
- Meta Ads conversion rate is too low

Supplier:
- Supplier delay rate is high
- Supplier backlog detected
```

---

## Skills Practiced

- Python scripting
- CSV and JSON processing
- data normalization
- API-style integration simulation
- business metric calculation
- alert logic
- report generation
- scheduler logic
- Streamlit dashboard development
- Pandas-based chart data preparation
- modular project structure
- Git and GitHub workflow

---

## What This Project Demonstrates

OpsFlow demonstrates how Python can automate technical operations workflows.

The project separates responsibilities into clear modules:

- `ingestion.py` reads and normalizes data
- `metrics.py` calculates KPIs
- `alerts.py` detects business issues
- `notifications.py` formats alert messages
- `reporting.py` exports reports
- `pipeline.py` exposes reusable processed data
- `dashboard.py` visualizes the results
- `run_scheduler.py` runs the workflow repeatedly

---

## Future Improvements

- SQLite database storage
- alert history tracking
- automated tests
- Docker setup
- GitHub Actions
- dashboard filters by date/source
- historical trend charts

---

## Author

Adriana Tortja