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

input = '''cde
abc'''
raw_input = MockInput(input)
import collections
import string
f1 = collections.Counter([x for x in raw_input().strip()])
f2 = collections.Counter([x for x in raw_input().strip()])

count = 0
for s in string.ascii_lowercase:
    v1 = f1.get(s, 0)
    v2 = f2.get(s, 0)
    diff = abs(v2 - v1)
    count += diff
print count
