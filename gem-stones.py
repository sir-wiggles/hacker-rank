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
abcdde
baccd
eeabg'''
raw_input = MockInput(input)

elements = set()
rocks = int(raw_input().strip())
rock = raw_input().strip()
map(lambda x: elements.add(x), rock)
for i in xrange(rocks-1):
    rock = set()
    map(lambda x: rock.add(x), raw_input().strip() )
    elements.intersection_update(rock)

print len(elements)
    
     
