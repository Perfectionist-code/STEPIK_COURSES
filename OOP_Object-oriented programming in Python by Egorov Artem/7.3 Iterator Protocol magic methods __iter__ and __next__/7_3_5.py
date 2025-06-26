class FileReader:
    def __init__(self, filename):
        self.file = open(filename)

    def __iter__(self):
        return self

    def __next__(self):
        try:
            return self.file.__next__().strip()
        except:
            self.file.close()
            raise StopIteration

for line in FileReader('lorem.txt'):
    print(line)