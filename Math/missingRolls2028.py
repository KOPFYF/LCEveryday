class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        m = len(rolls)
        curSum = sum(rolls)
        missingSum = mean * (n + m) - curSum
        if missingSum < n or missingSum > 6*n: 
            return []

        part, rem = divmod(missingSum, n)
        ans = [part] * n
        for i in range(rem):
            ans[i] += 1
        return ans