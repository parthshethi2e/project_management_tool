from fastapi import APIRouter
from employee_service import get_employees_by_role

router = APIRouter()


@router.get("/employees")
def get_employees():

    android = get_employees_by_role("Android Developer")
    ios = get_employees_by_role("iOS Developer")
    web = get_employees_by_role("Web Developer")

    return {
        "android": android,
        "ios": ios,
        "web": web
    }