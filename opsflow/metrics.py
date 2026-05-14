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


def calculate_meta_ads_metrics(meta_ads_data):
    """
    Calculate performance metrics from fake Meta Ads API data.
    """
    total_spend = 0
    total_revenue = 0
    total_clicks = 0
    total_conversions = 0

    for campaign in meta_ads_data:
        total_spend += float(campaign["spend"])
        total_revenue += float(campaign["revenue"])
        total_clicks += int(campaign["clicks"])
        total_conversions += int(campaign["conversions"])

    roas = total_revenue / total_spend if total_spend > 0 else 0
    conversion_rate = total_conversions / total_clicks if total_clicks > 0 else 0

    return {
        "total_meta_spend": total_spend,
        "total_meta_revenue": total_revenue,
        "meta_roas": roas,
        "total_clicks": total_clicks,
        "total_conversions": total_conversions,
        "conversion_rate": conversion_rate,
    }