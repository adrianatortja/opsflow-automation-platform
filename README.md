# OpsFlow Automation Platform

OpsFlow is a Python automation project for ecommerce operations, ad performance tracking, alerts, and reporting workflows.

It reads operations data, calculates key metrics, detects issues, and exports a daily report.

```text
input → processing → decision → output
```

---

## Why I Built This

I built OpsFlow to practice Python automation for technical operations work.

The project is based on common ecommerce operations tasks like:

- checking order data
- reviewing ad spend
- calculating ROAS
- spotting failed orders
- tracking fulfillment issues
- preparing daily reports

---

## Features

- Read order data from CSV
- Read ad spend data from CSV
- Read fake Shopify-style JSON order data
- Normalize external data into one internal format
- Calculate business metrics
- Detect operational issues
- Export a daily CSV report

---

## Metrics

OpsFlow calculates:

- total revenue
- total ad spend
- ROAS
- failed order rate
- pending fulfillment count

---

## Alerts

OpsFlow creates alerts when:

- failed order rate is higher than 10%
- ROAS is lower than 1.5
- pending fulfillment is higher than 20

---

## Project Structure

```text
opsflow-automation-platform/
├── data/
│   ├── orders.csv
│   ├── ads.csv
│   └── fake_shopify_orders.json
├── reports/
│   └── daily_ops_report.csv
├── opsflow/
│   ├── __init__.py
│   ├── ingestion.py
│   ├── metrics.py
│   ├── alerts.py
│   └── reporting.py
├── main.py
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

Run the project:

```bash
python main.py
```

The report will be created here:

```text
reports/daily_ops_report.csv
```

---

## Example Output

```text
Daily operations metrics:
{
  'total_revenue': 415.0,
  'total_ad_spend': 650.0,
  'roas': 0.6384615384615384,
  'failed_order_rate': 0.4,
  'pending_fulfillment': 2
}

Alerts:
[
  'High failed order rate detected',
  'Low ROAS detected'
]
```

---

## Skills Practiced

- Python scripting
- CSV processing
- JSON processing
- data normalization
- business metric calculation
- alert logic
- report generation
- modular project structure
- Git and GitHub

---

## Future Improvements

- fake Meta Ads API data
- supplier or warehouse data
- email alerts
- scheduled automation
- Google Sheets export
- Streamlit dashboard
- PostgreSQL
- Docker
- GitHub Actions

---

## Author

Adriana Palushi Tortja