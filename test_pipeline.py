"""tests/test_pipeline.py -- Dummy tests for Healthcare pipeline."""

from pipeline import extract, transform, load, run


def test_extract_returns_list():
    assert isinstance(extract(), list)


def test_extract_not_empty():
    assert len(extract()) > 0


def test_transform_removes_rejected():
    data = [
        {"id": 1, "patient": "A", "amount": 100, "status": "rejected"},
        {"id": 2, "patient": "B", "amount": 200, "status": "approved"},
    ]
    assert all(c["status"] != "rejected" for c in transform(data))


def test_transform_fills_null_amount():
    data = [{"id": 1, "patient": "A", "amount": None, "status": "pending"}]
    assert transform(data)[0]["amount"] == 0


def test_load_returns_list():
    assert isinstance(load([]), list)


def test_load_passes_data_through():
    data = [{"id": 1, "patient": "A", "amount": 100, "status": "approved"}]
    assert load(data) == data


def test_run_returns_list():
    assert isinstance(run(), list)


def test_run_no_rejected():
    assert all(c["status"] != "rejected" for c in run())


def test_run_no_null_amounts():
    assert all(c["amount"] is not None for c in run())
