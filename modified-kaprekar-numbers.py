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

input = '''100
300
'''

raw_input = MockInput(input)

lower = int(raw_input().strip())
upper = int(raw_input().strip())

vals = [] 

for n in xrange(lower, upper+1):
    d = len(str(n))
    s = str(n**2)
    a, b = int(s[:len(s) - d] or 0), int(s[len(s) - d:] or 0)
    if b and a+b == n:
        vals.append(str(n))

if len(vals) == 0:
    print "INVALID RANGE"
else:
    print ' '.join(vals)
