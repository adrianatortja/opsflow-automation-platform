# OpsFlow Automation Platform

Python automation platform for ecommerce operations, ad performance tracking, alerts, and reporting workflows.

---

## Overview

OpsFlow is a Python-first automation project designed to simulate real technical operations workflows in an ecommerce environment.

The goal is to automate repetitive operational work such as data ingestion, metric calculations, issue detection, and report generation.

This project follows a simple automation architecture:

```text
input → processing → decision → output
```

Example workflow:

```text
orders data + ad spend data
→ calculate metrics
→ detect business problems
→ generate alerts
→ export report
```

---

## Why This Project Exists

OpsFlow was built as a portfolio project for Technical Operations / Automation roles.

It reflects the type of work involved in operations teams that support ecommerce, performance marketing, fulfillment, and reporting workflows.

This includes:

- automating repetitive reporting tasks
- processing operational data
- detecting business issues automatically
- building internal tooling
- integrating multiple data sources
- generating actionable reports

---

## Current Features

### Data Ingestion

Supports:

- CSV ecommerce orders
- CSV ad campaign spend
- fake Shopify-style JSON API data

### Data Normalization

Converts external Shopify-style data into a consistent internal structure for processing.

### Business Metrics

Calculates:

- Total Revenue
- Total Ad Spend
- ROAS (Return on Ad Spend)
- Failed Order Rate
- Pending Fulfillment Count

### Alert Engine

Detects operational problems such as:

- Failed order rate > 10%
- ROAS < 1.5
- Fulfillment backlog > 20 pending orders

### Reporting

Generates:

- Daily operations report
- CSV export for reporting workflows

---

## Project Architecture

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

## File Responsibilities

### `main.py`

Controls the full automation workflow.

Responsibilities:

- load data
- trigger metric calculations
- trigger alerts
- generate reports

---

### `ingestion.py`

Handles data input.

Responsibilities:

- read CSV files
- read JSON files
- normalize external API-style data

---

### `metrics.py`

Handles business calculations.

Responsibilities:

- total revenue
- total ad spend
- ROAS
- failed order rate
- pending fulfillment count

---

### `alerts.py`

Handles decision logic.

Responsibilities:

- detect operational issues
- generate alert messages

---

### `reporting.py`

Handles output generation.

Responsibilities:

- export CSV reports

---

## Example Output

### Metrics

```python
{
    'total_revenue': 415.0,
    'total_ad_spend': 650.0,
    'roas': 0.6384615384615384,
    'failed_order_rate': 0.4,
    'pending_fulfillment': 2
}
```

### Alerts

```python
[
    'High failed order rate detected',
    'Low ROAS detected'
]
```

---

## How to Run

### Clone Repository

```bash
git clone https://github.com/adrianatortja/opsflow-automation-platform.git
cd opsflow-automation-platform
```

---

### Create Virtual Environment

Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

---

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

### Run Automation Workflow

```bash
python main.py
```

---

### Generated Output

Report will be created here:

```text
reports/daily_ops_report.csv
```

---

## Skills Demonstrated

This project demonstrates:

### Python Automation

- Python scripting
- file processing
- workflow orchestration

### Data Processing

- CSV parsing
- JSON parsing
- data transformation
- data normalization

### Business Logic

- KPI calculation
- alert thresholds
- decision logic

### Technical Operations Thinking

- automation workflow design
- operational monitoring
- reporting automation
- modular internal tooling architecture

---

## Interview Explanation

Simple explanation:

> OpsFlow automates operational reporting by ingesting business data, calculating KPIs, detecting issues, and generating actionable reports.

Non-technical explanation:

> Instead of manually checking spreadsheets every day, this system automatically analyzes operational data and highlights problems that need attention.

CEO explanation:

> OpsFlow helps teams make faster operational decisions by automatically turning raw business data into reports and alerts.

---

## Future Improvements

Planned upgrades:

- fake Meta Ads API integration
- supplier / warehouse API simulation
- PostgreSQL database integration
- Streamlit dashboard
- scheduled jobs with APScheduler
- Celery task automation
- email alerts
- webhook notifications
- Google Sheets export
- Docker
- GitHub Actions CI/CD
- deployment

---

## Tech Stack

- Python
- CSV
- JSON
- Modular Python Architecture
- Git
- GitHub

---

## Author

Adriana Palushi Tortja

Backend developer building automation and technical operations tooling with Python.