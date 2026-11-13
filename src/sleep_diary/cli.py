"""command-line interface: sleep-diary add | report."""

from pathlib import Path

import typer

from sleep_diary.stats import make_report
from sleep_diary.storage import add_record, load_records

app = typer.Typer(help="Log your sleep and see how you are doing.")
DATA = typer.Option(Path("sleep.csv"), help="CSV file with your records.")
GOAL = typer.Option(8.0, help="Target hours of sleep per night.")   

@app.command() 
def add(hours: float, data: Path = DATA) -> None:
    """Record last night's sleep, e.g. `sleep-diary add 7.5`."""
    add_record(data, hours)
    typer.echo(f"Saved {hours} h to {data}")

@app.command()
def report(data: Path = DATA, goal: float = GOAL) -> None:
    """Show average, shortest, longest and nights below the goal."""
    records = load_records(data)
    if not records:
        typer.echo("No records yet. Try: sleep-diary add 7.5")
        raise typer.Exit(code=1)
    r = make_report([h for _, h in records], goal)
    typer.echo(f"Nights:      {r.nights}")
    typer.echo(f"Average:     {r.average} h (goal {goal} h)")
    typer.echo(f"Shortest:    {r.shortest} h")
    typer.echo(f"Longest:     {r.longest} h")
    typer.echo(f"Below goal:  {r.below_goal} night(s)")