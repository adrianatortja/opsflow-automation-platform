import csv


def export_daily_report(metrics, alerts, meta_ads_metrics, meta_ads_alerts, output_file):
    with open(output_file, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)

        writer.writerow(["Section", "Metric", "Value"])

        writer.writerow(["Operations", "Total Revenue", metrics["total_revenue"]])
        writer.writerow(["Operations", "Total Ad Spend", metrics["total_ad_spend"]])
        writer.writerow(["Operations", "ROAS", metrics["roas"]])
        writer.writerow(["Operations", "Failed Order Rate", metrics["failed_order_rate"]])
        writer.writerow(["Operations", "Pending Fulfillment", metrics["pending_fulfillment"]])

        writer.writerow([])

        writer.writerow(["Meta Ads", "Total Meta Spend", meta_ads_metrics["total_meta_spend"]])
        writer.writerow(["Meta Ads", "Total Meta Revenue", meta_ads_metrics["total_meta_revenue"]])
        writer.writerow(["Meta Ads", "Meta ROAS", meta_ads_metrics["meta_roas"]])
        writer.writerow(["Meta Ads", "Total Clicks", meta_ads_metrics["total_clicks"]])
        writer.writerow(["Meta Ads", "Total Conversions", meta_ads_metrics["total_conversions"]])
        writer.writerow(["Meta Ads", "Conversion Rate", meta_ads_metrics["conversion_rate"]])

        writer.writerow([])

        writer.writerow(["Section", "Alert"])

        for alert in alerts:
            writer.writerow(["Operations", alert])

        for alert in meta_ads_alerts:
            writer.writerow(["Meta Ads", alert])