class Solution(object):
    def breakPalindrome(self, palindrome):
        """
        :type palindrome: str
        :rtype: str
        
        Change the first non 'a' character to 'a'.
        if the string has only 'a', then change the last character to 'b'.
        """
        n = len(palindrome)
        if n == 1:
            return ""
        
        for i in range(n//2):
            if palindrome[i] != 'a':
                return palindrome[:i] + 'a' + palindrome[i+1:]
        return palindrome[:-1] + 'b' # 'aaaaaaa'