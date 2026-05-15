from datetime import datetime

from opsflow.ingestion import read_csv_file, read_json_file, normalize_shopify_orders, fetch_meta_ads_data, fetch_supplier_status_data
from opsflow.metrics import calculate_metrics, calculate_meta_ads_metrics, calculate_supplier_metrics
from opsflow.alerts import generate_alerts, generate_meta_ads_alerts, generate_supplier_alerts
from opsflow.reporting import export_daily_report


shopify_orders = read_json_file("data/fake_shopify_orders.json")
orders = normalize_shopify_orders(shopify_orders)

ads = read_csv_file("data/ads.csv")
meta_ads_data = fetch_meta_ads_data("data/fake_meta_ads.json")
supplier_status_data = fetch_supplier_status_data("data/fake_supplier_status.json")

metrics = calculate_metrics(orders, ads)
meta_ads_metrics = calculate_meta_ads_metrics(meta_ads_data)
supplier_metrics = calculate_supplier_metrics(supplier_status_data)

alerts = generate_alerts(metrics)
meta_ads_alerts = generate_meta_ads_alerts(meta_ads_metrics)
supplier_alerts = generate_supplier_alerts(supplier_metrics)

report_date = datetime.now().strftime("%Y-%m-%d")
report_file = f"reports/daily_ops_report_{report_date}.csv"

export_daily_report(
    metrics,
    alerts,
    meta_ads_metrics,
    meta_ads_alerts,
    supplier_metrics,
    supplier_alerts,
    report_file
)

print(f"Report generated: {report_file}")

print("Daily operations metrics:")
print(metrics)

print("\nAlerts:")
print(alerts)

print("\nMeta Ads metrics:")
print(meta_ads_metrics)

print("\nMeta Ads alerts:")
print(meta_ads_alerts)

print("\nSupplier metrics:")
print(supplier_metrics)

print("\nSupplier alerts:")
print(supplier_alerts)