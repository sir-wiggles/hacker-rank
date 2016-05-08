class MockInput(object):
    def __init__(self, *args):
        self.args = args
        self.count = 0
    def __call__(self):
        value = self.args[self.count]
        self.count += 1
        return value
input = '''6
5 4 4 2 2 8'''
input = '''8
1 2 3 4 3 3 2 1'''
input = ''' 8
1 13 3 8 14 9 4 4 '''
input = '''94
23 74 26 23 92 92 44 13 34 23 69 4 19 94 94 38 14 9 51 98 72 46 17 25 21 87 99 50 59 53 82 24 93 16 88 52 14 38 27 7 18 81 13 75 80 11 29 39 37 78 55 17 78 12 77 84 63 29 68 32 17 55 31 30 3 17 99 6 45 81 75 31 50 93 66 98 94 59 68 30 98 57 83 75 68 85 98 76 91 23 53 42 72 77'''
raw_input = MockInput(*input.split('\n'))

sticks = int(raw_input().strip())
sizes = map(int, raw_input().strip().split(" "))
zero_size = 0
print sticks
new_min = min_size = min(sizes)
left = set()
while sticks-zero_size > 0:
    min_size = new_min
    for i, stick in enumerate(sizes):
        if stick <= 0:
            continue
        new_size = stick - min_size
        sizes[i] = new_size
        if new_size <= 0:
            zero_size += 1
        if new_size > 0 and new_size < new_min:
            new_min = new_size
    l = sticks - zero_size
    if l:
        left.add(l)
print '\n'.join(map(str, sorted(list(left), reverse=True)))

