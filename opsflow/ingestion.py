import csv
import json


def read_csv_file(file_path):
    """
    Read a CSV file and return the rows as a list of dictionaries.
    """
    with open(file_path, mode="r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        return list(reader)


def read_json_file(file_path):
    """
    Read a JSON file and return the data.
    """
    with open(file_path, mode="r", encoding="utf-8") as file:
        return json.load(file)


def normalize_shopify_orders(shopify_orders):
    """
    Convert Shopify-style order data into the format our metrics code expects.
    """
    normalized_orders = []

    for order in shopify_orders:
        normalized_orders.append({
            "order_id": order["id"],
            "status": "completed" if order["financial_status"] == "paid" else "failed",
            "revenue": order["total_price"],
            "fulfillment_status": order["fulfillment_status"],
        })

    return normalized_orders

def fetch_meta_ads_data(file_path):
    """
    Simulate fetching Meta Ads data from an API.

    In a real integration, this function would send an HTTP request
    to the Meta Ads API and receive JSON data back.

    For now, we read from a local JSON file so we can practice
    the same integration pattern safely.
    """
    try:
        return read_json_file(file_path)
    except FileNotFoundError:
        print(f"Error: Meta Ads data file not found: {file_path}")
        return []

def fetch_supplier_status_data(file_path):
    """
    Simulate fetching supplier status data from an API.

    In a real technical operations workflow, this could come from
    a supplier portal, warehouse system, fulfillment API, or ERP system.

    For now, we read from a local JSON file so we can practice
    the same API-style integration pattern safely.
    """
    try:
        return read_json_file(file_path)
    except FileNotFoundError:
        print(f"Error: Supplier status data file not found: {file_path}")
        return []