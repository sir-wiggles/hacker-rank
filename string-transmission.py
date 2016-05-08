class MockInput(object):
    def __init__(self, *args):
        if type(args[0]) == str:
            self.args = args[0].split('\n')
        else:
            self.args = args
        self.count = 0
    def __call__(self):
        value = self.args[self.count]
        self.count += 1
        return value

input = '''3
5 0
00000
3 1
001
3 3
101'''




"""
Notes:


    000 <- x
    001
    010
    011
    100
    101
    110
    111 <- x


"""
