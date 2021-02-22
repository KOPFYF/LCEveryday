# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''
Traverse the binary tree by level order;
If the current node has left and right child, pop it out, and add both of its children into the queue; otherwise, insert new node as its child;
repeat the above till encounter the first node that does NOT have two children.
'''
class CBTInserter:

    def __init__(self, root: TreeNode):
        self.root = root
        self.dq = collections.deque([root]) # overwrite level by level
        while self.dq[0].right: # if right exists, left must exist
            node = self.dq.popleft()
            self.dq += [node.left, node.right]
        # print(self.dq, len(self.dq))

    def insert(self, v: int) -> int:
        parent = self.dq[0]
        # print(parent)
        if parent.left:
            parent.right = TreeNode(v) 
            # print(parent, parent.left, parent.right)
            self.dq += [parent.left, parent.right]
            self.dq.popleft() # popout current parent
        else:
            parent.left = TreeNode(v)    
        return parent.val

    def get_root(self) -> TreeNode:
        return self.root