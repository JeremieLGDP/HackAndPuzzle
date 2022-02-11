from typing import List
import model
import json
from datetime import date

todo_list = list()
json_list = list()
# with open('todo_data.json') as json_file:
#     json_list = json.loads(json_file.read())
    
#     for todo in json_list:
#         todo = model.Todo_obj(**todo)
#         todo_list.append(todo) # model.Todo_obj(**todo))


def Add(todo: model.ToDo):
    json_list.append(todo.dict())
    todo = model.Todo_obj(todo.dict())
    todo_list.append(todo)
    with open('todo_data.json', 'w') as f:
        f.write(json_list)

def Update(todo: model.ToDo):
    for todol in json_list:
        if todol.id == todo.id:
            todol = todo
            break
    with open('todo_data.json', 'w') as f:
        f.write(json_list)

def Delete(id):
    for todo in json_list:
        if todo.id == id:
            json_list.remove(todo)
            with open('todo_data.json', 'w') as f:
                f.write(json_list)
            break

Add(model.ToDo(name='task3', owner='Jeremie', due_date=date(2022, 7, 1), description='I have to do this', priority='Low'))


