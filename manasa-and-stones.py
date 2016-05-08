
class MockInput(object):
    def __init__(self, *args):
        self.args = args
        self.count = 0
    def __call__(self):
        value = self.args[self.count]
        self.count += 1
        return value


input = '''1
4
10
100'''


raw_input = MockInput(*input.split('\n'))

cases = raw_input().strip()

for case in cases:
    stones = int(raw_input().strip())
    a = int(raw_input().strip())
    b = int(raw_input().strip())

    s = set()
    for i in xrange(stones):
        s.add(i*a + (stones-i-1) * b)

    print ' '.join(map(str, sorted(list(s))))

