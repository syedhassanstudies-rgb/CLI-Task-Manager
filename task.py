import uuid
from datetime import datetime
from typing import Optional


class Task:
    def __init__(
        self,
        title: str,
        description: str = "",
        priority: str = "medium",
        estimated_time: str = "",
        status: str = "pending",
        task_id: Optional[str] = None,
        created_at: Optional[str] = None,
    ):
        self.task_id = task_id or str(uuid.uuid4())
        self.title = title
        self.description = description
        self.priority = priority
        self.estimated_time = estimated_time
        self.status = status
        self.created_at = created_at or datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def complete(self) -> None:
        self.status = "completed"

    def to_dict(self) -> dict:
        return {
            "task_id": self.task_id,
            "title": self.title,
            "description": self.description,
            "priority": self.priority,
            "estimated_time": self.estimated_time,
            "status": self.status,
            "created_at": self.created_at,
        }

    @classmethod
    def from_dict(cls, data: dict) -> "Task":
        return cls(
            title=data["title"],
            description=data["description"],
            priority=data["priority"],
            estimated_time=data["estimated_time"],
            status=data["status"],
            task_id=data["task_id"],
            created_at=data["created_at"],
        )

    def __repr__(self) -> str:
        return (
            f"Task(id={self.task_id[:8]}, "
            f"title={self.title}, "
            f"status={self.status}, "
            f"priority={self.priority})"
        )