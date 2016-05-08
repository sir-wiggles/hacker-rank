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

input = '''4
12 15
2 3
8 13
8 16'''

raw_input = MockInput(input)


cases = int(raw_input().strip())
for case in xrange(cases):
    a, b = map(int, raw_input().strip().split(' '))
    x, y = a, b
    count = 0
    while True:
        count += 1
        x = x>>1
        y = y>>1
        if x == y:
            print x<<count
            break


'''
Notes: 

    Count the number of bit pos from the right until the bits match 
    For example: [330, 332]
         x 
    101001100
    101001010

    It takes three right bit shifts to get the two number to match 

    So 
        x = 330>>3
        x = x<<3
        print x

'''
