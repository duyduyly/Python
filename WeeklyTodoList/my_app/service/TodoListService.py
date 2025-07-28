from my_app.service.FileService import FileService
from my_app.constant.JsonKeys import JsonKeys as keys
from my_app.utils.DatetimeUtils import *
import json


class TodoListService:
    __file_service = FileService()

    # get_weekly_schedule
    # get_tasks
    # get_last_index
    # create_task(get_last_index to set key, increase last_index,  add scheduler task by date and add task)
    def __init__(self):
        str_json = self.__file_service.load_str_json()
        self.__dict_json = json.loads(str_json)

    def get_weekly_schedule(self):
        return self.__dict_json[keys.WEEKLY_SCHEDULE]

    def get_tasks(self):
        return self.__dict_json[keys.TASKS]

    def get_last_index(self):
        return self.__dict_json[keys.LAST_INDEX]

    def create_task(self, task):
        last_index = self.get_last_index()
        tasks = self.get_tasks()
        tasks[str(last_index)] = task

        self.__dict_json[keys.TASKS] = tasks
        self.__dict_json[keys.LAST_INDEX] = last_index + 1

    def update_task(self, pr_task_key, pr_task):
        tasks = self.get_tasks()
        for task_id in tasks:
            if task_id == pr_task_key:
                tasks[task_id] = pr_task

    def update_status_task(self, pr_task_key, status):
        weekly_schedule = self.get_weekly_schedule()
        weekly_schedule_list = weekly_schedule[get_lower_str_short_day()]
        for schedule in weekly_schedule_list:
            if schedule[keys.TASK_ID] == pr_task_key:
                schedule[keys.STATUS] = status

        self.__dict_json[keys.WEEKLY_SCHEDULE] = weekly_schedule

    def load_task_list_by_day(self, day):
        task_list = []
        max_title_size = 0
        for day_task in self.get_weekly_schedule()[day]:
            title_task = self.get_tasks()[str(day_task[keys.TASK_ID])][keys.TITLE]
            status = day_task[keys.STATUS]
            title = title_task + f" ({status})"
            max_title_size = max(max_title_size, len(title))
            task_list.append(title)
        return dict(max_title_size=max_title_size, task_list=task_list)

# test = TodoListService()
# test.update_status_task(1, "OK")
