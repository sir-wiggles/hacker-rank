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

input = '''3
2 4
2 8
5 9'''
input = '''2
8 10
8 10'''

input = '''2
160 160
831 831'''

raw_input = MockInput(input)

def get_val(n):
    val = n%4
    if val == 0:
        val = n/4 * 4
    elif val == 1:
        val = 1
    elif val == 2:
        val = n+1
    else:
        val = 0
    return val

for case in xrange(int(raw_input().strip())):

    l, r = map(int, raw_input().strip().split())
    if l == r:
        print get_val(l)
        continue
    
    array = []
    for i in xrange(l, (l//4 + 1) * 4):
        array.append(get_val(i))
    if l/4 != r/4:
        for i in xrange(4 * (r//4), r + 1):
            array.append(get_val(i))

        array.append(((r//4 - l//4 - 1) % 2) * 2)

    val = reduce(lambda x, y: x^y, array)
    print val


'''
Notes:

    [0, 4, 8, ...]  | i % 4 = 0 -> i/4 * 4
    [1, 5, 9, ...]  | i % 4 = 1 -> 1
    [2, 6, 10, ...] | i % 4 = 2 -> i + 1
    [3, 7, 11, ...] | i % 4 = 3 -> i

[
1 |     0,   1, 3, 
2 |  0, 4,   1, 7, 
3 |  0, 8,   1, 11, 
4 |  0, 12,  1, 15, 
5 |  0, 16,  1, 19, 
6 |  0, 20,  1, 23, 
7 |  0, 24,  1, 27, 
8 |  0, 28,  1, 31, 
9 |  0, 32,  1, 35, 
. |  0, 36,  1, 39, 
. |  0, 40,  1, 43, 
. |  0, 44,  1, 47, 
  |  0, 48,  1, 51, 
  |  0, 52,  1, 55, 
  |  0, 56,  1, 59, 
  |  0, 60,  1, 63, 
  |  0, 64,  1, 67, 
  |  0, 68,  1, 71, 
  |  0, 72,  1, 75, 
  |  0, 76,  1, 79, 
  |  0, 80,  1, 83, 
  |  0, 84,  1, 87, 
  |  0, 88,  1, 91, 
  |  0, 92,  1, 95, 
  |  0, 96,  1, 99, 
26|  0, 100, 1, 103]



'''
