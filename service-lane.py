class MockInput(object):
    def __init__(self, *args):
        self.args = args
        self.count = 0
    def __call__(self):
        value = self.args[self.count]
        self.count += 1
        return value

def run(raw_input):

    length, cases = map(int, raw_input().strip().split(" "))
    width = map(int, raw_input().strip().split(" "))
    for case in xrange(cases):
        enter, exit = map(int, raw_input().strip().split(" "))
        print min(width[enter:exit+1])


if __name__ == "__main__":
    input = '''8 5
2 3 1 2 3 2 3 3
0 3
4 6
6 7
3 5
0 7'''.split('\n')

    input = '''5 5
1 2 2 2 1
2 3
1 4
2 4
2 4
2 3'''.split('\n')
    raw_input = MockInput(*input)
    run(raw_input)
