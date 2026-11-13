from datetime import date

from sleep_diary.storage import add_record, load_records

def test_add_then_load(tmp_path):
    csv_file = tmp_path / "sleep.csv"

    add_record(csv_file, 7.5, day=date(2026, 11, 12))
    add_record(csv_file, 6, day=date(2026, 11, 13))

    records = load_records(csv_file)
    assert records == [("2026-11-12", 7.5), ("2026-11-13", 6.0)]

def test_load_missing_file_returns_empty_list(tmp_path):
    records = load_records(tmp_path / "nothing.csv")
    assert records == []