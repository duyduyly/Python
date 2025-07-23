from service import TodoListService
from service import FileService
from constant import TodoJsonKeys as keys

if __name__ == '__main__':
    todo_list_service = TodoListService()
    file_service = FileService()

    todo_list_service.initializeFunc()
    file_service.initializeFunc()
    print(keys.MONDAY)
