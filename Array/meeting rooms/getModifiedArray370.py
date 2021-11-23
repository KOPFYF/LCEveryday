class Solution:
    def getModifiedArray(self, length: int, updates: List[List[int]]) -> List[int]:
        # O(n)/O(1)
        res = [0] * length
        
        # like sweep line
        for start, end, inc in updates:
            res[start] += inc
            if end + 1 < length:
                res[end + 1] -= inc
        # print(res)
        for i in range(1, len(res)):
            res[i] += res[i - 1] # presum
        
        return res