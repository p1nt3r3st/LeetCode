class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root: TreeNode) -> list[int]:
        most_right = []
        available_nodes = [root]

        if not root:
            pass
        else:
            while len(available_nodes) != 0:
                most_right.append(available_nodes[-1].val)
                extend_nodes = []
                for i in range(len(available_nodes)):
                    work_node = available_nodes.pop(0)
                    if work_node.left:
                        extend_nodes.append(work_node.left)
                    if work_node.right:
                        extend_nodes.append(work_node.right)
                available_nodes.extend(extend_nodes)

        return most_right


solution = Solution()
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.right = TreeNode(5)
root.right.right = TreeNode(4)
print(solution.rightSideView(root))
