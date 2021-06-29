class Solution:
    def findRLEArray(self, encoded1: List[List[int]], encoded2: List[List[int]]) -> List[List[int]]:
        # 2 pointers 
        n1, n2 = len(encoded1), len(encoded2)
        res, i, j = [], 0, 0
        while i < n1 and j < n2:
            freq = min(encoded1[i][1], encoded2[j][1])
            encoded1[i][1] -= freq
            encoded2[j][1] -= freq
            
            val = encoded1[i][0] * encoded2[j][0]
            if res and res[-1][0] == val:
                res[-1][1] += freq
            else:
                res.append([val, freq])
            
            if encoded1[i][1] == 0:
                i += 1
            if encoded2[j][1] == 0:
                j += 1  
        return res
                
        
        
        # TLE on the last test case
        def decode(encode):
            res = []
            for num, cnt in encode:
                res += [num] * cnt
            return res
        
        decode1, decode2 = decode(encoded1), decode(encoded2)
        
        prod = [a * b for a, b in zip(decode1, decode2)]
        # print(decode1, decode2, prod)
        
        res, cnt = [], 1
        prod.append(-1)
        for x, y in zip(prod, prod[1:]):
            if y == x:
                cnt += 1
            else:
                res.append([x, cnt])
                cnt = 1
        return res
                