class MockInput(object):
    def __init__(self, *args):
        self.args = args
        self.count = 0
    def __call__(self):
        value = self.args[self.count]
        self.count += 1
        return value

input = '''5
0 0 1 2 1'''

raw_input = MockInput(*input.split("\n"))

count = raw_input().strip()
numbers = map(int, raw_input().strip().split(" "))
freq_counter = {}

for nu in numbers:
    freq_counter[nu] = freq_counter.setdefault(nu, 0) + 1
for k, v in freq_counter.iteritems():
    if v == 1:
        print k
