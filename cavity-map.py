
class MockInput(object):
    def __init__(self, *args):
        self.args = args
        self.count = 0
    def __call__(self):
        value = self.args[self.count]
        self.count += 1
        return value

input = '''4
1112
1912
1892
1234'''

raw_input = MockInput(*input.split("\n"))

row_count = int(raw_input().strip())
rows = [raw_input().strip() for _ in xrange(row_count)]

loc = []
for y, valid_row in enumerate(rows[1:-1], start=1):
    for x, d in enumerate(valid_row[1:-1], start=1):
       t = rows[y-1][x] 
       b = rows[y+1][x]
       l = rows[y][x-1]
       r = rows[y][x+1]
       if d > t and d > b and d > l and d > r:
           loc.append((x, y))

for l in loc:
    x, y = l
    line = rows[y] 
    line = line[:x] + 'X' + line[x+1:]
    rows[y] = line

print '\n'.join(rows)
