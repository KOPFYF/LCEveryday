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
        preorder traversal and preorder decompose
        """
        encode = []
        def preorder(node):
            if not node:
                encode.append('#')
            else:
                encode.append(str(node.val))
                preorder(node.left)
                preorder(node.right)
            
        preorder(root)
        return ','.join(encode)
            
                
    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        # print(data)
        vals = deque(data.split(","))
        def build(vals):
            if not vals:
                return
            val = vals.popleft()
            if val == '#': # null node
                return
            else:
                node = TreeNode(val)
                node.left = build(vals)
                node.right = build(vals)
                return node
        
        return build(vals)

        
class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        encode = []
        def preorder(node):
            if not node:
                encode.append('#')
            else:
                encode.append(str(node.val))
                preorder(node.left)
                preorder(node.right)
        preorder(root)
        return ','.join(encode)
                
    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        vals = deque(data.split(","))
        def build(vals):
            if not vals:
                return None
            val = vals.popleft()
            if val == '#':
                return None
            else:
                root = TreeNode(int(val))
                root.left = build(vals)
                root.right = build(vals)
            return root
        
        return build(vals)
                    
            
        
            

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))