def greet(name, *args):
    if args == ():
        res = 'Hello, ' + name + '!'
    else:
        res = ' and '
        res = 'Hello, ' + name + res + ' and '. join(args) + '!'
    return res

# def greet(name, *args):
#     return f'Hello, {" and ".join((name, *args))}!'


print(greet('Timur'))
print(greet('Timur', 'Roman'))
print(greet('Timur', 'Roman', 'Ruslan'))