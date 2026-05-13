# OpsFlow Automation Platform

OpsFlow is a Python automation project for ecommerce operations, ad performance tracking, alerts, and reporting.

I built this project to practice the kind of work used in technical operations roles: reading data, processing it, finding issues, and generating reports automatically.

---

## What It Does

OpsFlow takes simple operations data and turns it into useful business information.

Right now, it can:

- read order data from CSV
- read ad spend data from CSV
- read fake Shopify-style JSON order data
- normalize external data into one format
- calculate business metrics
- detect problems with simple alert rules
- export a daily operations report to CSV

The main flow is:

```text
input → processing → decision → output
```

Example:

```text
orders + ad spend
→ calculate revenue, ROAS, failed orders, pending fulfillment
→ detect problems
→ create a report
```

---

## Why I Built This

I wanted to build a project that is closer to real operations work, not only CRUD APIs.

In many ecommerce or performance marketing teams, people often repeat the same manual tasks:

- checking spreadsheets
- calculating numbers
- looking for failed orders
- checking if ad spend is performing
- preparing daily reports

OpsFlow is a small version of that workflow, automated with Python.

---

## Current Features

- CSV data ingestion
- JSON data ingestion
- Shopify-style data normalization
- revenue calculation
- ad spend calculation
- ROAS calculation
- failed order rate calculation
- pending fulfillment count
- alert detection
- CSV report export

---

## Metrics Calculated

OpsFlow currently calculates:

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
│
├── reports/
│   └── daily_ops_report.csv
│
├── opsflow/
│   ├── __init__.py
│   ├── ingestion.py
│   ├── metrics.py
│   ├── alerts.py
│   └── reporting.py
│
├── main.py
├── README.md
└── requirements.txt
```

---

## How The Files Work

### `main.py`

Runs the full workflow.

It reads the data, calculates metrics, generates alerts, and creates the report.

### `ingestion.py`

Handles input data.

It reads CSV files, reads JSON files, and converts Shopify-style data into the format the rest of the project expects.

### `metrics.py`

Handles the calculations.

This is where revenue, ad spend, ROAS, failed order rate, and pending fulfillment are calculated.

### `alerts.py`

Handles the decision logic.

It checks the metrics and decides if something needs attention.

### `reporting.py`

Handles the output.

It creates the daily CSV report.

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

## How To Run It

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

Install requirements:

```bash
pip install -r requirements.txt
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

## Design Notes

I separated the project into small files because each part has a different job.

For example:

- `ingestion.py` only cares about where the data comes from
- `metrics.py` only cares about calculations
- `alerts.py` only cares about detecting problems
- `reporting.py` only cares about creating output

This makes the project easier to change later.

For example, I started with CSV files, then added fake Shopify JSON data without changing the metrics or alerts logic.

That is the main idea of this project: the input source can change, but the business logic can stay reusable.

---

## Tech Used

- Python
- CSV
- JSON
- Git
- GitHub

---

## Future Improvements

Things I want to add later:

- fake Meta Ads API data
- supplier or warehouse data
- better report formatting
- email alerts
- webhook alerts
- scheduled automation
- Google Sheets export
- Streamlit dashboard
- PostgreSQL
- Docker
- GitHub Actions

---

## Author

Adriana Palushi Tortja