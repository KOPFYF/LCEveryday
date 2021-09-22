class Solution:
    def maxProduct(self, s: str) -> int:
        '''
        2 <= s.length <= 12
        
        bitmask
        
        ch cases:
        1. belong to p1
        2. belong to p2
        3. does not belong to anyone
        '''
        # improved with a hash table
        mem = {}
        n = len(s)
        for mask in range(1, 1<<n): # index of mask
            tmp = ""
            for j in range(n): # index of char
                if (mask >> j) & 1:
                    tmp += s[j]
            if tmp == tmp[::-1]:
                mem[mask] = len(tmp)
        
        res = 0
        for mask1, x in mem.items():
            for mask2, y in mem.items():
                if mask1 & mask2 == 0:
                    res = max(res, x * y)
        return res
    
    
        # soln 1, TLE on "yyyyyynyyyy"
        n, arr = len(s), []
        for mask in range(1, 1 << n):
            # loop all possible char combination to find all subseq = palindromic
            subseq = ''
            for i in range(n):
                if mask & (1 << i):
                    # 1 means available
                    subseq += s[i]
                if subseq == subseq[::-1]:
                    arr.append((mask, len(subseq)))
                    
        res = 1 # worst case 2 singles
        arr.sort(key=lambda x: x[1], reverse=True) # sort by len
        
        for i in range(len(arr)):
            mask1, len1 = arr[i]
            # break early
            if len1 ** 2 < res: 
                break
            for j in range(i + 1, len(arr)):
                mask2, len2 = arr[j]
                # disjoint
                if mask1 & mask2 == 0 and len1 * len2 > res:
                    res = len1 * len2
                    break # break because sorted from longest
        return res
    
    
        
        # Soln 0, TLE on "mfdfxfdfm"
        # time: O(n*2^n) * O(n*2^n) = O(n^2*2^(2n))
        n, arr = len(s), []
        for mask in range(1, 1 << n):
            # loop all possible char combination to find all subseq = palindromic
            subseq = ''
            for i in range(n):
                if mask & (1 << i):
                    # 1 means available
                    subseq += s[i]
                if subseq == subseq[::-1]:
                    arr.append((mask, len(subseq)))
                    
        res = 1 # worst case 2 singles
        for mask1, len1 in arr:
            for mask2, len2 in arr:
                if mask1 & mask2 == 0: # disjoint
                    res = max(res, len1 * len2)
        return res
        
        