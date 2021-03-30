class Solution:
    def maxSum(self, nums1: List[int], nums2: List[int]) -> int:
        # topo sort, O(m + n)
        graph, indeg = defaultdict(list), defaultdict(int)
        m, n = len(nums1), len(nums2)
        
        for a, b in zip(nums1, nums1[1:]):
            graph[a].append(b)
            indeg[b] += 1
        for a, b in zip(nums2, nums2[1:]):
            graph[a].append(b)
            indeg[b] += 1
            
        bfs, scores = deque(), defaultdict(int) 
        for num in graph:
            if not indeg[num]:
                bfs.append((num, num)) # num, score
                scores[num] = num
        
        res = 0
        while bfs:
            num, score = bfs.popleft()
            res = max(res, score)
            for nxt_num in graph[num]:
                indeg[nxt_num] -= 1
                # init nxt score, take max because there could be 2 indegs from before
                scores[nxt_num] = max(scores[nxt_num], score) 
                if not indeg[nxt_num]:
                    bfs.append((nxt_num, nxt_num + scores[nxt_num]))
        return res % (10**9 + 7)