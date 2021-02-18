class Solution:
    def consecutiveNumbersSum(self, N: int) -> int:
        '''
        x + (x+1) + (x+2)+...+ (x+k) = N
        kx + k*(k-1)/2 = N implies
        kx = N - k*(k-1)/2
        
        => N - k*(k-1)/2 > 0 => k*(k-1) < 2N => k*k < 2N => k < sqrt(2N)
        So time complexity O(sqrt(N))
        '''
        cnt = 1
        for k in range(2, int((2*N) ** 0.5) + 1):
            if (N - k * (k - 1) // 2) % k == 0:
                cnt += 1
        return cnt