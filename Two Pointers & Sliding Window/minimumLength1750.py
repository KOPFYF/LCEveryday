class Solution:
    def minimumLength(self, s: str) -> int:
        n = len(s)
        i, j = 0, n - 1
        while i < j:
            # print(i, j)
            if s[i] == s[j]:
                while i < j and s[i] == s[i+1]:
                    i += 1
                while i < j and s[j] == s[j-1]:
                    j -= 1
                i, j = i + 1, j - 1
            else:
                return j - i + 1
        
        return 1  if i == j else 0