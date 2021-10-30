from collections import defaultdict
class Solution:
    def verticalOrder(self, root: TreeNode) -> List[List[int]]:
        # BFS, O(n)/O(n), no sorting
        if not root:
            return
        dic = defaultdict(list)
        miny, maxy = 0, 0
        bfs = deque([(root, 0)]) # node, y
        while bfs:
            node, y = bfs.popleft()
            dic[y].append(node.val)
            miny, maxy = min(miny, y), max(maxy, y)
            if node.left:
                bfs.append((node.left, y - 1))
            if node.right:
                bfs.append((node.right, y + 1))
        return [dic[y] for y in range(miny, maxy + 1)]



class Solution(object):
    def verticalOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        # DFS with sorting, slow!
        dic = defaultdict(list)
        def dfs(node, x, y):
            if not node:
                return
            dic[(x, y)].append(node.val)
            dfs(node.left, x + 1, y - 1)
            dfs(node.right, x + 1, y + 1)
        dfs(root, 0, 0)
        
        prev_y = float('-inf')
        positions = sorted(dic.keys(), key=lambda x:(x[1], x[0]))
        # print(dic, positions)
        res = []
        for x, y in positions:
            if y != prev_y:
                # new level y:
                res.append(dic[x, y])
                # res.append(sorted(dic[x, y]))
            else:
                res[-1] += dic[x, y]
                # res[-1] += sorted(dic[x, y])
            prev_y = y
        return res



