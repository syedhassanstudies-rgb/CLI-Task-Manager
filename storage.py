import json
import os
from typing import List
from task import Task


STORAGE_FILE = "data/tasks.json"


def ensure_file_exists() -> None:
    if not os.path.exists(STORAGE_FILE):
        with open(STORAGE_FILE, "w") as f:
            json.dump([], f)


def load_tasks() -> List[Task]:
    ensure_file_exists()
    with open(STORAGE_FILE, "r") as f:
        raw = json.load(f)
    return [Task.from_dict(item) for item in raw]


def save_tasks(tasks: List[Task]) -> None:
    ensure_file_exists()
    with open(STORAGE_FILE, "w") as f:
        json.dump([task.to_dict() for task in tasks], f, indent=2)