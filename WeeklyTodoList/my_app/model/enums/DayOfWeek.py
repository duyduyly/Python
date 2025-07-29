from enum import Enum


def str_enum(value: str):
    for day in DayOfWeek:
        if day.value == value:
            return day


def list_short_day() -> list[str]:
    return [day.value for day in DayOfWeek]


class DayOfWeek(Enum):
    MONDAY = "mon"
    TUESDAY = "tue"
    WEDNESDAY = "wed"
    THURSDAY = "thu"
    FRIDAY = "fri"
    SATURDAY = "sat"
    SUNDAY = "sun"
