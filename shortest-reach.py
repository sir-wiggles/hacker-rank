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
4 2
1 2
1 3
1
3 1
2 3
2'''

input = '''1
10 6
3 1
10 1
10 1
3 1
1 8
5 2
3'''

raw_input = MockInput(input)

# ========================

import collections

cases = int(raw_input().strip())

for case in xrange(cases):

    nodes, edges = map(int, raw_input().strip().split(' '))
    graph = {}
    for edge in xrange(edges):
        n1, n2 = map(int, raw_input().strip().split(' '))
        children = graph.get(n1, [])
        children.append(n2)
        graph[n1] = children

    start = int(raw_input().strip())
    queue = collections.deque([[start]])
    final = dict(zip(xrange(1, nodes+1), [0] * nodes))

    while queue:
        current = queue.popleft()
        parent = current[-1]
        nodes = graph.get(parent, None)
        if nodes is None:
            final[current[-1]] = current[0] 
            continue

        for node in nodes:
            if node not in current:
                queue.append([len(current), node])
            else:
                continue
    
    for k, v in final.iteritems():
        if k == start:
            continue
        print v * 6 if v > 0 else -1,
    print
