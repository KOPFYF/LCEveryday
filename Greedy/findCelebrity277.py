# The knows API is already defined for you.
# return a bool, whether a knows b
# def knows(a: int, b: int) -> bool:

class Solution:
    def findCelebrity(self, n: int) -> int:
        # all the other n - 1 people know him/her
        # but he/she does not know any of them
        cand = 0
        for i in range(n):
            if knows(cand, i):
                cand = i
        # after this cand should know nobody
        # if celebrity exist, it must be cand!
        # double check again, if not meet, return -1 in the loop
        for i in range(n):
            if i != cand:
                if not knows(i, cand) or knows(cand, i):
                    return -1
        return cand
        