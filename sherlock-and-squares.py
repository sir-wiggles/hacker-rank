input = '''100
213 874
300 346
252 879
208 867
152 871
47 320
53 292
152 823
354 800
275 558
298 457
236 785
85 154
156 435
192 778
470 688
95 602
125 926
467 942
413 556
202 588
266 893
203 511
336 995
311 882
64 822
17 834
477 718
42 893
367 388
227 380
270 636
281 949
69 360
184 945
488 723
294 860
40 47
130 421
423 583
294 599
172 669
216 275
159 859
478 552
35 180
404 795
301 907
275 668
124 886
53 203
63 687
405 826
125 419
212 667
91 317
16 368
94 277
414 558
370 756
82 689
57 927
476 511
96 688
346 454
46 855
277 694
232 350
73 578
194 660
45 827
40 943
354 661
241 947
457 607
336 778
34 696
152 911
36 423
280 511
213 281
428 961
149 527
202 711
41 747
494 587
72 269
460 940
204 824
182 555
6 744
344 454
475 814
394 446
422 618
251 790
144 658
121 743
31 711
354 387
'''
class MockInput(object):
    def __init__(self, *args):
        self.args = args
        self.count = 0
    def __call__(self):
        value = self.args[self.count]
        self.count += 1
        return value
raw_input = MockInput(*input.split('\n'))
# =======================================

import math

cases = int(raw_input().strip())

for case in xrange(cases):
    bounds = map(int, raw_input().strip().split(' '))
    lower, upper = bounds
    upper = math.sqrt(upper)
    lower = math.sqrt(lower)
    upper = int(upper)
    lower = int(lower) if int(lower) != lower else int(lower) - 1
    print upper - lower

