from opsflow.ingestion import (
    read_csv_file,
    read_json_file,
    normalize_shopify_orders,
    fetch_meta_ads_data,
    fetch_supplier_status_data,
)
from opsflow.metrics import (
    calculate_metrics,
    calculate_meta_ads_metrics,
    calculate_supplier_metrics,
)
from opsflow.alerts import (
    generate_alerts,
    generate_meta_ads_alerts,
    generate_supplier_alerts,
)


def get_opsflow_dashboard_data():
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

    total_alerts = len(alerts) + len(meta_ads_alerts) + len(supplier_alerts)

    return {
        "metrics": metrics,
        "meta_ads_metrics": meta_ads_metrics,
        "supplier_metrics": supplier_metrics,
        "alerts": alerts,
        "meta_ads_alerts": meta_ads_alerts,
        "supplier_alerts": supplier_alerts,
        "total_alerts": total_alerts,
    }