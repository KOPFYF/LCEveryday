class Solution(object):
    def pushDominoes(self, dominoes):
        """
        :type dominoes: str
        :rtype: str
        """
        # 2 pointers O(n)
        symbols = [(i, x) for i, x in enumerate(dominoes) if x != '.']
        symbols = [(-1, 'L')] + symbols + [(len(dominoes), 'R')]

        ans = list(dominoes)
        for (i, x), (j, y) in zip(symbols, symbols[1:]):
            # 3 cases, LL(copy), RR(copy), RL(update mid), LR(do nothing)
            if x == y:
                for k in range(i+1, j):
                    ans[k] = x
            elif x > y: #RL
                for k in range(i+1, j):
                    # print(k-i, j-k, cmp(k-i, j-k))
                    # print('.LR'[cmp(k-i, j-k)])
                    # cmp will output 0:., -1:R, 1:L
                    ans[k] = '.LR'[cmp(k-i, j-k)]

        return "".join(ans)
    
    
        # O(n) time O(n) space
        d = 'L' + dominoes + 'R'
        res = ""
        i = 0
        for j in range(1, len(d)):
            if d[j] == '.': 
                continue
            mid = j - i - 1
            # print('mid/2:', mid/2)
            if i: # forbid first one i=0
                res += d[i]
            if d[i] == d[j]:
                res += d[i] * mid
            elif d[i] == 'L' and d[j] == 'R':
                res += '.' * mid
            else:
                res += 'R' * (mid/2) + '.' * (mid % 2) + 'L' * (mid/2)
            i = j
        return res
        
        