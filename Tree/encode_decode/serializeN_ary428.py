"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Codec:
    def serialize(self, root: 'Node') -> str:
        """Encodes a tree to a single string.
        
        :type root: Node
        :rtype: str
        """
        encode = []
        def preorder(root):
            if not root: return None
            encode.append(str(root.val))
            encode.append("[")
            for child in root.children:
                preorder(child)
            encode.append("]")
        preorder(root)
        # print(' '.join(encode))
        return ','.join(encode)
            
        
    def deserialize(self, data: str) -> 'Node':
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: Node
        """
        if not data: return None
        vals = deque(data.split(','))
        val = vals.popleft()
        root = Node(int(val), [])
        def build(root):
            if vals.popleft() == '[':
                child = vals.popleft()
                while child != ']':
                    childNode = Node(int(child), [])
                    root.children.append(build(childNode))
                    child = vals.popleft()
                return root
        return build(root)