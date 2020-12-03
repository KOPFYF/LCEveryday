class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        # i_1 < i_2 < i_3 and s_1 < s_3 < s_2
        # keep the value of s3 as big as possible
        # use a "sorted" stack to maintain the candidates of s2 and s3.
        # the numbers in the stack are s2, 
        # the number that popped out is the maximum s3.
        n = len(nums)
        s3 = float('-inf')
        stack = []
        for i in range(n - 1, -1, -1):
            if nums[i] < s3: # find a s1
                return True
            while stack and stack[-1] < nums[i]:
                # at least one number is larger than s3, find s2
                s3 = stack.pop()
            stack.append(nums[i])
        return False