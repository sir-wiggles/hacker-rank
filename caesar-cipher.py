
class MockInput(object):
    def __init__(self, *args):
        self.args = args
        self.count = 0
    def __call__(self):
        value = self.args[self.count]
        self.count += 1
        return value

input = '''11
middle-Outz
2'''

raw_input = MockInput(*input.split())

length = int(raw_input().strip())
message = raw_input().strip()
shift = int(raw_input().strip())
encrypted = []
for l in message:
    if not l.isalpha():
        encrypted.append(l)
        continue
    if l.isupper():
        adj = 65
    else:
        adj = 97
    encrypted.append(chr(((ord(l) + shift) - adj) % 26 + adj))
print ''.join(encrypted)

