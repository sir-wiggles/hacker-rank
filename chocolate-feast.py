class MockInput(object):
    def __init__(self, *args):
        self.args = args
        self.count = 0
    def __call__(self):
        value = self.args[self.count]
        self.count += 1
        return value

input = '''1
6 2 2'''
input = '''1
10 2 2'''

raw_input = MockInput(*input.split('\n'))

import math
cases = int(raw_input().strip())

def calc(wrappers, price):
    can_buy = wrappers/price
    if can_buy < 1:
        return 0
    leftover = math.modf(can_buy)[0] * price
    leftover = leftover if leftover >= 1 else 0
    return int(can_buy) + calc(int(can_buy) + leftover ,price)


wrappers_saved = 0
for case in xrange(cases):
    m, c, w = map(int, raw_input().strip().split(" "))
    can_buy = m/c
    print can_buy + calc(can_buy, float(w))

