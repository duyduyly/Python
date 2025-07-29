from my_app.constant.JsonKeys import JsonKeys as keys
from my_app.service.TodoListService import TodoListService
from my_app.model.enums.DayOfWeek import DayOfWeek
from my_app.utils.DatetimeUtils import *


class TodoListUI:
    __service = TodoListService()
    __column_sign = "|"
    __list_sign = "-"

    def __display_menu(self):
        print("Todo List Function: ")
        print("1.Add Todo List.")
        print("2.Update Task.")
        print("3.Remove Task.")
        print("4.Update Status Task.")
        print("5.Update Multiple Status Task.")
        print("6.Display Weekly Todo List.")
        print("7.Display Current Day Todo List.")
        print("0.Exit.")

    def __display_weekly_todo_list(self):
        mon_task_list = self.__service.load_task_list_by_day(DayOfWeek.MONDAY.value)
        tue_task_list = self.__service.load_task_list_by_day(DayOfWeek.TUESDAY.value)
        wed_task_list = self.__service.load_task_list_by_day(DayOfWeek.WEDNESDAY.value)
        thu_task_list = self.__service.load_task_list_by_day(DayOfWeek.THURSDAY.value)
        fri_task_list = self.__service.load_task_list_by_day(DayOfWeek.FRIDAY.value)
        sat_task_list = self.__service.load_task_list_by_day(DayOfWeek.SATURDAY.value)
        sun_task_list = self.__service.load_task_list_by_day(DayOfWeek.SUNDAY.value)

        print(self.__generate_column(mon_task_list[keys.MAX_TITLE_SIZE], DayOfWeek.MONDAY.value, self.__column_sign),
              end="")
        print(self.__generate_column(tue_task_list[keys.MAX_TITLE_SIZE], DayOfWeek.TUESDAY.value, self.__column_sign),
              end="")
        print(self.__generate_column(wed_task_list[keys.MAX_TITLE_SIZE], DayOfWeek.WEDNESDAY.value, self.__column_sign),
              end="")
        print(self.__generate_column(thu_task_list[keys.MAX_TITLE_SIZE], DayOfWeek.THURSDAY.value, self.__column_sign),
              end="")
        print(self.__generate_column(fri_task_list[keys.MAX_TITLE_SIZE], DayOfWeek.FRIDAY.value, self.__column_sign),
              end="")
        print(self.__generate_column(sat_task_list[keys.MAX_TITLE_SIZE], DayOfWeek.SATURDAY.value, self.__column_sign),
              end="")
        print(self.__generate_column(sun_task_list[keys.MAX_TITLE_SIZE], DayOfWeek.SUNDAY.value, self.__column_sign),
              end="")
        print(" |")

        print("|", self.__generate_sign(mon_task_list[keys.MAX_TITLE_SIZE], "-"), end="")
        print(" |", self.__generate_sign(tue_task_list[keys.MAX_TITLE_SIZE], "-"), end="")
        print(" |", self.__generate_sign(wed_task_list[keys.MAX_TITLE_SIZE], "-"), end="")
        print(" |", self.__generate_sign(thu_task_list[keys.MAX_TITLE_SIZE], "-"), end="")
        print(" |", self.__generate_sign(fri_task_list[keys.MAX_TITLE_SIZE], "-"), end="")
        print(" |", self.__generate_sign(sat_task_list[keys.MAX_TITLE_SIZE], "-"), end="")
        print(" |", self.__generate_sign(sun_task_list[keys.MAX_TITLE_SIZE], "-"), end="")
        print("  |")

        index = 0
        while index < self.__service.count_max_row():
            self.__print_column(mon_task_list, index)
            self.__print_column(tue_task_list, index)
            self.__print_column(wed_task_list, index)
            self.__print_column(thu_task_list, index)
            self.__print_column(fri_task_list, index)
            self.__print_column(sat_task_list, index)
            self.__print_column(sun_task_list, index)

            index = index + 1
            print(" |")

    def __display_current_day_todo_list(self):
        day = get_lower_str_short_day()
        task_list = self.__service.load_task_list_by_day(day)
        print(self.__generate_column(task_list[keys.MAX_TITLE_SIZE], day, self.__list_sign))
        for index in range(len(task_list[keys.TASK_LIST])):
            print(self.__generate_column(task_list[keys.MAX_TITLE_SIZE], task_list[keys.TASK_LIST][index],
                                         f"\t{self.__list_sign}"))

    def __print_column(self, task_list, index):
        if len(task_list[keys.TASK_LIST]) > index:
            print(self.__generate_column(task_list[keys.MAX_TITLE_SIZE], task_list[keys.TASK_LIST][index],
                                         self.__column_sign),
                  end="")
        else:
            print(self.__generate_column(task_list[keys.MAX_TITLE_SIZE], "", self.__column_sign), end="")

    def __generate_column(self, max_size, text, list_sign):
        return f"{list_sign} {text} {self.__generate_space(text, max_size)}"

    def __generate_space(self, text, long_length):
        if long_length == 0: long_length = 10
        return " " * (long_length - len(text))

    def __generate_sign(self, max_size, sign):
        if max_size == 0: max_size = 10
        return sign * max_size

    def start(self):
        while True:
            self.__display_menu()

            print("Choose Function: ")
            choose_function = int(input())

            match choose_function:
                case 1:
                    print(
                        "Enter task (Example: Todo 100, 120, 2025-07-23T12:01:00, 2025-07-2T314:01:00, learning|content"
                    )
                    str_task = str(input())
                    self.__service.create_task(str_task)

                case 2:
                    pass
                case 3:
                    pass

                case 4:
                    pass

                case 5:
                    pass

                case 6:
                    print()
                    self.__display_weekly_todo_list()
                    print()
                case 7:
                    print()
                    self.__display_current_day_todo_list()
                    print()
                case 8:
                    pass

                case 0:
                    break
                case _:
                    break
