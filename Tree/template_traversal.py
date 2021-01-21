# https://leetcode.com/problems/binary-tree-postorder-traversal/discuss/45740/Summary-of-preorder-inorder-postorder-four-traversal-ways-for-each

# Recursive Way
# preorder
class Solution(object):
    def preorderTraversal(self, root):
        return ([root.val] + sum(map(self.preorderTraversal, (root.left, root.right)), [])) if root else []

# inorder
class Solution(object):
    def inorderTraversal(self, root):
        if not root:
            return []
        
        left, right = map(self.inorderTraversal, (root.left, root.right))
        return left + [root.val] + right

# postorder
class Solution(object):
    def postorderTraversal(self, root):
        return (sum(map(self.postorderTraversal, (root.left, root.right)), []) + [root.val]) if root else []


# Iterative Way With Stack + Visited State
# preorder
class Solution(object):
    def preorderTraversal(self, root):
        if not root:
            return []

        stack, r = [[root, 0]], []
        while stack:
            top = stack[-1]

            if top[1]:
                stack.pop()
                if top[0].right:
                    stack.append([top[0].right, 0])
            else:
                r.append(top[0].val)
                top[1] = 1

                if top[0].left:
                    stack.append([top[0].left, 0])
        return r

# inorder
class Solution(object):
    def inorderTraversal(self, root):
        if not root:
            return []

        stack, r, poped = [[root, 0]], [], False
        while stack:
            top = stack[-1]

            if top[1]:
                stack.pop()
                poped = True

                if top[0].right:
                    stack.append([top[0].right, 0])
                    poped = False

            elif top[0].left and not poped:
                stack.append([top[0].left, 0])
            else:
                r.append(top[0].val)
                top[1] = 1
        return r

# postorder
class Solution(object):
    def postorderTraversal(self, root):
        if not root:
            return []

        stack, r = [[root, 0]], []
        while stack:
            top = stack[-1]

            if top[1]:
                stack.pop()
                if top[0].left:
                    stack.append([top[0].left, 0])
            else:
                r.append(top[0].val)
                top[1] = 1

                if top[0].right:
                    stack.append([top[0].right, 0])

        return r[::-1]



# Iterative Way With Stack
# preorder
class Solution(object):
    def preorderTraversal(self, root):
        stack, r = [], []
        while stack or root:
            if root:
                stack.append(root)
                r.append(root.val)
                root = root.left
            else:
                root = stack.pop().right
        return r

# inorder
class Solution(object):
    def inorderTraversal(self, root):
        stack, r = [], []
        while stack or root:
            if root:
                stack.append(root)
                root = root.left
            else:
                root = stack.pop()
                r.append(root.val)
                root = root.right
        return r

# postorder
class Solution(object):
    def postorderTraversal(self, root):
        stack, r = [], []
        while stack or root:
            if root:
                r.append(root.val)
                stack.append(root)
                root = root.right
            else:
                root = stack.pop().left

        return r[::-1]


# Morris Traversal Way
# preorder
class Solution(object):
    def preorderTraversal(self, root):
        r = []
        while root:
            if not root.left:
                r.append(root.val)
                root = root.right
            else:
                pre = root.left
                while pre.right and pre.right != root:
                    pre = pre.right

                if not pre.right:
                    r.append(root.val)
                    pre.right = root
                    root = root.left
                else:
                    root = root.right
        return r

# inorder
class Solution(object):
    def inorderTraversal(self, root):
        r = []
        while root:
            if not root.left:
                r.append(root.val)
                root = root.right
            else:
                pre = root.left
                while pre.right and pre.right != root:
                    pre = pre.right

                if not pre.right:
                    pre.right = root
                    root = root.left
                else:
                    r.append(root.val)
                    root = root.right
        return r

# postorder
class Solution(object):
    def postorderTraversal(self, root):
        r = []
        while root:
            if not root.right:
                r.append(root.val)
                root = root.left
            else:
                next = root.right
                while next.left and next.left != root:
                    next = next.left

                if not next.left:
                    r.append(root.val)
                    next.left = root
                    root = root.right
                else:
                    root = root.left
        return r[::-1]