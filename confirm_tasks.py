from fastapi import APIRouter
from task_sender import send_tasks

router = APIRouter()

@router.post("/confirm-tasks")
def confirm_tasks(data: dict):

    android = data["android"]
    ios = data["ios"]
    web = data["web"]

    android_email = data["androidEmail"]
    ios_email = data["iosEmail"]
    web_email = data["webEmail"]

    send_tasks(
        android,
        ios,
        web,
        android_email,
        ios_email,
        web_email
    )

    return {"message": "Tasks sent successfully"}