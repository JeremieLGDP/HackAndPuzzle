from datetime import date
from email.mime import multipart
from typing import List
from uuid import uuid4
import uvicorn
from fastapi import FastAPI, Form
import data_base
import model


app = FastAPI()

# db: List[model.ToDo] = [
#     model.ToDo(id=uuid4(), name='task1', owner='Jeremie', due_date=date(2022, 5, 1), description='I have to do this', priority='High'),
#     model.ToDo(id=uuid4(), name='task2', owner='Jeremie', due_date=date(2022, 5, 7), description='I have to do that', priority='Medium')
# ]

# get requests definition
@app.get('/')
def home():
    return {'hello' : 'world'}

@app.get('/ToDo/List')
async def Get_ToDo():
    return data_base.json_list

@app.post('/ToDo/Elem')
async def Add_ToDo(todo: model.ToDo):
    data_base.Add(todo)
    return {'id': todo.id}

@app.post('/ToDo/Mod')
async def Mod_ToDo(todo: model.ToDo):
    data_base.Update(todo)
    return {todo}

@app.delete('/ToDo/Elem/{todo_id}')
async def Delete_ToDo(todo_id):
    data_base.Delete(todo_id)
    return {data_base.json_list}


@app.post("/ToDo/Add")
async def Add_ToDo(name: str = Form(...), owner: str = Form(...), due_date: date = Form(date), description: str = Form(...), priority: model.Priority = Form(model.Priority)):
    todo = model.ToDo(name, owner, due_date, description, priority)
    data_base.Add(todo)
    return {"id": todo.id}



if __name__ == '__ main__':
    uvicorn.run("main:app", host="127.0.0.1", port=5000, log_level="info")