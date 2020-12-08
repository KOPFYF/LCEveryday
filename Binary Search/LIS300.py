class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Patience sorting
        # tails is an array storing the smallest tail of all increasing subsequences with length i+1 in tails[i]
        tails = []
        for h in nums:
            idx = bisect.bisect_left(tails, h)
            # if x is larger than all tails, append it, increase the size by 1
            if idx == len(tails):
                tails.append(h)
            # if tails[i-1] < x <= tails[i], update tails[i]
            else:
                tails[idx] = h
            # print(tails)
            # Input: [10,9,2,5,3,7,101,18]
            # [10]
            # [9]
            # [2]
            # [2, 5]
            # [2, 3]
            # [2, 3, 7]
            # [2, 3, 7, 101]
            # [2, 3, 7, 18]

        return len(tails)