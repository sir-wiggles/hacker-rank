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
aaab
baa
aaa
abcdcfba'''

raw_input = MockInput(input)

def is_palindrome(s):
    l, r = 0, len(s) - 1
    for x in xrange(len(s)/2):
        if s[l] != s[r]:
            return False            
        l += 1
        r -= 1
    return True



cases = int(raw_input().strip())

for case in xrange(cases):
    line = raw_input().strip()
   
    s = len(line)
    l = line[:s/2] 
    r = line[-s/2 + (1 if s % 2 else 0):][::-1]

    pl, pr = 0, len(line)-1
    palindrome = True
    for x in xrange(s/2):
        if l[x] != r[x]:
            palindrome = False
            
            temp = line[:pl] + line[pl+1:]
            if not is_palindrome(temp):
                print pr
            else:
                print pl
            break

        pl += 1
        pr -= 1
    if palindrome:
        print -1
