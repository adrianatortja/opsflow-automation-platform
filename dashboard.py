import pandas as pd
import streamlit as st

from opsflow.pipeline import get_opsflow_dashboard_data


st.set_page_config(
    page_title="OpsFlow Dashboard",
    page_icon="📊",
    layout="wide",
)

data = get_opsflow_dashboard_data()

metrics = data["metrics"]
meta_ads_metrics = data["meta_ads_metrics"]
supplier_metrics = data["supplier_metrics"]

alerts = data["alerts"]
meta_ads_alerts = data["meta_ads_alerts"]
supplier_alerts = data["supplier_alerts"]
total_alerts = data["total_alerts"]

st.title("OpsFlow Automation Dashboard")

st.write(
    "A Python dashboard for monitoring ecommerce operations, ad performance, "
    "supplier health, and operational alerts."
)

st.sidebar.title("OpsFlow Summary")
st.sidebar.metric("Total Alerts", total_alerts)
st.sidebar.metric("ROAS", f"{metrics['roas']:.2f}")
st.sidebar.metric("Failed Order Rate", f"{metrics['failed_order_rate']:.1%}")
st.sidebar.metric("Supplier Delay Rate", f"{supplier_metrics['supplier_delay_rate']:.1%}")

if total_alerts > 0:
    st.sidebar.warning("Action needed today")
else:
    st.sidebar.success("Operations look healthy")

st.divider()

st.subheader("Operations KPIs")

col1, col2, col3, col4, col5 = st.columns(5)

col1.metric("Total Revenue", f"${metrics['total_revenue']:.2f}")
col2.metric("Total Ad Spend", f"${metrics['total_ad_spend']:.2f}")
col3.metric("ROAS", f"{metrics['roas']:.2f}")
col4.metric("Failed Order Rate", f"{metrics['failed_order_rate']:.1%}")
col5.metric("Pending Fulfillment", metrics["pending_fulfillment"])

operations_chart_data = pd.DataFrame(
    {
        "Metric": ["Revenue", "Ad Spend", "Pending Fulfillment"],
        "Value": [
            metrics["total_revenue"],
            metrics["total_ad_spend"],
            metrics["pending_fulfillment"],
        ],
    }
)

st.bar_chart(
    operations_chart_data,
    x="Metric",
    y="Value",
)

st.divider()

st.subheader("Alert Summary")

alert_col1, alert_col2, alert_col3, alert_col4 = st.columns(4)

alert_col1.metric("Total Alerts", total_alerts)
alert_col2.metric("Operations Alerts", len(alerts))
alert_col3.metric("Meta Ads Alerts", len(meta_ads_alerts))
alert_col4.metric("Supplier Alerts", len(supplier_alerts))

st.subheader("Alerts")

if total_alerts == 0:
    st.success("No alerts. Operations look healthy.")
else:
    if alerts:
        st.markdown("**Operations**")
        for alert in alerts:
            st.error(alert)

    if meta_ads_alerts:
        st.markdown("**Meta Ads**")
        for alert in meta_ads_alerts:
            st.warning(alert)

    if supplier_alerts:
        st.markdown("**Supplier**")
        for alert in supplier_alerts:
            st.warning(alert)

st.divider()

st.subheader("Meta Ads Performance")

meta_col1, meta_col2, meta_col3, meta_col4 = st.columns(4)

meta_col1.metric("Meta Spend", f"${meta_ads_metrics['total_meta_spend']:.2f}")
meta_col2.metric("Meta Revenue", f"${meta_ads_metrics['total_meta_revenue']:.2f}")
meta_col3.metric("Meta ROAS", f"{meta_ads_metrics['meta_roas']:.2f}")
meta_col4.metric("Conversion Rate", f"{meta_ads_metrics['conversion_rate']:.1%}")

meta_chart_data = pd.DataFrame(
    {
        "Metric": ["Meta Spend", "Meta Revenue"],
        "Value": [
            meta_ads_metrics["total_meta_spend"],
            meta_ads_metrics["total_meta_revenue"],
        ],
    }
)

st.bar_chart(
    meta_chart_data,
    x="Metric",
    y="Value",
)

st.divider()

st.subheader("Supplier Health")

supplier_col1, supplier_col2, supplier_col3, supplier_col4 = st.columns(4)

supplier_col1.metric("Supplier Orders", supplier_metrics["total_supplier_orders"])
supplier_col2.metric("Delayed Orders", supplier_metrics["total_delayed_orders"])
supplier_col3.metric(
    "Supplier Delay Rate",
    f"{supplier_metrics['supplier_delay_rate']:.1%}",
)
supplier_col4.metric(
    "Pending Supplier Orders",
    supplier_metrics["total_pending_supplier_orders"],
)

supplier_col5, supplier_col6 = st.columns(2)

supplier_col5.metric(
    "Average Supplier Delay Days",
    f"{supplier_metrics['average_supplier_delay_days']:.1f}",
)

supplier_chart_data = pd.DataFrame(
    {
        "Metric": ["Supplier Orders", "Delayed Orders", "Pending Orders"],
        "Value": [
            supplier_metrics["total_supplier_orders"],
            supplier_metrics["total_delayed_orders"],
            supplier_metrics["total_pending_supplier_orders"],
        ],
    }
)

st.bar_chart(
    supplier_chart_data,
    x="Metric",
    y="Value",
)