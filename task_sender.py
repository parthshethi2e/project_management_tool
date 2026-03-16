from email_service import send_email


def format_tasks(timeline):

    message = ""

    for task in timeline:

        message += f"""
Task: {task['task']}
Start: {task['start']}
End: {task['end']}

"""

    return message


def send_tasks(android_tasks, ios_tasks, web_tasks,
               android_email, ios_email, web_email):
    
    android_message = format_tasks(android_tasks)
    ios_message = format_tasks(ios_tasks)
    web_message = format_tasks(web_tasks)

    send_email(
        android_email,
        "Android Project Tasks",
        android_message
    )

    send_email(
        ios_email,
        "iOS Project Tasks",
        ios_message
    )

    send_email(
        web_email,
        "Web Project Tasks",
        web_message
    )