from dataclasses import dataclass, field
from typing import List, Dict

from my_app.model.enums.DayOfWeek import DayOfWeek, str_enum


@dataclass
class Task:
    title: str
    estimate_minutes: int
    start: str
    end: str
    tags: List[str]

    def __init__(self, title: str, estimate_minutes: int, start: str, end: str, tags: List[str]):
        self.title = title
        self.estimate_minutes = estimate_minutes
        self.start = start
        self.end = end
        self.tags = tags

    @staticmethod
    def from_dict(data: dict) -> 'Task':
        return Task(**data)

    def to_dict(self) -> dict:
        return {
            "title": self.title,
            "estimate_minutes": self.estimate_minutes,
            "start": self.start,
            "end": self.end,
            "tags": self.tags
        }


@dataclass
class ScheduledTask:
    task_id: int
    status: str

    def __init__(self, task_id, status):
        self.task_id = task_id
        self.status = status

    @staticmethod
    def from_dict(data: dict) -> 'ScheduledTask':
        return ScheduledTask(**data)

    def to_dict(self) -> dict:
        return {
            "task_id": self.task_id,
            "status": self.status
        }


@dataclass
class WeeklySchedule:
    mon: List[ScheduledTask] = field(default_factory=list)
    tue: List[ScheduledTask] = field(default_factory=list)
    wed: List[ScheduledTask] = field(default_factory=list)
    thu: List[ScheduledTask] = field(default_factory=list)
    fri: List[ScheduledTask] = field(default_factory=list)
    sat: List[ScheduledTask] = field(default_factory=list)
    sun: List[ScheduledTask] = field(default_factory=list)

    @staticmethod
    def from_dict(data: dict) -> 'WeeklySchedule':
        return WeeklySchedule(
            mon=[ScheduledTask.from_dict(d) for d in data.get("mon", [])],
            tue=[ScheduledTask.from_dict(d) for d in data.get("tue", [])],
            wed=[ScheduledTask.from_dict(d) for d in data.get("wed", [])],
            thu=[ScheduledTask.from_dict(d) for d in data.get("thu", [])],
            fri=[ScheduledTask.from_dict(d) for d in data.get("fri", [])],
            sat=[ScheduledTask.from_dict(d) for d in data.get("sat", [])],
            sun=[ScheduledTask.from_dict(d) for d in data.get("sun", [])],
        )

    def to_dict(self) -> dict:
        return {
            "mon": [t.to_dict() for t in self.mon],
            "tue": [t.to_dict() for t in self.tue],
            "wed": [t.to_dict() for t in self.wed],
            "thu": [t.to_dict() for t in self.thu],
            "fri": [t.to_dict() for t in self.fri],
            "sat": [t.to_dict() for t in self.sat],
            "sun": [t.to_dict() for t in self.sun],
        }

    def add_weekly_schedule(self, scheduled_task: ScheduledTask, day: str) -> 'WeeklySchedule':
        enum = str_enum(day)
        match enum:
            case DayOfWeek.MONDAY:
                self.mon.append(scheduled_task)
            case DayOfWeek.TUESDAY:
                self.tue.append(scheduled_task)
            case DayOfWeek.WEDNESDAY:
                self.wed.append(scheduled_task)
            case DayOfWeek.THURSDAY:
                self.thu.append(scheduled_task)
            case DayOfWeek.FRIDAY:
                self.fri.append(scheduled_task)
            case DayOfWeek.SATURDAY:
                self.sat.append(scheduled_task)
            case DayOfWeek.SUNDAY:
                self.sun.append(scheduled_task)
        return self


@dataclass
class WeeklyTodoJson:
    tasks: Dict[int, Task]
    weekly_schedule: WeeklySchedule
    last_index: int

    @staticmethod
    def from_dict(data: dict) -> 'WeeklyTodoJson':
        tasks = {int(k): Task.from_dict(v) for k, v in data["tasks"].items()}
        schedule = WeeklySchedule.from_dict(data["weekly_schedule"])
        return WeeklyTodoJson(
            tasks=tasks,
            weekly_schedule=schedule,
            last_index=data["last_index"]
        )

    def to_dict(self) -> dict:
        return {
            "tasks": {str(k): v.to_dict() for k, v in self.tasks.items()},
            "weekly_schedule": self.weekly_schedule.to_dict(),
            "last_index": self.last_index
        }
