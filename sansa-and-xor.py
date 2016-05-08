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

input = '''2
3
1 2 3
4
4 5 7 5'''

raw_input = MockInput(input)

for case in xrange(int(raw_input().strip())):

    n = int(raw_input().strip())
    array = map(int, raw_input().strip().split())
    
    xor = 0
    if n % 2 == 0:
        xor = 0
    else:
        for i in array[::2]:
            xor ^= i
    print xor

    # Code to print out contiguous groupings used for figuring out.
    # for size in xrange(0, n):
    #     for pos in xrange(n-size):
    #         print array[pos:pos+1+size]
    # print ""

'''
Notes:

    Even lengh arrays will have symmetry in number of occurences.
    In the example below, with an array of 4 elements index 2, 3
    will mirror index 0, 1 in that 0 and 3 will both have 4 elements
    and index 1 and 2 will both have 6 elements.

    The properties of xor state that A^A = 0 so pairing them off,
    (A^A)^(A^A) = 0 ^ 0 = 0 So even length arrays will always be 0.

4x 6x 6x 4x 
[4]                                                                                                             
   [5]                                                                                                             
      [7]                                                                                                             
         [5]                                                                                                             
[4, 5]                                                                                                          
   [5, 7]                                                                                                          
      [7, 5]                                                                                                          
[4, 5, 7]                                                                                                       
   [5, 7, 5]                                                                                                       
[4, 5, 7, 5] 

    Odd length arrays will have symmetry but with a peak in the middle
    to account for the oddness; however, every even index will have an
    even number of occurences making only the odd indices of interest.
    We don't care about the odd number of occurences though because of 
    the xor properties (A^A)^A = A

3x 4x 3x
[1]                                                                                                             
   [2]                                                                                                             
      [3]                                                                                                             
[1, 2]                                                                                                          
   [2, 3]                                                                                                          
[1, 2, 3]

5x 8x 9x 8x 5x
[1]                                                                                                             
   [2]                                                                                                             
      [3]                                                                                                             
         [4]                                                                                                             
            [5]                                                                                                             
[1, 2]                                                                                                          
   [2, 3]                                                                                                          
      [3, 4]                                                                                                          
         [4, 5]                                                                                                          
[1, 2, 3]                                                                                                       
   [2, 3, 4]                                                                                                       
      [3, 4, 5]                                                                                                       
[1, 2, 3, 4]                                                                                                    
   [2, 3, 4, 5]                                                                                                    
[1, 2, 3, 4, 5] 
'''
