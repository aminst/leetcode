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
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        
        def read(vals):
            cur = next(vals)
            if cur == "$":
                return None
            node = TreeNode(int(cur))
            node.left = read(vals)
            node.right = read(vals)
            return node

        vals = iter(data.split())
        root = read(vals)
        return root
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))

"""
Question:
    * unique: no
    * binary tree

BFS:
1
2 3
4 5
how to know nothing?

track how many we added for that parent
store if we have added left or right of parent


Format:
1 2 3 null null 4 5

Add null to queue?

"""
