from datetime import datetime, timedelta

def create_timeline(tasks, start_date):

    start = datetime.strptime(start_date, "%Y-%m-%d")

    timeline = []

    for i, task in enumerate(tasks):

        task_start = start + timedelta(days=i*2)
        task_end = task_start + timedelta(days=2)

        timeline.append({
            "task": task,
            "start": task_start.strftime("%Y-%m-%d"),
            "end": task_end.strftime("%Y-%m-%d")
        })

    return timeline