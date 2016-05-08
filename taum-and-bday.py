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

input = '''5
10 10
1 1 1
5 9
2 3 4
3 6
9 1 1
7 7
4 2 1
3 3
1 9 2'''

raw_input = MockInput(input)

cases = int(raw_input().strip())
for case in xrange(cases):

    b, w = map(int, raw_input().strip().split(' '))
    pb, pw, ex = map(int, raw_input().strip().split(" "))

    if pb == pw:
        print b * pb + w * pw
    elif pb < pw:
        if pb + ex < pw:
            print b * pb + w * (pb+ex)
        else:
            print b * pb + w * pw
    elif pb > pw:
        if pw + ex < pb:
            print b * (pw+ex) + w * pw
        else:
            print b * pb + w * pw

