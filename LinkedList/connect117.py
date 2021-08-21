"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        node = root
        levelHead = TreeLinkNode(0)
        
        while node: # loop for each level
            needle = levelHead
            
            while node: # loop for current level
                if node.left:
                    # since needle and levelHead points to the same object. That means after needle.next = node.left. 
                    # Same for levelHead.next = node.left. 
                    # this is how levelHead move to next level
                    needle.next = node.left 
                    
                    # needle now points to a different object, not same as levelHead anymore
                    # needle is at node's left child
                    needle = needle.next 
                    
                if node.right:
                    # connect node's left child to right child
                    needle.next = node.right
                    # needle moves to node's right child
                    needle = needle.next
                
                # node moves to its neighbor in the current level
                node = node.next
            
            # this is key part. as said before, levelHead.next = node.left
            # so that node moves to its upper level's leftmost node's left child. meaning the head of this next level
            node = levelHead.next
            
            # levelHead.next is used above, make it to none so that next time it won't grab the same level head again.
            levelHead.next = None


            