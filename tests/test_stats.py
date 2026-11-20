from sleep_diary.stats import make_report


def test_report_counts_nights_below_goal():
    hours = [7.5, 8, 6.5, 7, 8.5, 6, 7.5]

    report = make_report(hours, goal=8)

    assert report.nights == 7
    assert report.average == 7.29
    assert report.shortest == 6
    assert report.longest == 8.5
    assert report.below_goal == 5
