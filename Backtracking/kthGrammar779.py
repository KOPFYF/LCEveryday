class Solution:
    def kthGrammar(self, N: int, K: int) -> int:
#         backtracking
#         We see that, for any level N, the first half of the string is the same as the string in N-1, 
#         the next half is just complement of it. The total number of items in level N is 2^N. 
#         The half mark of the string is marked by [2^(N-1)]-th item. So, for any level N:

#         if K is in the first half, it is same as the Kth element in level N-1
#         if K is in the second half, it is the complement of the number in [K-2^(N-1)]-th position in level N-1
        if N == 1:
            if K == 1:
                return 0
            else:
                return 1
            
        half = 2 ** (N - 1)
        if K <= half:
            return self.kthGrammar(N - 1, K)
        else:
            res = self.kthGrammar(N - 1, K - half) # complement
            if res == 0:
                return 1
            else:
                return 0
        
        # TLE, We don't need to actually generate the strings "0110..."
        n, k = N - 1, K - 1
        def dfs(n):
            if n == 0:
                return ["0"]
            last_row = dfs(n - 1)
            res = []
            for bit in last_row:
                if bit == "0":
                    res += ["0", "1"]
                else:
                    res += ["1", "0"]
            return res
        
        s = dfs(n)
        return s[k]