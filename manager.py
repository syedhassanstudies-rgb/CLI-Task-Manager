from typing import List, Optional
from task import Task
from storage import load_tasks, save_tasks
from decorators import log_action
from ai_helper import suggest_task_details


class TaskManager:
    def __init__(self):
        self.tasks: List[Task] = load_tasks()

    @log_action
    def add_task(self, title: str, description: str = "", use_ai: bool = True) -> Task:
        if use_ai:
            print("🤖 Analyzing your task...")
            suggestion = suggest_task_details(title, description)
            priority = suggestion["priority"]
            estimated_time = suggestion["estimated_time"]
            print(f"   Priority suggested: {priority}")
            print(f"   Estimated time:     {estimated_time}")
            print(f"   Reason:             {suggestion['reason']}")
        else:
            priority = "medium"
            estimated_time = ""

        task = Task(
            title=title,
            description=description,
            priority=priority,
            estimated_time=estimated_time,
        )

        self.tasks.append(task)
        save_tasks(self.tasks)
        return task

    @log_action
    def complete_task(self, task_id: str) -> Optional[Task]:
        task = self._find_task(task_id)
        if task:
            task.complete()
            save_tasks(self.tasks)
            return task
        print(f"No task found with id starting with '{task_id}'")
        return None

    @log_action
    def delete_task(self, task_id: str) -> bool:
        task = self._find_task(task_id)
        if task:
            self.tasks.remove(task)
            save_tasks(self.tasks)
            return True
        print(f"No task found with id starting with '{task_id}'")
        return False

    def get_all_tasks(self) -> List[Task]:
        return self.tasks

    def get_by_status(self, status: str) -> List[Task]:
        return [t for t in self.tasks if t.status == status]

    def get_by_priority(self, priority: str) -> List[Task]:
        return [t for t in self.tasks if t.priority == priority]

    def _find_task(self, task_id: str) -> Optional[Task]:
        for task in self.tasks:
            if task.task_id.startswith(task_id):
                return task
        return None