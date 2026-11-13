"""Compute a small report from sleep hours."""

from dataclasses import dataclass
from statistics import mean


@dataclass
class Report:
    nights: int
    average: float
    shortest: float
    longest: float
    below_goal: int


def make_report(hours: list[float], goal: float) -> Report:
    """Summarise a list of sleep hours against a nightly goal."""

    return Report(
        nights=len(hours),
        average=round(mean(hours), 2),
        shortest=min(hours),
        longest=max(hours),
        below_goal=sum(1 for h in hours if h < goal),
    )