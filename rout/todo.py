from fastapi import APIRouter, Path

import model

todo_router = APIRouter()

todo_list = []

##
MESSAGE = "message"

@todo_router.post("/todo")
async def add_todo(data: model.Todo) -> dict:
    todo_list.append(data)
    return {MESSAGE: "Todo added succesfully"}


@todo_router.get("/todo")
async def retrieve_todos() -> dict:
    return {"todos": todo_list}


@todo_router.get("/todo/{todo_id}")
async def get_single_todo(todo_id: int = Path(..., title="The ID of the todo to retrieve.")) -> dict:
    for _todo in todo_list:
        if _todo.id == todo_id:
            return {
                "todo": _todo
            }
    return {
        MESSAGE: "Todo with supplied ID doesn't exist."
    }


@todo_router.put("/todo/{todo_id}")
async def update_todo(todo_data: model.TodoItem, todo_id: int = Path(..., title="The ID of the todo to be updated")) -> dict:
    for _todo in todo_list:
        _todo : model.Todo
        if _todo.id == todo_id:
            _todo.item = todo_data.item
            return {
                MESSAGE: "Todo updated successfully."
            }
    return {
        MESSAGE: "Todo with supplied ID doesn't exist."
    }
