from datetime import datetime


def display_current_datetime():
    current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return current_date


print(display_current_datetime())