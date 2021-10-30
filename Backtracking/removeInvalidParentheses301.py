class Solution(object):
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        def check(s):
            # return unmatched left & right count, O(n)
            left = 0
            for ch in s:
                if ch == '(':
                    left += 1
                elif ch == ')':
                    if left > 0:
                        left -= 1
                    else:
                        return False
            return left == 0
        
        bfs = {s}
        while True:
            res = []
            for path in bfs:
                if check(path):
                    res.append(path)
            if res:
                return res
            nxt_bfs = set()
            for path in bfs:
                for i in range(len(path)):
                    nxt_bfs.add(path[:i] + path[i+1:])
            bfs = nxt_bfs



class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        '''
        Generate all valid parentheses from string s, we can memoize them to avoid re-compute sub-problem again. It's the same idea with 140. Word Break II.
Then get the maximum length among those valid parentheses.
Filter the result by choosing parentheses which has the length equals to the maximum length.
        '''
        
        @cache
        def dfs(i, bal):
            res = set()
            if bal < 0:
                return res # invalid
            if i == len(s):
                if bal == 0:
                    res.add("") # base case
                return res
            if s[i] == '(' or s[i] == ')':
                res.update(dfs(i+1, bal)) # case 1, skip current parentheses
            
            # case 2, use parenthese
            if s[i] == '(':
                bal += 1
            elif s[i] == ')':
                bal -= 1
            for path in dfs(i+1, bal):
                res.add(s[i] + path)
            return res
        
        combs = dfs(0, 0)
        # print(combs)
        max_res = max(combs, key=len)
        max_len = len(max_res)
        # print(max_len)
        ans = []
        for path in combs:
            if len(path) == max_len:
                ans.append(path)
        return ans


class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        def dfs(s, i, left, right):
            if left == right == 0 and valid(s)[0] == valid(s)[1] == 0: 
                # nothing to remove
                res.append(s)
                return
            for j in range(i, len(s)):
                if j > i and s[j] == s[j - 1]: # dedup
                    continue
                if s[j] == "(" and left > 0: # remove left
                    dfs(s[:j] + s[j + 1:], j, left - 1, right)
                if s[j] == ")" and right > 0: # reemove right
                    dfs(s[:j] + s[j + 1:], j, left, right - 1)
        
        def valid(word):
            left, right = 0, 0
            for ch in word:
                if ch == "(":
                    left += 1
                if ch == ")": # could cancel out
                    right = right + 1 if left == 0 else right
                    left = left - 1 if left > 0 else left
            # print(left, right)
            return [left, right]
        
        res = []
        dfs(s, 0, valid(s)[0], valid(s)[1])
        return res

class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        res = []
        self.remove(s, res, 0, 0, ('(', ')'))
        return res
    
    def remove(self, s, res, last_i, last_j, par):
        count = 0
        for i in xrange(last_i, len(s)):
            count += (s[i] == par[0]) - (s[i] == par[1])
            if count >= 0:
                continue
            for j in xrange(last_j, i + 1):
                if s[j] == par[1] and (j == last_j or s[j - 1] != par[1]):
                    self.remove(s[:j] + s[j + 1:], res, i, j, par)
            return
        reversed_s = s[::-1]
        if par[0] == '(':
            self.remove(reversed_s, res, 0, 0, (')', '('))
        else:
            res.append(reversed_s)