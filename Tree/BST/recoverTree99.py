class Solution: 
    def recoverTree(self, root): # O(lg(n)) space
        pre = first = second = None
        stack = []
        while True:
            while root:
                stack.append(root)
                root = root.left
            if not stack:
                break
            node = stack.pop()
            if not first and pre and pre.val > node.val:
                first = pre
            if first and pre and pre.val > node.val:
                second = node
            pre = node
            root = node.right
        first.val, second.val = second.val, first.val

 
class Solution1:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        # inorder travese should give us increasing order
        # 1-2-3-4-5
        # 1-4-3-2-5
        # first = 4, second = 2
        
        res = [] # space/time O(n + logn)
        self.dfs(root, res)
        first, second = None, None
        for i in range(len(res)-1):
            if res[i].val > res[i+1].val and not first:
                first = res[i]
            if res[i].val > res[i+1].val and first:
                second = res[i+1]
        first.val, second.val = second.val, first.val
        
    def dfs(self, root, res):
        # O(depth)
        if root:
            self.dfs(root.left, res)
            res.append(root)
            self.dfs(root.right, res)


class Solution2:
    def recoverTree(self, root: TreeNode) -> None:
        firstElement, secondElement, prevElement = None, None, TreeNode(float('-inf'))
        def inOrder(root):
            nonlocal firstElement, secondElement, prevElement
            # nonlocal secondElement
            # nonlocal prevElement
            if not root: 
                return
            inOrder(root.left)
            # If first element not found, assign it to prevElement 
            if not firstElement and prevElement.val >= root.val:
                firstElement = prevElement
            # If first element is found, assign the second element to the root
            if firstElement and prevElement.val >= root.val:
                secondElement = root
            prevElement = root
            inOrder(root.right)
        
        inOrder(root)
        firstElement.val, secondElement.val = secondElement.val, firstElement.val