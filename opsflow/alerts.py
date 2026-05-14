def generate_alerts(metrics):
    alerts = []

    if metrics["failed_order_rate"] > 0.10:
        alerts.append("High failed order rate detected")

    if metrics["roas"] < 1.5:
        alerts.append("Low ROAS detected")

    if metrics["pending_fulfillment"] > 20:
        alerts.append("Fulfillment backlog detected")

    return alerts

def generate_meta_ads_alerts(meta_ads_metrics):
    """
    Generate alerts based on Meta Ads performance metrics.
    """
    alerts = []

    if meta_ads_metrics["meta_roas"] < 1.5:
        alerts.append("Meta Ads ROAS is too low")

    if meta_ads_metrics["conversion_rate"] < 0.02:
        alerts.append("Meta Ads conversion rate is too low")

    if meta_ads_metrics["total_meta_spend"] > 1000:
        alerts.append("Meta Ads spend is unusually high")

    return alerts