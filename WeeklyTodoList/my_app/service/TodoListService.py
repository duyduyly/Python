import json

from my_app.constant.JsonKeys import JsonKeys as keys
from my_app.model.WeeklyTodoJson import Task, WeeklySchedule
from my_app.repository.TodoListRepository import TodoListRepository
from my_app.service.FileService import FileService
from my_app.utils import setup_logger
from my_app.utils.DatetimeUtils import *
from abc import ABC, abstractmethod


class ITodoListService(ABC):
    @abstractmethod
    def get_weekly_schedule(self) -> dict[WeeklySchedule]:
        pass

    @abstractmethod
    def get_tasks(self) -> dict[int, Task]:
        pass

    @abstractmethod
    def get_last_index(self) -> int:
        pass

    # create Task From String input task
    @abstractmethod
    def create_task(self, str_task: str) -> None:
        pass

    # load task by currency day
    @abstractmethod
    def load_task_list_by_day(self, day=get_lower_str_short_day()):
        pass

    # Count max size in WeeklySchedule to generate max record number  in UI
    @abstractmethod
    def count_max_row(self):
        pass

    # example: Todo 01, 120, 2025-07-23T12:01:00, 2025-07-23T14:01:00, learning|content
    # slit String input from Console and set into Task Class
    @abstractmethod
    def format_str_task(self, str_task: str) -> Task:
        pass


class TodoListService(ITodoListService):
    __file_service = FileService()
    logging = setup_logger(name="Todo List Service")
    __todoListRepository = TodoListRepository()

    def __init__(self):
        str_json = self.__file_service.load_str_json()
        self.__dict_json = json.loads(str_json)

    def get_weekly_schedule(self) -> dict[WeeklySchedule]:
        return self.__todoListRepository.get_weekly_schedule().to_dict()

    def get_tasks(self) -> dict[int, Task]:
        return self.__todoListRepository.get_tasks()

    def get_last_index(self) -> int:
        return self.__todoListRepository.get_last_index()

    def create_task(self, str_task: str) -> None:
        task = self.format_str_task(str_task)
        self.__todoListRepository.add_day_task(task)
        self.logging.info(f"Create {str_task} was success")

    def load_task_list_by_day(self, day=get_lower_str_short_day()):
        task_list = []
        max_title_size = 0
        for day_task in self.get_weekly_schedule()[day]:
            task = self.get_tasks()[day_task[keys.TASK_ID]]
            title_task = task.to_dict()[keys.TITLE]
            status = day_task[keys.STATUS]
            title = title_task + f" ({status})"
            max_title_size = max(max_title_size, len(title))
            task_list.append(title)
        return dict(max_title_size=max_title_size, task_list=task_list)

    def count_max_row(self):
        return self.__todoListRepository.max_todo_number_weekly()

    def format_str_task(self, str_task: str) -> Task:
        plit_str = str_task.split(",")
        plit_status_list = plit_str[4].strip().split("|")  # plit status
        return Task(plit_str[0].strip(), int(plit_str[1].strip()), plit_str[2].strip(), plit_str[3].strip(),
                    plit_status_list)
