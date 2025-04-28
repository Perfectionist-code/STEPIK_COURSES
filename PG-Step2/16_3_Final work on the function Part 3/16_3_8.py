import operator
def arithmetic_operation(op: str):
    def operation(a,b):
    # d = {'+': operator.add,
    #         '/': operator.truediv,
    #         '*': operator.mul,
    #         '-': operator.sub}
        d = {'+': a + b,
             '/': a / b,
             '*': a * b,
             '-': a - b
            }
        return d[op]
    return operation


add = arithmetic_operation('+')
div = arithmetic_operation('/')
print(add(10, 20))
print(div(20, 5))