class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)
        s = sum(cardPoints)
        if k >= n:
            return s
        l, res, runsum = n - k, 0, sum(cardPoints[:n-k])
        for i in range(k+1):
            res = max(res, s - runsum)
            # print(i, s, runsum, res)
            if i + l < n:
                runsum -= cardPoints[i]
                runsum += cardPoints[i + l]
        
        return res