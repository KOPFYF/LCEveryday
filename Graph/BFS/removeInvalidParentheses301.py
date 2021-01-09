class Solution(object):
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        def check(s):
            cnt = 0
            for ch in s:
                if ch == '(': 
                    cnt += 1
                elif ch == ')': 
                    cnt -= 1
                    if cnt < 0:
                        return False
            return cnt == 0
        
        bfs = {s}
        while bfs:
            # the valid answer would appear in the same level of BFS
            valid = filter(check, bfs)
            if valid:
                return valid
            bfs = {s[:i] + s[i+1:] for s in bfs for i in range(len(s))}
            