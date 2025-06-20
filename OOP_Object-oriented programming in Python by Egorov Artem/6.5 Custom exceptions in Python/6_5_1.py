class UserNotFoundError(Exception):
    """ Класс исключения не найденного пользователя"""


users = {
    "alice": {"name": "Alice Smith", "email": "alice@example.com"},
    "bob": {"name": "Bob Johnson", "email": "bob@example.com"},
    "jack": {"name": "Jack Wild", "email": "jack_wild@example.com"}
}


def get_user(username):
    if not username in users:
        raise UserNotFoundError('User not found')
    return users[username]['name']


try:
    username = get_user(input())
except UserNotFoundError as e:
    print(e)
else:
    print(username)
