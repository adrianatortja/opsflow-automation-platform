import sqlite3
from pathlib import Path


DATABASE_PATH = Path("opsflow_history.db")


def get_connection():
    """
    Create and return a connection to the SQLite database.
    If the database file does not exist, SQLite will create it automatically.
    """
    return sqlite3.connect(DATABASE_PATH)


def create_tables():
    """
    Create the database tables needed for OpsFlow history.

    Also adds new columns safely if the database already exists.
    """
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS pipeline_runs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            run_date TEXT NOT NULL,
            total_revenue REAL NOT NULL,
            total_ad_spend REAL NOT NULL,
            roas REAL NOT NULL,
            failed_order_rate REAL NOT NULL,
            pending_fulfillment INTEGER NOT NULL,
            meta_roas REAL NOT NULL,
            conversion_rate REAL NOT NULL,
            supplier_delay_rate REAL NOT NULL,
            total_alerts INTEGER NOT NULL
        )
        """
    )

    cursor.execute("PRAGMA table_info(pipeline_runs)")
    existing_columns = [column[1] for column in cursor.fetchall()]

    if "run_datetime" not in existing_columns:
        cursor.execute(
            """
            ALTER TABLE pipeline_runs
            ADD COLUMN run_datetime TEXT
            """
        )

    connection.commit()
    connection.close()


def save_pipeline_run(
    run_date,
    operations_metrics,
    meta_ads_metrics,
    supplier_metrics,
    total_alerts,
    run_datetime=None,
):
    """
    Save one OpsFlow pipeline run into the database.
    """
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        """
        INSERT INTO pipeline_runs (
            run_date,
            total_revenue,
            total_ad_spend,
            roas,
            failed_order_rate,
            pending_fulfillment,
            meta_roas,
            conversion_rate,
            supplier_delay_rate,
            total_alerts,
            run_datetime
        )
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """,
        (
            run_date,
            operations_metrics["total_revenue"],
            operations_metrics["total_ad_spend"],
            operations_metrics["roas"],
            operations_metrics["failed_order_rate"],
            operations_metrics["pending_fulfillment"],
            meta_ads_metrics["meta_roas"],
            meta_ads_metrics["conversion_rate"],
            supplier_metrics["supplier_delay_rate"],
            total_alerts,
            run_datetime,
        ),
    )

    connection.commit()
    connection.close()


def get_pipeline_history():
    """
    Return all saved OpsFlow pipeline runs from the database.
    """
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        """
        SELECT
            id,
            run_date,
            total_revenue,
            total_ad_spend,
            roas,
            failed_order_rate,
            pending_fulfillment,
            meta_roas,
            conversion_rate,
            supplier_delay_rate,
            total_alerts,
            run_datetime
        FROM pipeline_runs
        ORDER BY id ASC
        """
    )

    rows = cursor.fetchall()

    connection.close()

    return rows