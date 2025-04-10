class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    net_nodes = {}

    def create_nodes(self, node: TreeNode):
        if not node.left and not node.right:
            pass
        elif node.left and not node.right:
            self.net_nodes[node.left] = node
            self.create_nodes(node.left)
        elif node.right and not node.left:
            self.net_nodes[node.right] = node
            self.create_nodes(node.right)
        else:
            self.net_nodes[node.left] = node
            self.net_nodes[node.right] = node
            self.create_nodes(node.left)
            self.create_nodes(node.right)

    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        self.create_nodes(root)
        result = root
        p_way = {}
        node = p
        while node != root:
            p_way[node] = 1
            node = self.net_nodes[node]

        node = q
        run = True
        while node != root and run:
            if node in p_way:
                result = node
                run = False
            else:
                node = self.net_nodes[node]
        return result
