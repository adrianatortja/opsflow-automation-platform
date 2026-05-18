import csv

from opsflow.reporting import (
    format_currency,
    format_percentage,
    format_days,
    format_number,
    format_report_value,
    get_health_status,
    export_daily_report,
)


def test_format_currency():
    assert format_currency(123.456) == "$123.46"


def test_format_percentage():
    assert format_percentage(0.1234) == "12.34%"


def test_format_days():
    assert format_days(2.5) == "2.50 days"


def test_format_number_handles_int_float_and_text():
    assert format_number(5) == 5
    assert format_number(5.678) == "5.68"
    assert format_number("test") == "test"


def test_format_report_value_formats_by_metric_name():
    assert format_report_value("Total Revenue", 100) == "$100.00"
    assert format_report_value("Total Ad Spend", 50) == "$50.00"
    assert format_report_value("ROAS", 2.345) == "2.35"
    assert format_report_value("Failed Order Rate", 0.25) == "25.00%"
    assert format_report_value("Average Supplier Delay Days", 3.5) == "3.50 days"


def test_get_health_status_returns_needs_attention_when_alerts_exist():
    alerts = ["Low ROAS detected"]

    result = get_health_status(alerts)

    assert result == "Needs Attention"


def test_get_health_status_returns_healthy_when_no_alerts_exist():
    alerts = []

    result = get_health_status(alerts)

    assert result == "Healthy"


def test_export_daily_report_creates_csv_with_expected_content(tmp_path):
    output_file = tmp_path / "daily_ops_report.csv"

    metrics = {
        "total_revenue": 500.0,
        "total_ad_spend": 250.0,
        "roas": 2.0,
        "failed_order_rate": 0.1,
        "pending_fulfillment": 5,
    }

    alerts = ["High failed order rate detected"]

    meta_ads_metrics = {
        "total_meta_spend": 300.0,
        "total_meta_revenue": 600.0,
        "meta_roas": 2.0,
        "total_clicks": 1000,
        "total_conversions": 50,
        "conversion_rate": 0.05,
    }

    meta_ads_alerts = []

    supplier_metrics = {
        "total_supplier_orders": 100,
        "total_delayed_orders": 5,
        "total_pending_supplier_orders": 10,
        "supplier_delay_rate": 0.05,
        "average_supplier_delay_days": 2.0,
    }

    supplier_alerts = ["Supplier delay rate is high"]

    export_daily_report(
        metrics=metrics,
        alerts=alerts,
        meta_ads_metrics=meta_ads_metrics,
        meta_ads_alerts=meta_ads_alerts,
        supplier_metrics=supplier_metrics,
        supplier_alerts=supplier_alerts,
        output_file=output_file,
    )

    assert output_file.exists()

    with open(output_file, mode="r", encoding="utf-8") as file:
        reader = csv.reader(file)
        rows = list(reader)

    assert ["Daily Summary"] in rows
    assert ["Total Alerts", "2"] in rows
    assert ["Overall Health", "Needs Attention"] in rows
    assert ["Operations Health", "Needs Attention"] in rows
    assert ["Meta Ads Health", "Healthy"] in rows
    assert ["Supplier Health", "Needs Attention"] in rows

    assert ["Operations", "Total Revenue", "$500.00"] in rows
    assert ["Operations", "ROAS", "2.00"] in rows
    assert ["Operations", "Failed Order Rate", "10.00%"] in rows

    assert ["Meta Ads", "Total Meta Spend", "$300.00"] in rows
    assert ["Meta Ads", "Conversion Rate", "5.00%"] in rows

    assert ["Supplier", "Average Supplier Delay Days", "2.00 days"] in rows

    assert ["Operations", "High failed order rate detected"] in rows
    assert ["Supplier", "Supplier delay rate is high"] in rows