from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from generate_tasks import router as generate_router
from confirm_tasks import router as confirm_router
from employees_api import router as employee_router

app = FastAPI()

# CORS configuration
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=[
#         "http://localhost:3000",
#         "http://localhost:3001"
#     ],
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://project-management-tool-yclf.onrender.com"],  # later restrict to your frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(generate_router)
app.include_router(confirm_router)
app.include_router(employee_router)

@app.get("/")
def home():
    return {"message": "AI Project Management Tool Running"}