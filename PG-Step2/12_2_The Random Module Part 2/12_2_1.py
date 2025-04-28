from random import randint


def generate_ip():
    return '.'.join([str(randint(0, 255)), str(randint(0, 255)), str(randint(0, 255)), str(randint(0, 255))])

print(generate_ip())

# from random import randrange as r
#
# def generate_ip():
#     return f'{r(256)}.{r(256)}.{r(256)}.{r(256)}'