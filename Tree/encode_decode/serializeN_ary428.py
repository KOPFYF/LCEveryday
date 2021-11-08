"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


Serialize with preorder traversal where sentinel "#" indicates the final child of a node has been processed, so the function returns to its parent call.
Deserialize by creating a deque (could also use an iterator with next() instead of popleft()).
While the next item is not "#", create a child with the item, add the child to the list of children and recurse to create its subtree.
Repeat until there are no more children, then ignore the "#".
"""
# https://leetcode.com/problems/serialize-and-deserialize-n-ary-tree/discuss/150790/Python-O(n)-recursive-both-functions

class Codec:
    def serialize(self, root):  
        serial = []

        def preorder(node):
            if not node:
                return
            serial.append(str(node.val))
            for child in node.children:
                preorder(child)
            serial.append("#")      # indicates no more children, continue serialization from parent
        preorder(root)
        return " ".join(serial)

    def deserialize(self, data):    
        print(data)
        if not data:
            return 

        tokens = deque(data.split())
        root = Node(int(tokens.popleft()), [])

        def build(node):
            if not tokens:
                return
            while tokens[0] != "#": # add child nodes with subtrees
                value = tokens.popleft()
                child = Node(int(value), [])
                node.children.append(child)
                build(child)
            tokens.popleft()        # discard the "#"

        build(root)
        return root







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