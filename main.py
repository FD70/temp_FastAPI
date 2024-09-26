import string
import random

import requests
import json


LETTERS = string.ascii_letters

BASE_URL = "http://127.0.0.1:8000"

todoData = {
    "id": 1,
    "item": ''.join(random.choice(LETTERS) for _ in range(4))
}


def r_get_todo() -> requests.Response:
    return requests.get(BASE_URL + "/todo")


def r_post_todo(todo: dict) -> requests.Response:
    return requests.post(BASE_URL + "/todo", data=json.dumps(todo))


def r_put_todo(item_id: int, todo_item: dict) -> requests.Response:
    return requests.put(BASE_URL + f"/todo/{item_id}", data=json.dumps(todo_item))


if __name__ == '__main__':

    print(r_put_todo(1, todoData).text)
    print(r_get_todo().text)
