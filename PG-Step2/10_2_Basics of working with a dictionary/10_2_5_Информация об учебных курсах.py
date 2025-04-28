courses = { 'CS101': {'room': '3004', 'teacher': 'Хайнс', 'time': '8:00'},
            'CS102': {'room': '4501', 'teacher': 'Альварадо', 'time': '9:00'},
            'CS103': {'room': '6755', 'teacher': 'Рич', 'time': '10:00'},
            'NT110': {'room': '1244', 'teacher': 'Берк', 'time': '11:00'},
            'CM241': {'room': '1411', 'teacher': 'Ли', 'time': '13:00'},
            }

request = input()
print(f"{request}: {courses[request]['room']}, {courses[request]['teacher']}, {courses[request]['time']}")