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
3
1 2 3
4
1 2 3 4
3
3 5 4'''

_raw_input = MockInput(input)

cases = int(raw_input().strip())
for case in xrange(cases):
    n = int(raw_input().strip())
    array = map(int, raw_input().strip().split(" "))
    mul = 2 ** n // 2

    val = array[0] * mul
    for i, n in enumerate(array[1:]):
        val = val | (n * mul)
    val = val % (10**9 + 7)
    print val



'''
Notes:

    [1]
       [2]
          [3]
             [4]
    [1, 2]
       [2, 3]
          [3, 4]
    [1,    3]
    [1,       4]
       [2,    4]
    [1, 2, 3]
       [2, 3, 4]
    [1, 2,    4]
    [1,    3, 4]
    [1, 2, 3, 4]
    
    
    Binary map represents which element is in the sub array
    so 0101 implies a sub array of [2, 4]
    1 2 3 4 <- elements in array
    -------
    0 0 0 0 xOR <- Manual xORing of sub arrays
    0 0 0 1  4
    0 0 1 0  3
    0 0 1 1  7
    0 1 0 0  2
    0 1 0 1  6
    0 1 1 0  1
    0 1 1 1  5
    1 0 0 0  1
    1 0 0 1  5
    1 0 1 0  2
    1 0 1 1  6
    1 1 0 0  3
    1 1 0 1  7
    1 1 1 0  0
    1 1 1 1  4
            Sum^ = 56 <- sum of all xORed sub arrays
    
    My approach:
    
    Given that each element appears 2^n / 2 times (16 combinations with bit set half the time), multiply
    the element by the multiplication factor and OR them with all the other elements multiplied with 
    the multiplication factor.
    
    multiplication factor (m) = i*(2^n/2) 
        where:
            i is the element in array
            n is the length of array
    
    
    iterate through each element and multiply by m followed by ORing all values together
    8 | 16 | 24 | 32 = 56

'''
