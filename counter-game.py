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

input = """6
9007199254740992
3876255231698756951
2505421038165995835
9181662375833297205
9876967415056854651
2147483648"""

raw_input = MockInput(input)

for x in xrange(int(raw_input().strip())):
    n = int(raw_input())-1
    on = sum(b=='1' for b in bin(n)[2:])

    if on&1:
        print "Louise"
    else:
        print "Richard"
