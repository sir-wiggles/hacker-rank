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

input = '''aaabbbb'''
input = '''cdefghmnopqrstuvw'''
input = '''cdcdcdcdeeeef'''

raw_input = MockInput(input)


import collections
line = raw_input().strip()
freq = collections.Counter([x for x in line])

valid = True
if len(line) % 2:
    center_taken = False
    for k, v in freq.iteritems():
        if v % 2 and not center_taken:
            center_taken = True
        elif v % 2 and center_taken:
            valid = False
            break
else:
    for k, v in freq.iteritems():
        if v % 2:
            valid = False
            break

if valid:
    print "YES"
else:
    print "NO"
