class Solution(object):
    def numberWays(self, hats):
        """
        :type hats: List[List[int]]
        :rtype: int
        """
        # O(40 * 2^n * n), n <= 10
        memo = {}
        return self.dfs(hats, 0, 0, memo)

    def dfs(self, hats, pos, state, memo):
        n = len(hats)
        N = (1 << n) - 1
        mod = 10 ** 9 + 7

        if (pos, state) in memo:
            return memo[(pos, state)]
        if state == N: # base case found!
            return 1
        if pos > 40: # no more hats to process
            return 0

        # dont assign hat(pos) to anyone, just move to the nxt ptr
        res = self.dfs(hats, pos + 1, state, memo)
        # try assign hat(pos) to each person, and update state 
        for i in range(n): 
            if pos in hats[i] and state & (1 << i) == 0:
                # current hat in person i's list
                # state & (1 << i) == 0: person i not assigned yet
                res += self.dfs(hats, pos + 1, state ^ (1 << i), memo)

        memo[(pos, state)] = res
        return res % mod
    

class Solution2:
    def numberWays(self, hats: List[List[int]]) -> int:   
        # Bottom up DP, O(40 * 2^n * n)
        hat2ppl = defaultdict(set)    
        mod, N = 10 ** 9 + 7, 1 << len(hats)
        
        for p, hats_i in enumerate(hats):
            for h in hats_i: 
                hat2ppl[h].add(p)     
        # print(hat2ppl) # defaultdict(<class 'set'>, {3: {0}, 4: {0, 1}, 5: {1, 2}})
        
        dp = [0] * N
        dp[0] = 1
        for h in hat2ppl:
            # assign hat h to people
            for state in range(N - 1, -1, -1):
                for p in hat2ppl[h]: 
                    # loop all people applicable to that hat h
                    if state & (1 << p) == 0:  
                        # if current person can be added to the state, add him: state ^ (1 << p)
                        dp[state ^ (1 << p)] = (dp[state ^ (1 << p)] + dp[state]) % mod                        
        return dp[-1]

        