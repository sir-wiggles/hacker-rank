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

input = '''7 4
1110100110'''


raw_input = MockInput(input)

n, k = map(int, raw_input().strip().split(" "))
cipher = raw_input().strip()

msg = [cipher[0]]
xor = int(cipher[0])
fall_off = None
for i, b in enumerate(cipher[1:n]):
    ptr = i-k+2
    if ptr > 0:
        fall_off = msg[ptr - 1]
        xor ^= int(fall_off)

    if xor == 1 and b == '1':
        val = '0'
    elif xor == 0 and b == '1':
        val = '1'
    elif xor == 1 and b == '0':
        val = '1'
    else: # xor == 0 and b == '0':
        val = '0'
    msg.append(val)
    xor ^= int(val) 
print ''.join(msg)

# decoded = [int(cipher[0])]
# sxor = decoded[0]
# for i, c in enumerate(cipher[1:n]):
#     next_bit = sxor ^ int(c)
#     decoded.append(next_bit)
#     sxor ^= next_bit 
# print decoded
    

"""
Notes:

  1001010
   1001010
    1001010
     1001010
  ----------
  1110100110  <- cipher


  1_________
  1110100110


"""
