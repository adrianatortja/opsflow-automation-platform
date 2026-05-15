def build_alert_message(alerts, meta_ads_alerts, supplier_alerts):
    total_alerts = len(alerts) + len(meta_ads_alerts) + len(supplier_alerts)

    if total_alerts == 0:
        return "✅ OpsFlow Alert\n\nAll systems healthy. No alerts detected."

    message_lines = [
        "🚨 OpsFlow Alert",
        "",
        f"Total Alerts: {total_alerts}",
        "",
    ]

    if alerts:
        message_lines.append("Operations:")
        for alert in alerts:
            message_lines.append(f"- {alert}")
        message_lines.append("")

    if meta_ads_alerts:
        message_lines.append("Meta Ads:")
        for alert in meta_ads_alerts:
            message_lines.append(f"- {alert}")
        message_lines.append("")

    if supplier_alerts:
        message_lines.append("Supplier:")
        for alert in supplier_alerts:
            message_lines.append(f"- {alert}")
        message_lines.append("")

    return "\n".join(message_lines)


def send_slack_style_notification(message):
    print("\n--- Slack-style Notification ---")
    print(message)
    print("--- End Notification ---")