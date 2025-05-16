from typing import Optional


class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

    def __str__(self):
        return str(self.val)


class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        else:
            visited = set()
            nodes = {}
            q = [node]
            while len(q) != 0:
                n = q.pop(0)
                if n.val not in nodes:
                    nodes[n.val] = Node(n.val)
                if n.val not in visited:
                    visited.add(n.val)
                    for ngs in n.neighbors:
                        q.append(ngs)
                        if ngs.val not in nodes:
                            nodes[ngs.val] = Node(ngs.val)
                        nodes[n.val].neighbors.append(nodes[ngs.val])

            return nodes[node.val]


root = Node(1)
a = Node(2)
b = Node(3)
c = Node(4)

root.neighbors.append(a)
root.neighbors.append(c)

a.neighbors.append(root)
a.neighbors.append(b)

b.neighbors.append(a)
b.neighbors.append(c)

c.neighbors.append(root)
c.neighbors.append(b)

solution = Solution()
cn = solution.cloneGraph(root)
print(cn.val, *cn.neighbors)
print(cn.neighbors[0], *cn.neighbors[0].neighbors)
print(cn.neighbors[1], *cn.neighbors[1].neighbors)

