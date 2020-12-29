class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums: 
            return []
        res = []
        dq = deque()  # store index
        for i in range(len(nums)):
            if dq and dq[0] < i - k + 1:  # out of the window
                dq.popleft()
            # like a mono dec stack
            while dq and nums[dq[-1]] < nums[i]:  # remove impossible candidate
                dq.pop()
            dq.append(i)
            if i >= k - 1:
                res.append(nums[dq[0]])
        return res