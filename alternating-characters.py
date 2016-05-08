class MockInput(object):
    def __init__(self, *args):
        self.args = args
        self.count = 0
    def __call__(self):
        value = self.args[self.count]
        self.count += 1
        return value

input = '''5
AAAA
BBBBB
ABABABAB
BABABA
AAABBB'''
raw_input = MockInput(*input.split('\n'))


cases = int(raw_input().strip())

for case in xrange(cases):
    line = raw_input().strip()
    previous = line[0]
    delete = 0
    for c in line[1:]:
        if c == previous:
            delete += 1
        else:
            previous = c

    print delete
