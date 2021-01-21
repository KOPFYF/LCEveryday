# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        # iteratively, LIFO
        # the right has to go in first to be printed last later when finished printing the left branch
        stack, res = [root], []
        while stack:
            node = stack.pop()
            if node:
                res.append(node.val)
                stack.append(node.right) # right first
                stack.append(node.left) # then left
        return res

        # recursively
        if not root:
            return []
        res = []
        def preOrder(root):
            if root:
                res.append(root.val)
                preOrder(root.left)
                preOrder(root.right)
        preOrder(root)
        return res
    
'''
Adding two elements to a stack reverses the order when they are popped:

example:
my_list = ["root"]

my_list.append("right") -> my_list = ["root", "right"]
my_list.append("left") -> my_list = ["root", "right", "left"]

value1 = my_list.pop() -> "left", my_list = ["root", "right"]
value2 = my_list.pop() -> "right", my_list = ["root"]

so we put in "right" "left" and got out "left" "right"

'''
                