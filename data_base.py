from typing import List
import model
import json

todo_list = list()
with open('todo_data.json') as json_file:
    json_list = json.loads(json_file.read())
    
    for todo in json_list:
        todo = model.Todo_obj(**todo)
        todo_list.append(todo) # model.Todo_obj(**todo))


def Add(todo: model.ToDo):
    json_list.append(todo)
    todo_list.append(model.Todo_obj(**todo))
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



