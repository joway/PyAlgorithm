class Test(object):
    def __init__(self):
        self.a = 1

    def insert(self, a):
        a = 2

test = Test()
test.insert(test.a)
print(test.a)
