from datetime import datetime


def is_more_one_hour(login_time: str, logout_time: str):
    start = datetime.strptime(login_time, "%H:%M")
    end = datetime.strptime(logout_time, "%H:%M")
    difference = end - start
    return difference.seconds >= 3600


with open('logfile.txt', encoding = 'UTF-8') as file:
    with open('output.txt', 'w', encoding = 'UTF-8') as output_file:
        for line in file:
            name, login_t, logout_t = line.strip().split(', ')
            if is_more_one_hour(login_t, logout_t):
                print(name, file = output_file)
