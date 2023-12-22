# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, root, k): # the value if found, the number of nodes seen
        if not root: return None, 0
        left_found, left_count = self.dfs(root.left, k)
        if left_found is not None:
            return left_found, k
        if k - left_count == 1:
            return root.val, k
        right_found, right_count = self.dfs(root.right, k - left_count - 1)
        return right_found, left_count + 1 + right_count
        

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        return self.dfs(root, k)[0]

"""

"""
