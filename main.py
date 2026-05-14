from opsflow.ingestion import read_csv_file, read_json_file, normalize_shopify_orders, fetch_meta_ads_data
from opsflow.metrics import calculate_metrics, calculate_meta_ads_metrics
from opsflow.alerts import generate_alerts, generate_meta_ads_alerts
from opsflow.reporting import export_daily_report


shopify_orders = read_json_file("data/fake_shopify_orders.json")
orders = normalize_shopify_orders(shopify_orders)

ads = read_csv_file("data/ads.csv")
meta_ads_data = fetch_meta_ads_data("data/fake_meta_ads.json")

metrics = calculate_metrics(orders, ads)
meta_ads_metrics = calculate_meta_ads_metrics(meta_ads_data)

alerts = generate_alerts(metrics)
meta_ads_alerts = generate_meta_ads_alerts(meta_ads_metrics)

export_daily_report(
    metrics,
    alerts,
    meta_ads_metrics,
    meta_ads_alerts,
    "reports/daily_ops_report.csv"
)

print("Daily operations metrics:")
print(metrics)

print("\nAlerts:")
print(alerts)

print("\nMeta Ads metrics:")
print(meta_ads_metrics)

print("\nMeta Ads alerts:")
print(meta_ads_alerts)