# The rand7() API is already defined for you.
# def rand7():
# @return a random integer in the range 1 to 7


'''
rand7() gives log2(7) bits information, and rand10() need log2(10) bits information. so, in theory, it need call rand7() at least log7(10) times.

use 2 calls of rand7() can generate 1~49 (contains 1~10) which can generate 1 interger of rand10() if we reject 11~49
use 3 calls of rand7() can generate 1~343 (contains 1~100) which can generate 2 interger of rand10() if we reject 101~343
use 4 calls of rand7() can generate 1~2401 (contains 1~1000) which can generate 3 interger of rand10() if we reject 1001~2401
...
use 19 calls of rand7() can generate 1~11398895185373143 (contains 1~10^16) which can generate 16 interger of rand10() if we reject 10^16+1~11398895185373143

If we have less rejection, we will have greater usage of the calls of rand7().

so we can do the math 7^x = 10^y , x/y = log10 / log7 = 1.1833
19/16 is almost close to this value!

so we can use 1.1833 calls of rand7() to get one call of rand10()

'''

class Solution:
    def rand10(self):
        """
        :rtype: int
        """
        
        rand40 = 40
        while rand40 >= 40:
            # (0 - 6) * 7 + (0 - 6) => (0 - 42) + (0 - 6) => (0 - 48), discard 40 ~ 48
            rand40 = (rand7() - 1) * 7 + rand7() - 1
        return rand40 % 10 + 1
        
        res = 11
        while res > 10:
            # (0 - 6) * 7 + (1 - 7) => (0 - 42) + (1 - 7) => (1 - 49), discard 11 ~ 49
            res = (rand7() - 1) * 7 + rand7() 
        return res