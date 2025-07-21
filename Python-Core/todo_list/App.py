from TodoListService import TodoListService


class Todo:

    # TodoList Assignment
    # 1. add task'
    # 2. update task or status
    #       - update task by id
    #       - update status of task by id
    # 3. remove task (soft remove task)
    # 4. display all task stored in List
    # 5. Update Status of Task by List id (input(1,2,3,4,5))
    # 10. Available tasks to test
    # 0. Exist out the System
    def process(self):
        service = TodoListService()
        while True:
            self.display_menu()
            print("Enter: ")
            choose_menu = int(input())
            match choose_menu:
                case 1:
                    print("Enter task: ")
                    task = str(input())
                    service.add(task)
                case 2:
                    self.update_task(service)
                case 3:
                    service.get_print_list()
                    print("Enter Id:")
                    task_id = int(input())
                    service.remove(task_id)
                case 4:
                    service.get_print_list()
                case 5:
                    self.update_status_by_listId(service)
                case 10:
                    service.add("Learn English.")
                    service.add("Learn Math.")
                    service.add("Learn Python.")
                    service.add("Learn Java.")
                    service.add("Clean Up My Room.")
                    service.add("Go to The Supper Market.")
                case 0:
                    break
                # exist
                case _:
                    print("Please, Choose from 0 to 4")

    def display_menu(self):
        print("Menu: ")
        print("1. Add task")
        print("2. Update task or Status")
        print("3. Remove task")
        print("4. Display All task")
        print("5. Update Status By List Id")
        print("10. Example Task List")
        print("0. System Exit")

    # update task by id
    # - update task
    # - update status of task
    def update_task(self, service):
        service.get_print_list()
        print("Enter Id:")
        task_id = int(input())

        print("Choose Kind of update do you want: ")
        print("Choose 1 to update task.")
        print("Choose 2 to update status")
        pick = int(input())
        match pick:
            case 1:
                print("Enter task want update: ")
                task = str(input())
                service.update_task(task_id, task)
            case 2:
                print("Choose status want update: ")
                print("(1) Processing")
                print("(2) Done")
                print("(Else) Failed ")
                status = int(input())
                match status:
                    case 1:
                        service.update_status(task_id, service.Status.PROCESSING.value["value"])
                    case 2:
                        service.update_status(task_id, service.Status.DONE.value["value"])
                    case _:
                        service.update_status(task_id, service.Status.FAILED.value["value"])

    # Update Status of task by List id
    def update_status_by_listId(self, service):
        service.get_print_list()
        print("Enter List Ids(Ex:1,2,3,4) : ")
        str_ids_list = str(input())
        int_ids_list = [int(x) for x in str_ids_list.split(",")]

        print("Choose status want update: ")
        print("(1) Processing")
        print("(2) Done")
        print("(Else) Failed ")
        status = int(input())
        match status:
            case 1:
                service.update_status_by_listId(int_ids_list, service.Status.PROCESSING.value["value"])
            case 2:
                service.update_status_by_listId(int_ids_list, service.Status.DONE.value["value"])
            case _:
                service.update_status_by_listId(int_ids_list, service.Status.FAILED.value["value"])


if __name__ == "__main__":
    todo = Todo()
    todo.process()
