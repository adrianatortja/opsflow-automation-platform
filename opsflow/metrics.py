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
 
    
def calculate_supplier_metrics(supplier_status_data):
    """
    Calculate supplier health metrics from fake supplier API data.
    """
    total_supplier_orders = 0
    total_delayed_orders = 0
    total_pending_orders = 0
    total_delay_days = 0
    supplier_count = len(supplier_status_data)

    for supplier in supplier_status_data:
        total_supplier_orders += int(supplier["total_orders"])
        total_delayed_orders += int(supplier["orders_delayed"])
        total_pending_orders += int(supplier["orders_pending"])
        total_delay_days += float(supplier["average_delay_days"])

    supplier_delay_rate = (
        total_delayed_orders / total_supplier_orders
        if total_supplier_orders > 0
        else 0
    )

    average_supplier_delay_days = (
        total_delay_days / supplier_count
        if supplier_count > 0
        else 0
    )

    return {
        "total_supplier_orders": total_supplier_orders,
        "total_delayed_orders": total_delayed_orders,
        "total_pending_supplier_orders": total_pending_orders,
        "supplier_delay_rate": supplier_delay_rate,
        "average_supplier_delay_days": average_supplier_delay_days,
    }