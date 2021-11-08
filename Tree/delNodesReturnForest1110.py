# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
        # BFS, O(n)/O(n)
        to_delete = set(to_delete)
        res = []
        bfs = deque([(root, True)])
        while bfs:
            node, parent_delete = bfs.popleft()
            root_deleted = node.val in to_delete
            if parent_delete and not root_deleted:
                res.append(node)
            
            if node.left:
                bfs.append((node.left, root_deleted))
                if node.left.val in to_delete:
                    node.left = None
            if node.right:
                bfs.append((node.right, root_deleted))
                if node.right.val in to_delete:
                    node.right = None
        return res

class Solution:
    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:    
        # DFS, O(n)/O(h + n)
        to_delete = set(to_delete)
        res = []
        
        def dfs(root, parent_delete):
            if not root: 
                return None
            root_deleted = root.val in to_delete
            
            if parent_delete and not root_deleted:
                # parent deleted, node itself not
                res.append(root)
            
            root.left = dfs(root.left, root_deleted)
            root.right = dfs(root.right, root_deleted)
            return None if root_deleted else root
        
        dfs(root, True)
        return res


class Solution:
    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
        to_delete = set(to_delete)
        res = []
        
        def dfs(root, parent_exist):
            # return root itself after deleting
            if not root:
                return None
            if root.val in to_delete:
                # delete current root
                root.left = dfs(root.left, False)
                root.right = dfs(root.right, False)
                return None # root is deleted, so return none
            else:
                # keep current root
                if not parent_exist: 
                    # parent does not exist, so it's a new node
                    res.append(root)
                root.left = dfs(root.left, True)
                root.right = dfs(root.right, True)
                return root
        dfs(root, False)
        return res