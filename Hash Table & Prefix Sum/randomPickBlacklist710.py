'''
Soln 3 (Hash table Remapping) O(B) processing - O(1) pick/O(B)
Optimal Solution!

Hash map blacklisted value in [0, N-len(blacklist)) to whitelisted value in [N-len(blacklist), N), and then randomly pick number in [0, N-len(blacklist)).

NNNNN
-BB--
W--WW

=>

NNNNN
W(W)(W)--
---(B)(B)
'''
from random import randint
class Solution:

    def __init__(self, N: int, blacklist: List[int]):
        blacklist = set(blacklist)  # to avoid TLE
        self.W = N - len(blacklist) # to be used in pick()
        key = [x for x in blacklist if x < N - len(blacklist)]
        val = [x for x in range(N - len(blacklist), N) if x not in blacklist]
        self.mapping = dict(zip(key, val))
        # print(self.mapping)

    def pick(self) -> int:
        i = randint(0, self.W - 1)
        return self.mapping.get(i, i)


'''
Soln 1 (TLE): while list
Time Complexity: O(N) preprocessing. O(1) pick. Preprocessing is too slow to pass the time limit.
Space Complexity: O(N). MLE (Memory Limit Exceeded) will occur.

Soln 2 (Binary Search) O(BlogB) - O(logB) / O(B)
full list(F): n numbers from 0 to n-1
blacklist(B): m numbers
whitelist(W): n - m numbers, index from 0 to n - m - 1

F: ----------
B: - -- - --
          (mid)
W:  -  - -  -
      (k)
pick one from whitelist by find the largest B[mid] less than the W[k]

Soln 3 (Hash table Remapping) O(B) processing - O(1) pick/O(B)
Optimal Solution!
Treat the first N - |B| numbers as those we can pick from. Iterate through the blacklisted numbers and map each of them to to one of the remaining non-blacklisted |B| numbers

For picking, just pick a random uniform int in 0, N - |B|. If its not blacklisted, return the number. If it is, return the number that its mapped to
'''

class Solution2:
    # binary search

    def __init__(self, n: int, blacklist: List[int]):
        self.blacklist = sorted(blacklist)
        self.n = n
        self.m = len(blacklist)

    def pick(self) -> int:
        #target find kth white list value 0,1, ...,k
        k = random.randint(0, self.n - self.m - 1)
        l, r = 0, self.m
        
        # find the largest B[mid] less than the W[k]
        while l < r:
            mid = (l + r) // 2
            if self.blacklist[mid] - mid <= k:
                # B[mid]−mid, the number of whitelist numbers less than B[\text{mid}]B[mid]
                l = mid + 1
            else:
                r = mid
        
        if l >= self.m:
            return k + self.m
        else:
            return k + l
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(n, blacklist)
# param_1 = obj.pick()