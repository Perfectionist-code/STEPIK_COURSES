def func_decorator(func) :
    def wrapper() :
        print("------ что-то делаем перед вызовом функции ------")
        func()
        print("------ что-то делаем после вызова функции ------")

    return wrapper


def some_func() :
    print("Вызов функции some_func")

f = func_decorator(some_func)
f()
