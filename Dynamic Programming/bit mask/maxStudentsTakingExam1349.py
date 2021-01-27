'''
bin count:
py embedded function: bit(mask).count('1')
'''

class Solution:
    def maxStudents(self, seats: List[List[str]]) -> int:
        # Bit mask DP
        m, n = len(seats), len(seats[0])
        valid_seats = [0] * m # for each row build a mask
        for i in range(m):
            for j in range(n):
                if seats[i][j] == '.':
                    valid_seats[i] |= (1 << j) 
        def bit_count(n):
            cnt = 0
            while n:
                # # soln 1
                # # 1100 - 0100 = 1000
                # n = n - (n & -n)
                # soln 2
                # 1100 & 1011 = 1000
                n &= (n - 1)
                cnt += 1
            return cnt
        
        @lru_cache(None)
        def dfs(i, prev_mask):
            if i == m: return 0
            res = 0
            # soln 1, range(1 << n) try all 2^n combos
            for mask in range(1 << n):
                if (mask & valid_seats[i]) == mask: 
                    # 1001 & 0111 = 0001, cannot fulfill the mask, similar to submask
                    if mask & (mask << 1) == 0 and \
                        (prev_mask & (mask << 1) == 0 and prev_mask & (mask >> 1) == 0):
                        # 01011 mask
                        # 10110 mask << 1
                        res = max(res, bit_count(mask) + dfs(i + 1, mask))
                    
            # soln 2, submask 1101 1101 => find all submasks like 1001 1001, 3^k(k = number of lines)
            return res
                
        return dfs(0, 0)
            