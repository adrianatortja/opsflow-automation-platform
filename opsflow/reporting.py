import csv


def export_daily_report(metrics, alerts, output_file):
    with open(output_file, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)

        writer.writerow(["Metric", "Value"])

        writer.writerow(["Total Revenue", metrics["total_revenue"]])
        writer.writerow(["Total Ad Spend", metrics["total_ad_spend"]])
        writer.writerow(["ROAS", metrics["roas"]])
        writer.writerow(["Failed Order Rate", metrics["failed_order_rate"]])
        writer.writerow(["Pending Fulfillment", metrics["pending_fulfillment"]])

        writer.writerow([])

        writer.writerow(["Alerts"])

        for alert in alerts:
            writer.writerow([alert])