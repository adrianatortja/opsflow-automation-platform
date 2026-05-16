import streamlit as st


st.set_page_config(
    page_title="OpsFlow Dashboard",
    page_icon="📊",
    layout="wide",
)

st.title("OpsFlow Automation Dashboard")

st.write(
    "A Python dashboard for monitoring ecommerce operations, ad performance, "
    "supplier health, and operational alerts."
)

st.subheader("Dashboard Sections")

st.markdown(
    """
    - Operations KPIs
    - Meta Ads Performance
    - Supplier Health
    - Alerts Overview
    - Daily Report Summary
    """
)