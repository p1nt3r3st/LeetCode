class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        max_sum = float("-inf")

        def recurse(node):
            nonlocal max_sum
            if not node:
                return 0
            left = max(recurse(node.left), 0)
            right = max(recurse(node.right), 0)

            max_sum = max(max_sum, node.val+left+right)

            return node.val + max(left, right)

        recurse(root)
        return max_sum
