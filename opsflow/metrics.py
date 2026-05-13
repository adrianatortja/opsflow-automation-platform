def calculate_metrics(orders, ads):
    total_revenue = sum(float(order["revenue"]) for order in orders)
    total_ad_spend = sum(float(ad["spend"]) for ad in ads)

    total_orders = len(orders)
    failed_orders = sum(1 for order in orders if order["status"] == "failed")
    pending_fulfillment = sum(
        1 for order in orders if order["fulfillment_status"] == "pending"
    )

    roas = total_revenue / total_ad_spend if total_ad_spend > 0 else 0
    failed_order_rate = failed_orders / total_orders if total_orders > 0 else 0

    return {
        "total_revenue": total_revenue,
        "total_ad_spend": total_ad_spend,
        "roas": roas,
        "failed_order_rate": failed_order_rate,
        "pending_fulfillment": pending_fulfillment,
    }