from opsflow import database


def test_create_tables_creates_pipeline_runs_table(tmp_path, monkeypatch):
    test_db_path = tmp_path / "test_opsflow_history.db"

    monkeypatch.setattr(database, "DATABASE_PATH", test_db_path)

    database.create_tables()

    connection = database.get_connection()
    cursor = connection.cursor()

    cursor.execute(
        """
        SELECT name
        FROM sqlite_master
        WHERE type='table' AND name='pipeline_runs'
        """
    )

    table = cursor.fetchone()

    connection.close()

    assert table is not None


def test_save_pipeline_run_saves_data_correctly(tmp_path, monkeypatch):
    test_db_path = tmp_path / "test_opsflow_history.db"

    monkeypatch.setattr(database, "DATABASE_PATH", test_db_path)

    database.create_tables()

    operations_metrics = {
        "total_revenue": 500.0,
        "total_ad_spend": 250.0,
        "roas": 2.0,
        "failed_order_rate": 0.1,
        "pending_fulfillment": 5,
    }

    meta_ads_metrics = {
        "meta_roas": 1.8,
        "conversion_rate": 0.03,
    }

    supplier_metrics = {
        "supplier_delay_rate": 0.05,
    }

    database.save_pipeline_run(
        run_date="2026-05-18",
        operations_metrics=operations_metrics,
        meta_ads_metrics=meta_ads_metrics,
        supplier_metrics=supplier_metrics,
        total_alerts=2,
        run_datetime="2026-05-18 13:30:00",
    )

    history = database.get_pipeline_history()

    assert len(history) == 1

    saved_run = history[0]

    assert saved_run[1] == "2026-05-18"
    assert saved_run[2] == 500.0
    assert saved_run[3] == 250.0
    assert saved_run[4] == 2.0
    assert saved_run[5] == 0.1
    assert saved_run[6] == 5
    assert saved_run[7] == 1.8
    assert saved_run[8] == 0.03
    assert saved_run[9] == 0.05
    assert saved_run[10] == 2
    assert saved_run[11] == "2026-05-18 13:30:00"


def test_get_pipeline_history_returns_empty_list_when_no_runs_exist(
    tmp_path, monkeypatch
):
    test_db_path = tmp_path / "test_opsflow_history.db"

    monkeypatch.setattr(database, "DATABASE_PATH", test_db_path)

    database.create_tables()

    history = database.get_pipeline_history()

    assert history == []