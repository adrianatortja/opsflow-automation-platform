import csv


def format_currency(value):
    return f"${value:.2f}"


def format_percentage(value):
    return f"{value * 100:.2f}%"


def format_days(value):
    return f"{value:.2f} days"


def format_number(value):
    if isinstance(value, int):
        return value

    if isinstance(value, float):
        return f"{value:.2f}"

    return value


def format_report_value(metric_name, value):
    metric_name_lower = metric_name.lower()

    if "revenue" in metric_name_lower or "spend" in metric_name_lower:
        return format_currency(value)

    if "delay days" in metric_name_lower:
        return format_days(value)

    if "roas" in metric_name_lower:
        return f"{value:.2f}"

    if "rate" in metric_name_lower:
        return format_percentage(value)

    return format_number(value)


def write_metric_row(writer, section, metric_name, value):
    formatted_value = format_report_value(metric_name, value)
    writer.writerow([section, metric_name, formatted_value])


def export_daily_report(
    metrics,
    alerts,
    meta_ads_metrics,
    meta_ads_alerts,
    supplier_metrics,
    supplier_alerts,
    output_file
):
    with open(output_file, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)

        writer.writerow(["Section", "Metric", "Value"])

        write_metric_row(writer, "Operations", "Total Revenue", metrics["total_revenue"])
        write_metric_row(writer, "Operations", "Total Ad Spend", metrics["total_ad_spend"])
        write_metric_row(writer, "Operations", "ROAS", metrics["roas"])
        write_metric_row(writer, "Operations", "Failed Order Rate", metrics["failed_order_rate"])
        write_metric_row(writer, "Operations", "Pending Fulfillment", metrics["pending_fulfillment"])

        writer.writerow([])

        write_metric_row(writer, "Meta Ads", "Total Meta Spend", meta_ads_metrics["total_meta_spend"])
        write_metric_row(writer, "Meta Ads", "Total Meta Revenue", meta_ads_metrics["total_meta_revenue"])
        write_metric_row(writer, "Meta Ads", "Meta ROAS", meta_ads_metrics["meta_roas"])
        write_metric_row(writer, "Meta Ads", "Total Clicks", meta_ads_metrics["total_clicks"])
        write_metric_row(writer, "Meta Ads", "Total Conversions", meta_ads_metrics["total_conversions"])
        write_metric_row(writer, "Meta Ads", "Conversion Rate", meta_ads_metrics["conversion_rate"])

        writer.writerow([])

        write_metric_row(writer, "Supplier", "Total Supplier Orders", supplier_metrics["total_supplier_orders"])
        write_metric_row(writer, "Supplier", "Total Delayed Orders", supplier_metrics["total_delayed_orders"])
        write_metric_row(writer, "Supplier", "Total Pending Supplier Orders", supplier_metrics["total_pending_supplier_orders"])
        write_metric_row(writer, "Supplier", "Supplier Delay Rate", supplier_metrics["supplier_delay_rate"])
        write_metric_row(writer, "Supplier", "Average Supplier Delay Days", supplier_metrics["average_supplier_delay_days"])

        writer.writerow([])

        writer.writerow(["Section", "Alert"])

        for alert in alerts:
            writer.writerow(["Operations", alert])

        for alert in meta_ads_alerts:
            writer.writerow(["Meta Ads", alert])

        for alert in supplier_alerts:
            writer.writerow(["Supplier", alert])