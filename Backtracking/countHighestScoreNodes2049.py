class Solution:
    def countHighestScoreNodes(self, parents: List[int]) -> int:
        n = len(parents)
        tree = [[] for _ in parents]
        for i, p in enumerate(parents):
            if p >= 0:
                tree[p].append(i) # add children to the parent
        freq = defaultdict(int) # score : node count
        
        def dfs(node):
            # return size of subtree
            cnt, score = 1, 1
            for child in tree[node]:
                sub_cnt = dfs(child)
                cnt += sub_cnt
                score *= sub_cnt
            score *= n - cnt or 1 # in case zero count
            freq[score] += 1
            return cnt
        
        dfs(0)
        
        return freq[max(freq)]