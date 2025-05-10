class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    is_valid = True
    previous_num = None

    def dfs(self, node: TreeNode):
        if node:
            self.dfs(node.left)
            if self.previous_num is not None and self.previous_num >= node.val:
                self.is_valid = False
            self.previous_num = node.val
            if self.is_valid:
                self.dfs(node.right)

    def isValidBST(self, root: TreeNode) -> bool:
        self.dfs(root)
        return self.is_valid


solution = Solution()
node = TreeNode(13)
node.left = TreeNode(8)
node.left.left = TreeNode(6)
node.left.right = TreeNode(10)
node.right = TreeNode(30)
node.right.left = TreeNode(15)
node.right.left.right = TreeNode(29)
node.right.left.right.left = TreeNode(23)
node.right.right = TreeNode(33)
node.right.right.right = TreeNode(45)
node.right.right.right.left = TreeNode(39)
node.right.right.right.right = TreeNode(49)
print(solution.isValidBST(node))  # True
