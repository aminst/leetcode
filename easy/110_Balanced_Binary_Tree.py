# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def helper(root):
            if not root:
                return True, 0
            left_is_balanced, left_max_depth = helper(root.left)
            right_is_balanced, right_max_depth = helper(root.right)
            return (
                left_is_balanced and
                right_is_balanced and
                abs(left_max_depth - right_max_depth) <= 1
            ), max(left_max_depth, right_max_depth) + 1

        return helper(root)[0]
