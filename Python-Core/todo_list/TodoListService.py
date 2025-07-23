from enum import Enum


class TodoListService:
    _todo_list = []

    class Status(Enum):
        TODO = dict(key=1, value="todo")
        PROCESSING = dict(key=2, value="processing")
        DONE = dict(key=3, value="done")
        FAILED = dict(key=4, value="failed")
        REMOVED = dict(key=5, value="removed")

    def add(self, task):
        self._todo_list.append(
            dict(
                id=1 if len(self._todo_list) == 0 else self._todo_list[len(self._todo_list) - 1]["id"] + 1,
                task=task,
                status=self.Status.TODO.value["value"]
            )
        )

    def remove(self, id):
        for todo in self._todo_list:
            if todo["id"] == id:
                self.update_status(id, self.Status.REMOVED)

    def update_task(self, id, task):
        for index in range(len(self._todo_list)):
            if self._todo_list[index]["id"] == id:
                self._todo_list[index]["task"] = task

    def update_status(self, id, status):
        for index in range(len(self._todo_list)):
            if self._todo_list[index]["id"] == id:
                self._todo_list[index]["status"] = status

    def update_status_by_listId(self, ids, status):
        if not bool(ids):
            print("Update List Status was Failed")
            return

        # check valid Id
        for id in ids:
            if type(id) is not int:
                print("Update List Status was Failed")
                return

        # update status
        for id in ids:
            self.update_status(id, status)
        print("Update List Status was Done")

    def get_print_list(self):
        print()

        for todo in self._todo_list:
            task_id = "(" + str(todo["id"]) + ")"
            task = todo["task"]
            status = todo["status"]
            print("-", task_id, task, " | ", status, end="\n")

    def get_list(self):
        return self._todo_list

    def clear_todo_list(self):
        self._todo_list.clear()
