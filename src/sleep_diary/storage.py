"""Read and write sleep records in a CSV file."""

import csv
from datetime import date
from pathlib import Path 


FIELDS = ["date", "hours"]


def add_record(path: Path, hours: float, day: date | None = None) -> None:
    """Append one night of sleep to the CSV file (created if missing)."""
    if day is None:
        day = date.today()

    file_is_new = not path.exists()

    with path.open("a", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=FIELDS)
        if file_is_new:
            writer.writeheader()
        writer.writerow({"date": day.isoformat(), "hours": hours})


def load_records(path: Path) -> list:
    """Return all records as a list of (date, hours) pairs."""
    if not path.exists():
        return []

    records = []
    with path.open(newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            day = row["date"]
            hours = float(row["hours"]) 
            records.append((day, hours))
    return records