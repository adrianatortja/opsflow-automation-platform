from opsflow.alerts import (
    generate_alerts,
    generate_meta_ads_alerts,
    generate_supplier_alerts,
)


def test_generate_alerts_returns_expected_alerts():
    metrics = {
        "failed_order_rate": 0.20,
        "roas": 1.2,
        "pending_fulfillment": 25,
    }

    result = generate_alerts(metrics)

    assert "High failed order rate detected" in result
    assert "Low ROAS detected" in result
    assert "Fulfillment backlog detected" in result


def test_generate_alerts_returns_empty_list_when_metrics_are_healthy():
    metrics = {
        "failed_order_rate": 0.05,
        "roas": 2.5,
        "pending_fulfillment": 5,
    }

    result = generate_alerts(metrics)

    assert result == []


def test_generate_meta_ads_alerts_returns_expected_alerts():
    meta_ads_metrics = {
        "meta_roas": 1.2,
        "conversion_rate": 0.01,
        "total_meta_spend": 1200,
    }

    result = generate_meta_ads_alerts(meta_ads_metrics)

    assert "Meta Ads ROAS is too low" in result
    assert "Meta Ads conversion rate is too low" in result
    assert "Meta Ads spend is unusually high" in result


def test_generate_meta_ads_alerts_returns_empty_list_when_metrics_are_healthy():
    meta_ads_metrics = {
        "meta_roas": 2.5,
        "conversion_rate": 0.05,
        "total_meta_spend": 500,
    }

    result = generate_meta_ads_alerts(meta_ads_metrics)

    assert result == []


def test_generate_supplier_alerts_returns_expected_alerts():
    supplier_metrics = {
        "supplier_delay_rate": 0.20,
        "total_pending_supplier_orders": 50,
        "average_supplier_delay_days": 4,
    }

    result = generate_supplier_alerts(supplier_metrics)

    assert "Supplier delay rate is high" in result
    assert "Supplier backlog detected" in result
    assert "Average supplier delay is too high" in result


def test_generate_supplier_alerts_returns_empty_list_when_metrics_are_healthy():
    supplier_metrics = {
        "supplier_delay_rate": 0.05,
        "total_pending_supplier_orders": 10,
        "average_supplier_delay_days": 2,
    }

    result = generate_supplier_alerts(supplier_metrics)

    assert result == []