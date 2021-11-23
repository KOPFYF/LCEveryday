'''
If the length of the string is 11, return an empty string since we cannot create a non-palindromic string in this case.
Iterate over the string from left to the middle of the string: if the character is not a, change it to a and return the string.
If we traversed over the whole left part of the string and still haven't got a non-palindromic string, it means the string has only aa's. Hence, change the last character to b and return the obtained string.

'''

class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        n = len(palindrome)
        if n == 1:
            return ""
        for i in range(n//2):
            if palindrome[i] != 'a':
                return palindrome[:i] + 'a' +  palindrome[i+1:]
        return palindrome[:-1] + 'b' # change last one to b