import json
from abc import ABC, abstractmethod

from my_app.model.WeeklyTodoJson import ScheduledTask
from my_app.model.WeeklyTodoJson import WeeklyTodoJson, WeeklySchedule, Task
from my_app.model.enums.Status import Status
from my_app.service.FileService import FileService
from my_app.utils import setup_logger
from my_app.utils.DatetimeUtils import *


class ITodoListRepository(ABC):

    # Load Str Json to WeeklyTodoJson Class
    @abstractmethod
    def load_todo(self) -> 'WeeklyTodoJson':
        pass

    # refresh Todoo Json After Update
    @abstractmethod
    def refresh(self, todo: WeeklyTodoJson) -> None:
        pass

    # Get Weekly Schedule Class from WeeklyTodoJson class
    @abstractmethod
    def get_weekly_schedule(self) -> WeeklySchedule:
        pass

    # Update Weekly Schedule and then Update Todoo Json
    @abstractmethod
    def set_weekly_schedule(self, weekly_schedule: WeeklySchedule) -> None:
        pass

    # Get list dict[int, Task] from WeeklyTodoJson
    @abstractmethod
    def get_tasks(self) -> dict[int, Task]:
        pass

    # Update task and Update TodoJson
    @abstractmethod
    def set_tasks(self, task: Task) -> None:
        pass

    # Get Last Index (last index use to create id of task
    @abstractmethod
    def get_last_index(self) -> int:
        pass

    # add task for json, add task and Schedule task
    @abstractmethod
    def add_day_task(self, ui_task: Task, day: str) -> None:
        pass

    # update Json File
    @abstractmethod
    def update_json_file(self) -> None:
        pass

    @abstractmethod
    def max_todo_number_weekly(self) -> int:
        pass


class TodoListRepository(ITodoListRepository):
    __file_service = FileService()
    logging = setup_logger(name="Todo List Service")
    __weekly_todo_json = None

    def __init__(self):
        str_json = self.__file_service.load_str_json()
        self.__dict_json = json.loads(str_json)
        self.__weekly_todo_json = self.load_todo()

    def load_todo(self) -> 'WeeklyTodoJson':
        return WeeklyTodoJson.from_dict(self.__dict_json)

    def get_todo(self) -> 'WeeklyTodoJson':
        return self.__weekly_todo_json

    def refresh(self, todo: WeeklyTodoJson):
        self.__weekly_todo_json = todo

    def get_weekly_schedule(self):
        return self.__weekly_todo_json.weekly_schedule

    def set_weekly_schedule(self, weekly_schedule: WeeklySchedule) -> None:
        todo = self.__weekly_todo_json
        todo.weekly_schedule = weekly_schedule
        self.refresh(todo)

    def get_tasks(self) -> dict[int, Task]:
        return self.__weekly_todo_json.tasks

    def set_tasks(self, ui_task: Task) -> int:
        todo = self.__weekly_todo_json
        todo.last_index += 1
        todo.tasks.update({todo.last_index: ui_task})

        self.refresh(todo)
        return todo.last_index

    def get_last_index(self):
        return self.__weekly_todo_json.last_index

    def add_day_task(self, ui_task: Task, day=get_lower_str_short_day()) -> None:
        schedule = self.get_weekly_schedule()
        task_id = self.set_tasks(ui_task)
        self.set_weekly_schedule(
            schedule.add_weekly_schedule(
                ScheduledTask(task_id, Status.TODO.value),
                day)
        )
        self.update_json_file()

    def update_json_file(self):
        self.__file_service.update_json(self.__weekly_todo_json)

    def max_todo_number_weekly(self) -> int:
        schedule = self.get_weekly_schedule()
        max_size = 0
        for day in (
                schedule.mon,
                schedule.tue,
                schedule.wed,
                schedule.thu,
                schedule.fri,
                schedule.sat,
                schedule.sun):
            max_size = max(max_size, len(day))
        return max_size
