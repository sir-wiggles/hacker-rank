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

input = '''haveaniceday'''

raw_input = MockInput(input)

#===========================

import math

line = raw_input().strip()
line_length = len(line)

sr = math.sqrt(line_length)
row = int(math.floor(sr))
col = int(math.ceil(sr))

while True:
    if row * col < sr:
        row += 1
    else:
        break

mat = map(None, *[iter(line)]*col)
mat = zip(*mat)
rows = []
for row in mat:
    rows.append(''.join(filter(lambda c: c is not None, row)))

print ' '.join(rows)
