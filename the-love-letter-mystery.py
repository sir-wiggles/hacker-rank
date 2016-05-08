
class MockInput(object):
    def __init__(self, *args):
        self.args = args
        self.count = 0
    def __call__(self):
        value = self.args[self.count]
        self.count += 1
        return value

input = '''4
abc
abcba
abcd
cba'''

raw_input = MockInput(*input.split('\n'))


cases = int(raw_input().strip())

for case in xrange(cases):
    line = raw_input().strip()

    r = len(line) - 1
    diff = 0
    for l in xrange(len(line)/2):
        a, z = line[l], line[r]
        if a != z:
            diff += abs(ord(z) - ord(a))
        r -= 1
    print diff
