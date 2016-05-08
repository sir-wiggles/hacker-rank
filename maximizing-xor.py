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

input = '''10
1500'''

raw_input = MockInput(input)


l = int(raw_input().strip())
r = int(raw_input().strip())

max_so_far = 0
for x in xrange(l, r+1):
    for y in xrange(l, r+1):
        val = x ^ y
        if val > max_so_far:
            max_so_far = val

print max_so_far
