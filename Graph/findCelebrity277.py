# The knows API is already defined for you.
# return a bool, whether a knows b
# def knows(a: int, b: int) -> bool:

class Solution:
    def findCelebrity(self, n: int) -> int:
        # celebrity: indegree = n - 1, 2 <= n <= 100, n == graph[i].length
        # There will be exactly one celebrity 
        
        # pick out the candidate. If candidate knows i, then switch candidate
        # after this the candidate will not know anyone
        candidate = 0
        for i in range(1, n):
            if knows(candidate, i):
                candidate = i
           
        # check whether the candidate is real
        for i in range(n):
            # all the other n - 1 people know him/her
            # but he/she does not know any of them
            if i != candidate and (knows(candidate, i) or not knows(i, candidate)):
                return -1
        return candidate