from fastapi import FastAPI
from models import *
from typing_extensions import TypedDict
from db import temp_db
from typing import Optional, List
import uvicorn

app = FastAPI()


@app.get("/")
def hello():
    return "Hello, user!"


@app.post("/create_task")
def create_task(task: Task):
    temp_db.append(task)

    return {"status": 200, "data": task}


@app.put("/update_task/{task_id}")
def update_task(task_id: int, task: TaskDefault):
    for task in temp_db:
        if task["task_id"] == task_id:
            task["title"] = task["title"]
            task["description"] = task["description"]
            task["deadline"] = task["deadline"]
            task["priority"] = task["priority"]
            task["time_spent"] = task["time_spent"]
            return {"status": 200, "data": task}
    else:
        return {"status": 404, "data": "Task not found"}


@app.delete("/delete_task/{task_id}")
def delete_task(task_id: int):
    for task in temp_db:
        if task["task_id"] == task_id:
            temp_db.remove(task)
            return {"status": 200, "data": "Task deleted"}
    else:
        return {"status": 404, "data": "Task not found"}


@app.get("/tasks")
def get_tasks():
    return temp_db


@app.get("/task/{task_id}")
def get_task(task_id: int):
    for task in temp_db:
        if task["task_id"] == task_id:
            return task
    return {"status": 404, "data": "Task not found"}


@app.get("/tasks/{task_id}/time")
def get_task_time(task_id: int):
    for task in temp_db:
        if task["task_id"] == task_id:
            return task["time_spent"]
    return {"status": 404, "data": "Task not found"}


@app.put("/tasks/{task_id}/time")
def track_time_spent(task_id: int, time_spent: int):
    for task in temp_db:
        if task["task_id"] == task_id:
            task["time_spent"] = time_spent
            return {"status": 200, "data": task}
    return {"status": 404, "data": task}
