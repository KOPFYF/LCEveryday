class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        # josephus problem 
        # https://leetcode.com/problems/find-the-winner-of-the-circular-game/discuss/1152585/O(n)-(no-simulation)-The-classic-josephus-problem-with-explanation
        p = 1
        for i in range(1, n): 
            # here i represent number of alive persons
            p = (p + k - 1) % (i + 1) + 1
        return p
    
    
        arr = list(range(n))
        i = 0
        while len(arr) > 1:
            i = (i + k - 1) % len(arr) # get index of k to kick out, e.x. k = 2 kick idx = 1
            arr.pop(i) # O(n)
        
        return arr[0] + 1
            