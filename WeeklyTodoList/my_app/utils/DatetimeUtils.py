from datetime import datetime

current_datetime = datetime.now()


def get_lower_str_short_day():
    return current_datetime.strftime("%a").lower()


def get_week_no():
    return current_datetime.strftime("%W")


def get_now_datetime():
    return current_datetime
