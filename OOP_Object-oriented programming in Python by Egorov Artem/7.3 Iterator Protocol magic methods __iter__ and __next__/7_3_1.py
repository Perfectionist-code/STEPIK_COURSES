class SequenceIterable:
    def __init__(self, lst: list):
        self.lst = lst

    def __iter__(self):
        return iter(self.lst)

# container = SequenceIterable([1, 5, 4, 6, 43, True, 'hello'])
# for i in container:
#     print(i)