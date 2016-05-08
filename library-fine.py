
class MockInput(object):
    def __init__(self, *args):
        self.args = args
        self.count = 0
    def __call__(self):
        value = self.args[self.count]
        self.count += 1
        return value

input = '''9 6 2015
6 6 2015'''

input = '''31 8 2004
20 1 2004'''

input = '''28 2 2015
15 4 2015'''

input = '''2 7 1014
1 1 1014'''

raw_input = MockInput(*input.split('\n'))

returned = map(int, raw_input().strip().split(' '))
expected = map(int, raw_input().strip().split(' '))

fines = [15, 500, 10000][::-1]
total = 0

diffs = map(lambda x: x[0] - x[1], zip(returned, expected))
for i, t in enumerate(diffs[::-1]):
    if t > 0:
        total = fines[i] * t
        break
    elif t < 0:
        break


print diffs[::-1]
print total 
