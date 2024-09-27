from fastapi import APIRouter, Path, HTTPException, status, responses

import model

todo_router = APIRouter()

todo_list = []

##
MESSAGE = "message"


@todo_router.post("/todo", status_code=201)
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
    # return responses.PlainTextResponse(
    #     str({MESSAGE: "Todo with supplied ID doesn't exist."}),
    #     status_code=status.HTTP_404_NOT_FOUND)
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Todo with supplied ID doesn't exist."
    )


@todo_router.put("/todo/{todo_id}")
async def update_todo(todo_data: model.TodoItem, todo_id: int = Path(..., title="The ID of the todo to be updated")) -> dict:
    for _todo in todo_list:
        _todo : model.Todo
        if _todo.id == todo_id:
            _todo.item = todo_data.item
            return {
                MESSAGE: "Todo updated successfully."
            }
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Todo with supplied ID doesn't exist."
    )


@todo_router.delete("/todo/all")
async def delete_all_todo() -> dict:
    todo_list.clear()
    return {
        MESSAGE: "Todos deleted successfully."
    }


@todo_router.delete("/todo/{todo_id}")
async def delete_single_todo(todo_id: int) -> dict:
    for i in range(len(todo_list)):
        _todo = todo_list[i]
        if _todo.id == todo_id:
            todo_list.pop(i)
            return {
                MESSAGE: f"Todo with id:{todo_id} deleted successfully."
            }
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Todo with id:{todo_id} doesn't exist."
    )
