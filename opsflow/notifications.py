def get_alert_severity(alert):
    alert_lower = alert.lower()

    if "failed order" in alert_lower:
        return "HIGH"

    if "low roas" in alert_lower:
        return "HIGH"

    if "conversion rate" in alert_lower:
        return "MEDIUM"

    if "supplier delay" in alert_lower:
        return "HIGH"

    if "backlog" in alert_lower:
        return "HIGH"

    return "LOW"


def get_recommended_action(alert):
    alert_lower = alert.lower()

    if "failed order" in alert_lower:
        return "Check failed orders and review payment, inventory, or fulfillment issues."

    if "low roas" in alert_lower:
        return "Review ad spend, campaign performance, and revenue from paid traffic."

    if "conversion rate" in alert_lower:
        return "Check landing pages, ad targeting, and checkout flow for conversion problems."

    if "supplier delay" in alert_lower:
        return "Contact the supplier and review delayed purchase orders."

    if "backlog" in alert_lower:
        return "Prioritize pending supplier orders and review fulfillment capacity."

    return "Review this alert and investigate the related workflow."


def count_alerts_by_severity(alerts, meta_ads_alerts, supplier_alerts):
    severity_counts = {
        "HIGH": 0,
        "MEDIUM": 0,
        "LOW": 0,
    }

    all_alerts = alerts + meta_ads_alerts + supplier_alerts

    for alert in all_alerts:
        severity = get_alert_severity(alert)
        severity_counts[severity] += 1

    return severity_counts


def build_alert_message(alerts, meta_ads_alerts, supplier_alerts):
    total_alerts = len(alerts) + len(meta_ads_alerts) + len(supplier_alerts)
    severity_counts = count_alerts_by_severity(
        alerts,
        meta_ads_alerts,
        supplier_alerts,
    )

    if total_alerts == 0:
        return "✅ OpsFlow Alert\n\nAll systems healthy. No alerts detected."

    message_lines = [
        "🚨 OpsFlow Alert",
        "",
        f"Total Alerts: {total_alerts}",
        f"High Severity: {severity_counts['HIGH']}",
        f"Medium Severity: {severity_counts['MEDIUM']}",
        f"Low Severity: {severity_counts['LOW']}",
        "",
    ]

    if alerts:
        message_lines.append("Operations:")
        for alert in alerts:
            severity = get_alert_severity(alert)
            action = get_recommended_action(alert)
            message_lines.append(f"- {severity}: {alert}")
            message_lines.append(f"  Action: {action}")
        message_lines.append("")

    if meta_ads_alerts:
        message_lines.append("Meta Ads:")
        for alert in meta_ads_alerts:
            severity = get_alert_severity(alert)
            action = get_recommended_action(alert)
            message_lines.append(f"- {severity}: {alert}")
            message_lines.append(f"  Action: {action}")
        message_lines.append("")

    if supplier_alerts:
        message_lines.append("Supplier:")
        for alert in supplier_alerts:
            severity = get_alert_severity(alert)
            action = get_recommended_action(alert)
            message_lines.append(f"- {severity}: {alert}")
            message_lines.append(f"  Action: {action}")
        message_lines.append("")

    return "\n".join(message_lines)


def send_slack_style_notification(message):
    print("\n--- Slack-style Notification ---")
    print(message)
    print("--- End Notification ---")