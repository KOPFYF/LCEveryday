class Solution:
    def spiralMatrixIII(self, R: int, C: int, r0: int, c0: int) -> List[List[int]]:
        i, j = r0, c0
        res = [[r0, c0]]
        step_size, sign = 1, 1

        while len(res) < R*C:
            for _ in range(step_size):
                j += sign
                if 0 <= i < R and 0 <= j < C:
                    res.append([i, j])
            
            for _ in range(step_size):
                i += sign
                if 0 <= i < R and 0 <= j < C:
                    res.append([i, j])
            
            step_size += 1 # radius of square, will be 1-1-2-2-3-3
            sign *= -1 # ++ or --
        return res