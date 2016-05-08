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

input = '''8
GAAATAAA'''

raw_input = MockInput(input)

import collections

def inc_min(c, g):
    mk = ''
    mv = 0
    for k, v in sorted(c.items(), key=lambda x: x[1]):
        if g == k:
            continue
        if v < mv:
            mk= k
        break
    if mk != '':
        c[mk] += 1

def dec_max(c, g):
    mk = ''
    mv = 0
    for k, v in sorted(c.items(), key=lambda x: x[1], reverse=True):
        if g == k:
            continue
        if v > mv:
            mk= k
        break
    if mk != '':
        c[mk] -= 1


gene_length = int(raw_input().strip())
gene = raw_input().strip()
freq = collections.Counter(gene)

gene_diffs = {}
for g in 'ACTG':
    gene_diffs[g] = freq.get(g, 0) - gene_length/4

stable = gene_length/4
min_so_far = gene_length
for i, h in enumerate(gene):
    run = True
    count = 0
    gdc = gene_diffs.copy()
    j = i
    while(run):
        g = gene[j]
        dec_max(gdc, g)
        inc_min(gdc, g)
        j += 1
            
print min_so_far
