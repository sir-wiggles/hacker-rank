class MockInput(object):
    def __init__(self, *args):
        self.args = args
        self.count = 0
    def __call__(self):
        value = self.args[self.count]
        self.count += 1
        return value

input = '''5 3
4 2 6 1 10'''
input = '''15 20
1 8 19 15 2 29 3 2 25 2 19 26 17 33 22'''


raw_input = MockInput(*input.split('\n'))


chapters, ppp = map(int, raw_input().strip().split(" "))
problem_sets = map(int, raw_input().strip().split(" "))


page_number = 1
special = 0
for ch, problem_set in enumerate(problem_sets, start=1):
    page = []
    for problem in xrange(1, problem_set+1):
        page.append(problem)
        if problem == page_number:
            special += 1
        if problem and problem % ppp == 0:
            page = []
            page_number += 1
    if len(page):
        page_number += 1
print special
