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

input = '''6
aaabbb
ab
abc
mnop
xyyx
xaxbbbxx'''

input = '''1
immceukpupwhgaosececxmueynudagpiudmyaxpuondunrortutthpzhftkfzbpvhdthckdqxgmkzbbvvxoeopmvjyakcrgjvzqxmvqjbcuafxvdwljnbvimwlwyccjzezzqwpzxtvzzvxetkninlrzhcwhgyqgerfunwwmptlqqkukxiukvlkcpilyibgnsnjhjhtabgrttnfqxaaslmwduhddijqcwblhjejmnafgqlwnlwiyjebfogiypadncowntgzgiemypkocgybrcexslhraiuqmimzdsyldezbwjryspzlueimrqdrazjmkwnpqlbtrcxnoomgenryrckiuqcurlidjvtaiwvzasnohbunoolgqxqmpuijiqmrnhtvdrugjjuskpfzfshxszjhurqcjfvwmprsinyrxsmhjtgomplgpwnjng
wliuzzlrhzpbwknftgokudv'''
raw_input = MockInput(input)

import collections
import string

cases = int(raw_input().strip())

for case in xrange(cases):
    line = raw_input().strip()
    if len(line) % 2:
        print -1
        continue
    
    s1 = line[:len(line)/2]
    s2 = line[len(line)/2:]
    s1_char_set = collections.Counter(s1)
    s2_char_set = collections.Counter(s2)

    count = 0
    for s in string.ascii_lowercase:
        count += abs(s1_char_set.get(s, 0) - s2_char_set.get(s, 0))

    print count / 2
