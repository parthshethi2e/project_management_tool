from datetime import datetime, timedelta


def add_work_days(start_date, days):

    current = start_date

    while days > 0:

        current += timedelta(days=1)

        if not is_weekend(current):
            days -= 1

    return current


def create_timeline(tasks, start_date):

    start = datetime.strptime(start_date, "%Y-%m-%d")

    timeline = []

    for task in tasks:

        end = add_work_days(start, 2)

        timeline.append({
            "task": task,
            "start": start.strftime("%Y-%m-%d"),
            "end": end.strftime("%Y-%m-%d")
        })

        start = end

    return timeline

def is_weekend(date):
    return date.weekday() >= 5

def get_completion_date(timeline):

    last_task = timeline[-1]

    return last_task["end"]