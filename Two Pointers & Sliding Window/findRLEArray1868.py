class Solution:
    def findRLEArray(self, encoded1: List[List[int]], encoded2: List[List[int]]) -> List[List[int]]:
        # 2 ptrs, O(m + n) all unique
        m, n = len(encoded1), len(encoded2)
        i, j = 0, 0
        res = []
        while i < m and j < n:
            num1, freq1 = encoded1[i]
            num2, freq2 = encoded2[j]
            freq = min(freq1, freq2)
            num = num1 * num2
            
            encoded1[i][1] -= freq
            encoded2[j][1] -= freq
            
            if encoded1[i][1] == 0:
                i += 1
            if encoded2[j][1] == 0:
                j += 1
            
            if not res or res[-1][0] != num:
                res.append([num, freq])
            else:
                res[-1][1] += freq
        
        return res