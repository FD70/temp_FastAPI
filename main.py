import string
import random

import requests
import json


LETTERS = string.ascii_letters

BASE_URL = "http://127.0.0.1:8000"


def _get_random_todo_data() -> dict:
    return {
        "id": random.randint(1, 100),
        "item": ''.join(random.choice(LETTERS) for _ in range(7))
    }


def r_get_anything(route: str) -> requests.Response:
    return requests.get(BASE_URL + route)


def r_get_todo() -> requests.Response:
    return requests.get(BASE_URL + "/todo")


def r_get_todo_by_id(todo_id: int) -> requests.Response:
    return requests.get(BASE_URL + f"/todo/{todo_id}")


def r_post_todo(todo: dict) -> requests.Response:
    return requests.post(BASE_URL + "/todo", data=json.dumps(todo))


def r_put_todo(todo_id: int, todo_item: dict) -> requests.Response:
    return requests.put(BASE_URL + f"/todo/{todo_id}", data=json.dumps(todo_item))


def r_delete_todo(todo_id: int) -> requests.Response:
    return requests.delete(BASE_URL + f"/todo/{todo_id}")


def r_delete_all() -> requests.Response:
    return requests.delete(BASE_URL + "/todo/all")


if __name__ == '__main__':

    req = r_post_todo(_get_random_todo_data())
    print(req.text)
    print(req.status_code)
