class MockInput(object):
    def __init__(self, *args):
        self.args = args
        self.count = 0
    def __call__(self):
        value = self.args[self.count]
        self.count += 1
        return value

input = '''1
10 10
7283455864
6731158619
8988242643
3830589324
2229505813
5633845374
6473530293
7053106601
0834282956
4607924137
3 4
9505
3845
3530'''
input = '''1
2 5
99999
12311
2 2
99
11'''
input = '''1
5 15
111111111111111
111111111111111
111111011111111
111111111111111
111111111111111
3 5
11111
11111
11110'''

raw_input = MockInput(*input.split('\n'))

def lookahead(bg, lg, col):
    found = bg[0].find(lg[0], col) 
    if found != -1 and found == col and len(lg) > 1:
        return lookahead(bg[1:], lg[1:], col)
    elif found != -1 and found == col and len(lg) == 1:
        return True
    else:
        return False

cases = int(raw_input().strip('\n'))
for case in xrange(cases):
    br, bc = map(int, raw_input().strip().split(" "))
    brows = []
    for _ in xrange(br):
        brows.append(raw_input().strip())

    lr, lc = map(int, raw_input().strip().split(" "))
    lrows = []
    for _ in xrange(lr):
        lrows.append(raw_input().strip())

    find_me = lrows[0]
    found = False
    for i, row in enumerate(brows):
        start = 0
        while True:
            have = row.find(find_me, start)
            if have != -1:
                found = lookahead(brows[i+1:], lrows[1:], have)
            else:
                break
            if found:
                break
            else:
                start = have+1
        if found:
            break


    if found:
        print "YES"
    else:
        print "NO"







