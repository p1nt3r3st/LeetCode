class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> list[list[int]]:
        if root:
            queue = [root]
            levels = [[root.val]]
            i = -1
            while queue:
                level_nodes = []
                level_vals = []
                for c in queue:
                    if c.left:
                        level_nodes.append(c.left)
                        level_vals.append(c.left.val)
                    if c.right:
                        level_nodes.append(c.right)
                        level_vals.append(c.right.val)
                if level_vals:
                    levels.append(level_vals[::i])
                i *= -1
                queue = level_nodes.copy()
        else:
            levels = []
        return levels


solution = Solution()
root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.left.left = TreeNode(5)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)
print(solution.zigzagLevelOrder(root))

