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