# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        def add(node, vals):
            if node == None:
                vals.append("$")
            else:
                vals.append(str(node.val))
                add(node.left, vals)
                add(node.right, vals)
        vals = []
        add(root, vals)
        return ' '.join(vals)
        
