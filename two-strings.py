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

input = '''2
hello
world
hi
world'''
raw_input = MockInput(input)

import collections

cases = int(raw_input().strip())

for case in xrange(cases):
    s1 = collections.Counter([x for x in raw_input().strip()])
    s2 = collections.Counter([x for x in raw_input().strip()])

    s1_keys = set(s1.keys())
    s2_keys = set(s2.keys())

    s1_keys.intersection_update(s2_keys)
    if len(s1_keys):
        print "YES"
    else:
        print "NO"
