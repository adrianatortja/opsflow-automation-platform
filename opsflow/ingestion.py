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