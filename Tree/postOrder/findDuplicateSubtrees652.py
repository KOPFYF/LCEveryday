# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: TreeNode) -> List[TreeNode]:
        # PostOrder
        def trv(root):
            if not root: return "#"
            # looks like preorder, but actually for hashmap: left->right->root
            struct = "%s,%s,%s" % (str(root.val), trv(root.left), trv(root.right))
            nodes[struct].append(root)
            return struct
        
        nodes = collections.defaultdict(list)
        trv(root)
        print(nodes)
        return [nodes[struct][0] for struct in nodes if len(nodes[struct]) > 1]
        
        
        # Serializing and hashing the serials of subtrees in the process. 
        # We can recognize a duplicate subtree by its serialization.
        # O(n^2), postorder traversal, inorder would fail!!(cannot distinguish left and right)
        d = defaultdict(int)
        res = []
        def postOrder(cur, hashmap, res):
            if not cur:
                return '#'
            pattern = str(cur.val) + ',' + postOrder(cur.left, hashmap, res) + \
                                ',' + postOrder(cur.right, hashmap, res)
            hashmap[pattern] += 1
            if hashmap[pattern] == 2:
                res.append(cur)
            # print(hashmap)
            # defaultdict(<class 'int'>, {'4,#,#': 1})
            # defaultdict(<class 'int'>, {'4,#,#': 1, '2,4,#,#,#': 1})
            # defaultdict(<class 'int'>, {'4,#,#': 2, '2,4,#,#,#': 1})
            # defaultdict(<class 'int'>, {'4,#,#': 2, '2,4,#,#,#': 2})
            # defaultdict(<class 'int'>, {'4,#,#': 3, '2,4,#,#,#': 2})
            # defaultdict(<class 'int'>, {'4,#,#': 3, '2,4,#,#,#': 2, '3,2,4,#,#,#,4,#,#': 1})
            # defaultdict(<class 'int'>, {'4,#,#': 3, '2,4,#,#,#': 2, '3,2,4,#,#,#,4,#,#': 1, '1,2,4,#,#,#,3,2,4,#,#,#,4,#,#': 1})
            return pattern
        
        postOrder(root, d, res)
        return res
            