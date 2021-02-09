class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        def dfs(s1, s2, s):
            # s1 is the first number. s2 is the second number. s is the remaining number.
            if len(s1) > 1 and s1[0] == '0':
                return False
            if len(s2) > 1 and s2[0] == '0':
                return False
            if not s:
                return True
            s3 = str(int(s1) + int(s2))
            if s.startswith(s3):
                return dfs(s2, s3, s[len(s3):])
            else:
                return False
        
        for i in range(len(num) - 2):
            for j in range(i + 1, len(num) - 1):
                if dfs(num[:i+1], num[i+1:j+1], num[j+1:]):
                    return True
        return False