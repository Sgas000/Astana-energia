from fastapi import FastAPI, HTTPException
from typing import List
from models import Task
from crud import get_all_tasks, add_task, get_task_by_id, delete_task

app = FastAPI(title="Astana-Energia Technical Docs API")

@app.get("/tasks", response_model=List[Task])
def read_tasks():
    return get_all_tasks()

@app.post("/tasks", response_model=Task)
def create_task(task: Task):
    return add_task(task)

@app.get("/tasks/{task_id}", response_model=Task)
def read_task(task_id: int):
    task = get_task_by_id(task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task

@app.delete("/tasks/{task_id}")
def remove_task(task_id: int):
    if delete_task(task_id):
        return {"message": "Task deleted"}
    raise HTTPException(status_code=404, detail="Task not found")
