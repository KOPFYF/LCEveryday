class Solution:
    def smallestFactorization(self, a: int) -> int:
        # 48 = 1*48 = 2*24 = 3*16 = 4*12 = 6*8(ans)
        # 15 = 1*15 = 3*5
        res = []
        def dfs(num):
            # return True if we can decomp num
            # in the meantime find all divisor
            if num == 1: return True
            for n in range(9, 1, -1):
                if num % n == 0:
                    res.append(str(n))
                    return dfs(num // n)
            return False
        
        flag = dfs(a)
        # print(res) # res = [] if a = 1
        num = int("".join(sorted(res))) if res else 1
        # input 18000000, output 2555555889 but should return 0
        return num if flag and -(2 ** 31) <= num <= 2 ** 31 - 1 else 0