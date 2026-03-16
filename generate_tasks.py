from fastapi import APIRouter, UploadFile, File, Form
from ai_engine import generate_tasks
from timeline_service import create_timeline
from file_parser import extract_text_from_file
import json

router = APIRouter()


@router.post("/generate-tasks")
async def generate(
    file: UploadFile = File(...),
    start_date: str = Form(...)
):

    # 1️⃣ Extract text from file
    requirement_text = extract_text_from_file(file)

    # 2️⃣ Send to AI
    tasks = generate_tasks(requirement_text)

    tasks_json = json.loads(tasks)

    # 3️⃣ Create timelines
    android_timeline = create_timeline(tasks_json["android"], start_date)
    ios_timeline = create_timeline(tasks_json["ios"], start_date)
    web_timeline = create_timeline(tasks_json["web"], start_date)

    return {
        "android": android_timeline,
        "ios": ios_timeline,
        "web": web_timeline
    }