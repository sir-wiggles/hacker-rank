class MockInput(object):
    def __init__(self, *args):
        self.args = args
        self.count = 0
    def __call__(self):
        value = self.args[self.count]
        self.count += 1
        return value

input = '''We promptly judged antique ivory buckles for the next prize   
'''

raw_input = MockInput(*input.split('\n'))

import string

line = raw_input().strip().lower()
letter_map = {}
for ch in line:
    if ch in string.ascii_lowercase:
        letter_map[ch] = True
if len(letter_map) == len(string.ascii_lowercase):
    print "pangram"
else:
    print "not pangram"
