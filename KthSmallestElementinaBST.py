class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    kse = None
    i = 0
    next = True

    def dfs(self, node: TreeNode, k: int):
        if node:
            self.dfs(node.left, k)
            self.i += 1
            if self.i == k:
                self.kse = node.val
                self.next = False
            if self.next:
                self.dfs(node.right, k)

    def kthSmallest(self, root: TreeNode, k: int) -> int:
        self.dfs(root, k)
        return self.kse


solution = Solution()
node = TreeNode(13)
node.left = TreeNode(8)
node.left.left = TreeNode(6)
node.left.right = TreeNode(10)
node.right = TreeNode(30)
node.right.left = TreeNode(15)
node.right.left.right = TreeNode(2)
node.right.left.right.left = TreeNode(23)
node.right.right = TreeNode(33)
node.right.right.right = TreeNode(45)
node.right.right.right.left = TreeNode(39)
node.right.right.right.right = TreeNode(49)
print(solution.kthSmallest(node, 5))  # 15
