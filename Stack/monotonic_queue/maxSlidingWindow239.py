class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        '''
        i   num  i - k   dq   res
        0.   1     -3.   [0]   []
        1.   3     -2.   [1]   []
        2.  -1     -1.   [1,2]   [nums[1]] => [3]
        3.  -3     0.   [1,2,3]   [3,3]
        4.   5     1.   [4]   [3,3,5]
        5.   3     2.   [4,5] [3,3,5,5]
        6.   6     3.   [6]   [3,3,5,5,6]
        7.   7.    4.   [7]   [3,3,5,5,6,7]
        
        '''
    
        dq = deque()
        res = []
        for i, num in enumerate(nums):
            # mono dec
            while dq and nums[dq[-1]] < num:
                dq.pop()
            dq.append(i)
            print(dq)
            
            if i - k >= dq[0]:
                dq.popleft()
            
            if i >= k - 1:
                res.append(nums[dq[0]])
                
            print(i, i - k, dq, res)
                
        return res



class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # https://leetcode.com/problems/sliding-window-maximum/discuss/237611/Simplest-O(n)-Python-Solution-with-Explanation
        d = collections.deque()
        out = []
        for i, n in enumerate(nums):
            print("i = {}, curr element = {}, d = {} and out = {}".format(i, n, d, out))
            while d and nums[d[-1]] < n:
                d.pop()
                print("\t Popped from d because d has elements and nums[d.top] < curr element")
            d.append(i)
            print("\t Added i to d")
            if d[0] == i - k:
                d.popleft()
                print("\t Popped left from d because it's outside the window's leftmost (i-k)")
            if i>=k-1:
                out.append(nums[d[0]])
                print("\t Append nums[d[0]] = {} to out".format(nums[d[0]]))
        return out