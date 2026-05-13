def generate_alerts(metrics):
    alerts = []

    if metrics["failed_order_rate"] > 0.10:
        alerts.append("High failed order rate detected")

    if metrics["roas"] < 1.5:
        alerts.append("Low ROAS detected")

    if metrics["pending_fulfillment"] > 20:
        alerts.append("Fulfillment backlog detected")

    return alerts