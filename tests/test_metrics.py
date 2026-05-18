from opsflow.metrics import (
    calculate_metrics,
    calculate_meta_ads_metrics,
    calculate_supplier_metrics,
)


def test_calculate_metrics_returns_correct_values():
    orders = [
        {
            "revenue": "100",
            "status": "completed",
            "fulfillment_status": "fulfilled",
        },
        {
            "revenue": "200",
            "status": "failed",
            "fulfillment_status": "pending",
        },
    ]

    ads = [
        {"spend": "50"},
        {"spend": "100"},
    ]

    result = calculate_metrics(orders, ads)

    assert result["total_revenue"] == 300
    assert result["total_ad_spend"] == 150
    assert result["roas"] == 2
    assert result["failed_order_rate"] == 0.5
    assert result["pending_fulfillment"] == 1


def test_calculate_metrics_handles_zero_ad_spend():
    orders = [
        {
            "revenue": "100",
            "status": "completed",
            "fulfillment_status": "fulfilled",
        }
    ]

    ads = [
        {"spend": "0"},
    ]

    result = calculate_metrics(orders, ads)

    assert result["total_revenue"] == 100
    assert result["total_ad_spend"] == 0
    assert result["roas"] == 0


def test_calculate_meta_ads_metrics_returns_correct_values():
    meta_ads_data = [
        {
            "spend": "100",
            "revenue": "300",
            "clicks": "1000",
            "conversions": "20",
        },
        {
            "spend": "200",
            "revenue": "500",
            "clicks": "1500",
            "conversions": "30",
        },
    ]

    result = calculate_meta_ads_metrics(meta_ads_data)

    assert result["total_meta_spend"] == 300
    assert result["total_meta_revenue"] == 800
    assert result["meta_roas"] == 800 / 300
    assert result["total_clicks"] == 2500
    assert result["total_conversions"] == 50
    assert result["conversion_rate"] == 50 / 2500


def test_calculate_supplier_metrics_returns_correct_values():
    supplier_status_data = [
        {
            "total_orders": "100",
            "orders_delayed": "10",
            "orders_pending": "20",
            "average_delay_days": "2",
        },
        {
            "total_orders": "200",
            "orders_delayed": "30",
            "orders_pending": "40",
            "average_delay_days": "4",
        },
    ]

    result = calculate_supplier_metrics(supplier_status_data)

    assert result["total_supplier_orders"] == 300
    assert result["total_delayed_orders"] == 40
    assert result["total_pending_supplier_orders"] == 60
    assert result["supplier_delay_rate"] == 40 / 300
    assert result["average_supplier_delay_days"] == 3