from dataclasses import dataclass


@dataclass
class Task:
    title: str
    estimate_time: int
    start: str
    end: str
    tags: list


class Todo:
    task_id: int
    status: str


@dataclass
class WeeklySchedule:
    mon: list[Todo]
    tue: list[Todo]
    wed: list[Todo]
    thu: list[Todo]
    fri: list[Todo]
    sat: list[Todo]
    sun: list[Todo]

    def get_todo(self, day: str):
        match day.lower():
            case "mon":
                return self.mon
            case "tue":
                return self.tue
            case "wed":
                return self.wed
            case "thu":
                return self.thu
            case "fri":
                return self.fri
            case "sat":
                return self.sat
            case "sun":
                return self.sun
