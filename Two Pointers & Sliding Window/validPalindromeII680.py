class Solution:
    def validPalindrome(self, s: str) -> bool:
        # iteration
        i, j = 0, len(s) - 1
        while i < j:
            if s[i] != s[j]:
                s1, s2 = s[i:j], s[i+1:j+1] # s1 delete j, s2 delete i
                return s1 == s1[::-1] or s2 == s2[::-1]
            i += 1
            j -= 1
        return True # after all it still match
        
        
        # recursion
        def check_palindrome(s, i, j):
            while i < j:
                if s[i] == s[j]:
                    i += 1
                    j -= 1
                else:
                    return False
            return True
        
        i, j = 0, len(s) - 1
        while i < j:
            if s[i] == s[j]:
                i += 1
                j -= 1
            else:
                # delete one char
                return check_palindrome(s, i+1, j) or check_palindrome(s, i, j-1)
        return True
        
        
        
        # TLE O(n^2)
        if s == s[::-1]:
            return True
        n = len(s)
        for i in range(n):
            s2 = s[:i] + s[i+1:]
            if s2 == s2[::-1]:
                return True
        return False