'''
Basic idea:

First char of input string is first char of repeated substring
Last char of input string is last char of repeated substring
Let S1 = S + S (where S in input string)
Remove 1 and last char of S1. Let this be S2
If S exists in S2 then return true else false
Let i be index in S2 where S starts then repeated substring length i + 1 and repeated substring S[0: i+1]

The explanation for why that works is pretty straight forward.
Consider a string S="helloworld". Now, given another string T="lloworldhe", 
can we figure out if T is a rotated version of S? Yes, we can! We check if S is a substring of T+T.
Fine. How do we apply that to this problem? We consider every rotation of string S 
such that it's rotated by k units [k < len(S)] to the left. 
Specifically, we're looking at strings "elloworldh", "lloworldhe", "loworldhel", etc...
If we have a string that is periodic (i.e. is made up of strings that are the same and repeat R times), 
then we can check if the string is equal to some rotation of itself, and if it is, 
then we know that the string is periodic. 
Checking if S is a sub-string of (S+S)[1:-1] basically checks 
if the string is present in a rotation of itself for all values of R such that 0 < R < len(S).
'''


class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
    	# soln 0, O(n)
    	return s in (s + s)[1:-1]


    	# soln 1, O(n)
    	# The find() method returns the index of first occurrence of the substring (if found). If not found, it returns -1.
        i = (s + s).find(s, 1)
        return i < len(s)


        # soln 2, O(n*sqrt(n)), no more than O(sqrt(n)) divisors of number n
        N = len(s)
        for i in range(1, N // 2 + 1):
            if N % i == 0 and s[:i] * (N//i) == s:
                return True
        return False