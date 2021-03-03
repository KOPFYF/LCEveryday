class Solution_bucketsort:
    def maximumGap(self, nums: List[int]) -> int:
        '''
        Thanks for sharing! My understanding: we want to make sure those two numbers forming the maximum difference fall into separate buckets so that we do not need to worry about the numbers in the same bucket. To achieve this we want the size of each bucket to be less than the maximum difference.
        Assuming md denotes the maximum difference, then we have md * (len(nums) - 1) >= b - a, so md >= (b - a) / (len(nums) - 1), since md must be integer, we get md >= math.ceil((b - a) / (len(num) - 1)), thus we make size = math.ceil((b - a) / (len(num) - 1)).
        Then by making the number of buckets to be (b - a) // size + 1, it is guaranteed that the final bucket size is less than maximum difference hence those two numbers forming maximum difference will be in separate buckets.
        Finally, we find the maximum difference between two adjacent buckets (min value of current bucket and max value of previous bucket) and that will be the answer.
        
        '''
        # bucket sort, O(n)
        # two numbers forming the maximum difference fall into separate buckets
        if len(nums) < 2 or max(nums) == min(nums): return 0
        mini, maxi = min(nums), max(nums)
        size = (maxi - mini) // (len(nums) - 1) or 1 # how big is the bucket size?
        # size = (9 - 1) // (4 - 1) = 8 // 3 = 2
        # length of bucket: (9 - 1) // 2 + 1 = 4 + 1 = 5
        bucket = [[float('inf'), float('-inf')] for _ in range((maxi-mini)//size + 1)]
        # print(mini, maxi, size, len(bucket)) 
        
        for n in nums:
            b = bucket[(n - mini) // size]
            b[0] = min(b[0], n)
            b[1] = max(b[1], n)
            # print((n - mini) // size, b)
        
        bucket = [x for x in bucket if x[0] != float('inf')] # get valid buckets
        # print(bucket) # [[1, 1], [3, 3], [6, 6], [9, 9]]
        return max(b[0] - a[1] for a, b in zip(bucket, bucket[1:]))


class Solution_radixsort:
    '''
    https://www.cs.usfca.edu/~galles/visualization/RadixSort.html
    sort based on each digit from Least Significant Bit(LSB) to Most Significant Bit (MSB)

    '''
    def maximumGap(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return 0
        nums = self.radixSort(nums)
        # print(nums)
        res = 0
        for a, b in zip(nums, nums[1:]):
            res = max(res, b - a)
        return res
    
    def radixSort(self, nums):
        for i in range(31):
            one_bucket = []
            zero_bucket = []
            bit = 1 << i
            for j in range(len(nums)):
                if nums[j] & bit != 0:
                    one_bucket.append(nums[j])
                else:
                    zero_bucket.append(nums[j])
            # print('*', nums)
            nums = []
            nums += zero_bucket
            nums += one_bucket
            # print('***', nums)
        return nums