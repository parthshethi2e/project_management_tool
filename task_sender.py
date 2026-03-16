from email_service import send_email
from employee_service import get_employee_by_email


def format_tasks(project_name, developer_name, summary, timeline):

    completion_date = timeline[-1]["end"]
    total_tasks = len(timeline)

    html = f"""
    <h2>Project Assignment</h2>

    <p>Hello <b>{developer_name}</b>,</p>

    <p>You have been assigned tasks for the project.</p>

    <p>
    <b>Project Name:</b> {project_name}<br>
    <b>Project Summary:</b> {summary}<br>
    <b>Estimated Completion:</b> {completion_date}<br>
    <b>Total Tasks:</b> {total_tasks}
    </p>

    <h3>Task Timeline</h3>

    <table border="1" cellpadding="8" cellspacing="0" style="border-collapse: collapse;">
        <tr style="background-color:#f2f2f2;">
            <th>Task</th>
            <th>Start</th>
            <th>End</th>
        </tr>
    """

    for task in timeline:

        html += f"""
        <tr>
            <td>{task['task']}</td>
            <td>{task['start']}</td>
            <td>{task['end']}</td>
        </tr>
        """

    html += """
    </table>

    <p>
    Please begin development according to the schedule.
    </p>

    <p>
    Regards,<br>
    <b>AI Project Manager</b>
    </p>
    """

    return html


def send_tasks(project_name, summary,
               android_tasks, ios_tasks, web_tasks,
               android_email, ios_email, web_email):

    # Get developer names from database
    android_name = get_employee_by_email(android_email)
    ios_name = get_employee_by_email(ios_email)
    web_name = get_employee_by_email(web_email)

    # Send Android tasks
    send_email(
        android_email,
        f"Project Assignment – {project_name}",
        format_tasks(project_name, android_name, summary, android_tasks)
    )

    # Send iOS tasks
    send_email(
        ios_email,
        f"Project Assignment – {project_name}",
        format_tasks(project_name, ios_name, summary, ios_tasks)
    )

    # Send Web tasks
    send_email(
        web_email,
        f"Project Assignment – {project_name}",
        format_tasks(project_name, web_name, summary, web_tasks)
    )