from fastapi import APIRouter
from task_sender import send_tasks
from employee_service import get_employee_by_email

router = APIRouter()

@router.post("/confirm-tasks")
def confirm_tasks(data: dict):

    android = data["android"]
    ios = data["ios"]
    web = data["web"]
    

    android_email = data["androidEmail"]
    ios_email = data["iosEmail"]
    web_email = data["webEmail"]

    project_name = data.get("projectName", "AI Project")
    summary = data.get("summary", "")


    send_tasks(
        project_name,
        summary,
        android,
        ios,
        web,
        android_email,
        ios_email,
        web_email
    )

    return {"message": "Tasks sent successfully"}