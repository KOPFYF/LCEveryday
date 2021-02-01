class Solution(object):
    def minTransfers(self, transactions):
        """
        :type transactions: List[List[int]]
        :rtype: int
        """
        counter = collections.Counter()
        for f, t, m in transactions:
            counter[f] -= m
            counter[t] += m
        balances = counter.values()
        def dfs(b):
            # input is the unsettled balance, output is the min operation
            if not b: # all settled, 0 operation needed
                return 0
            if not b[0]: # skip 0
                return dfs(b[1:])
            for i in range(1, len(b)):
                if b[i] == -b[0]:
                    return 1 + dfs(b[1:i] + [0] + b[i+1:])
            res = []
            for i in range(1, len(b)):
                if b[i] * b[0] < 0:
                    res.append(dfs(b[1:i] + [b[i]+b[0]] + b[i+1:]))
            return 1 + min(res)

        return dfs(balances)


class Solution2:
    def minTransfers(self, transactions: List[List[int]]) -> int:
        # backtracking + greedy
        # preserve unsettled people only whose net profit != 0.
        # Person X is settled means that X's net profit becomes 0 after one transaction with another unsettled person Y
        # try settle as many people to 0 as possible
        
        # Step 1: Compute net profit for every person
        personNetProfit = defaultdict(int)
        for u, v, w in transactions:
            personNetProfit[u] -= w
            personNetProfit[v] += w
        
        # Step 2: Preserve unsettled people only.
        netProfit = []
        for w in personNetProfit.values():
            if w:
                netProfit.append(w)
          
        # Step 3: Recursion
        n = len(netProfit)
        def dfs(pos, numTrans):
            # skip settled ppl
            while pos < n and netProfit[pos] == 0:
                pos += 1
            if pos + 1 >= n: return numTrans
            
            for i in range(pos + 1, n):
                # greedy
                if netProfit[pos] + netProfit[i] == 0:
                    netProfit[i] += netProfit[pos]
                    minNumTrans = dfs(pos + 1, numTrans + 1)
                    netProfit[i] -= netProfit[pos]
                    return minNumTrans
                minNumTrans = float('inf')
                for i in range(pos + 1, len(netProfit)):
                    # Non-greedy condition for possible closing out in the future.
                    if netProfit[pos] * netProfit[i] < 0:
                        netProfit[i] += netProfit[pos]
                        minNumTrans = min(minNumTrans, dfs(pos + 1, numTrans + 1))
                        netProfit[i] -= netProfit[pos]
                return minNumTrans

        return dfs(0, 0)



class Solution3_bitmask_dp:
    def minTransfers(self, transactions):
        # https://leetcode.com/problems/optimal-account-balancing/discuss/219187/Short-O(N-*-2N)-DP-solution-with-detailed-explanation-and-complexity-analysis
        # Running Time: O(N * 2^N), there are 2^N subproblems, each subproblem contributes to O(N) larger problems.
        # Space: O(2^N)
        persons = collections.defaultdict(int)
        for sender, receiver, amount in transactions:
            persons[sender] -= amount
            persons[receiver] += amount
        
        amounts = [amount for amount in persons.values() if amount != 0]
        
        N = len(amounts)
        dp = [0] * (2**N) # dp[mask] = number of sets whose sum = 0
        sums = [0] * (2**N) # sums[mask] = sum of numbers in mask
        
        for mask in range(2**N):
            set_bit = 1
            for b in range(N):
                if mask & set_bit == 0:
                    nxt = mask | set_bit
                    sums[nxt] = sums[mask] + amounts[b]
                    if sums[nxt] == 0: 
                        dp[nxt] = max(dp[nxt], dp[mask] + 1)
                    else: 
                        dp[nxt] = max(dp[nxt], dp[mask])
                set_bit <<= 1
        
        return N - dp[-1]