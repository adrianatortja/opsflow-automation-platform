from opsflow.ingestion import read_csv_file, read_json_file, normalize_shopify_orders
from opsflow.metrics import calculate_metrics
from opsflow.alerts import generate_alerts
from opsflow.reporting import export_daily_report


shopify_orders = read_json_file("data/fake_shopify_orders.json")
orders = normalize_shopify_orders(shopify_orders)
ads = read_csv_file("data/ads.csv")

metrics = calculate_metrics(orders, ads)
alerts = generate_alerts(metrics)

export_daily_report(
    metrics,
    alerts,
    "reports/daily_ops_report.csv"
)

print("Daily operations metrics:")
print(metrics)

print("\nAlerts:")
print(alerts)