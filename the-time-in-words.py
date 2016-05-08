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


input = '''7
29'''

raw_input = MockInput(input)

h = int(raw_input().strip())
m = int(raw_input().strip())

words = {
0: "o' clock",
1: "one",
2: "two",
3: "three",
4: "four",
5: "five",
6: "six",
7: "seven",
8: "eight",
9: "nine",
10: "ten",
11: "eleven",
12: "twelve",
13: "thirteen",
14: "fourteen",
15: "quarter",
16: "sixteen",
17: "seventeen",
18: "eighteen",
19: "nineteen",
20: "twenty",
30: "half past"
}

if m < 30 and m != 0:
    hw = words[h]
    if m == 1:
        mins = "minute"
    else:
        mins = "minutes"
    if m < 21:
        mw = words[m]
    else:
        mw = '%s %s' % (words[20], words[m - 20])

    if m == 15:
        t = '%s past %s' % (mw, hw)
    else:
        t = '%s %s past %s' % (mw, mins, hw)

elif m > 30:
    hw = words[h+1 if h < 12 else 1]
    if 60-m == 1:
        mins = "minute"
    else:
        mins = "minutes"
    if 60 - m < 21:
        mw = words[60 - m]
    else:
        mw = '%s %s' % (words[20], words[60 - m - 20])

    if 60 - m == 15:
        t = '%s to %s' % (mw, hw)
    else:
        t = '%s %s to %s' % (mw, mins, hw)

elif m == 0:
    hw = words[h]
    t = '%s %s' % (hw, words[m])
    
else:
    hw = words[h]
    t = '%s %s' % (words[m], hw)

print t
