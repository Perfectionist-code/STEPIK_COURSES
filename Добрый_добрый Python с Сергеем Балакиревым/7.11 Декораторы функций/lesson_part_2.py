def func_decorator(func) :
    def wrapper(*args, **kwargs) :
        print("------ что-то делаем перед вызовом функции ------")
        res = func(*args,**kwargs)
        print("------ что-то делаем после вызова функции ------")
        return res
    return wrapper

# @func_decorator
def some_func(title, tag) :
    print("Работа функции, переданной в декоратор")
    print(f'title = {title}, tag = {tag}')
    return f'<{tag}>{title}</{tag}>'

some_func = func_decorator(some_func)
print(some_func('Python навсегда!', 'div'))
