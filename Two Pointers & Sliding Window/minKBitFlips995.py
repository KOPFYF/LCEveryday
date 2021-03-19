'''
cur means the number of flips in the current sliding window of size K.
cur should be number of flips contributed by A[i-K+1], ..., A[i - 1], because flipping the windows starting with these indices will also flip A[i]
cur是i-K+1~i-1之间的棋子，一共翻了多少次
If cur is even and A[i] is 0, we need to flip.
If cur is odd and A[i] is 1, we need to flip.

'''

class Solution:
    def minKBitFlips(self, A: List[int], K: int) -> int:
        # sliding win O(n)
        cur = 0
        res, n = 0, len(A)
        for i in range(n):
            if i >= K and A[i - K] == 2: # i >= k, could start flipping, 
                cur -= 1 # since i - K is flipped, nxt window wont be impacted, recover cur then
            # if cur & 1 ^ A[i] == 0:
            if (cur % 2) == A[i]: 
                # cur is even, cur % 2 = 0, A[i] = 0, we need to filp
                # cur is odd, cur % 2 = 1, A[i] = 1, we need to flip
                if i + K > n: # no enough space to flip all
                    return -1
                A[i] = 2 # after flip, set it to flipped state(2)
                cur, res = cur + 1, res + 1
            # print(i, cur,  A)
            # 0 1 [2, 0, 0, 1, 0, 1, 1, 0]
            # 1 1 [2, 0, 0, 1, 0, 1, 1, 0]
            # 2 1 [2, 0, 0, 1, 0, 1, 1, 0]
            # 3 0 [2, 0, 0, 1, 0, 1, 1, 0]
            # 4 1 [2, 0, 0, 1, 2, 1, 1, 0]
            # 5 2 [2, 0, 0, 1, 2, 2, 1, 0]
            # 6 2 [2, 0, 0, 1, 2, 2, 1, 0]
            # 7 1 [2, 0, 0, 1, 2, 2, 1, 0]
        return res