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