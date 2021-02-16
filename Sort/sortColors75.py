
'''
00...0011...11?......22....22, where ? = 1, 
then we do not need to change any elements, just move mid pointer by 1 to the right.

00...0011...11?......22....22, where ? = 2, 
then we need to put this element befor the first already sorted 2, so we change these elements and then move pointer end by 1 to the left.

00...0011...11?......22....22, where ? = 0, 
then we need to swap this element with the last sorted 0 and also move two pointers mid and beg by 1.
'''


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        ---000--- p0 ---111--- cur --- p2 --222--
        """
        # dutch partitioning problem, 3 pointers
        curr = p0 = 0
        p2 = len(nums) - 1
        while curr <= p2: # stop at nums[curr] = 2, nums[p2] = 1
            # print(nums, p0, curr, p2)
            if nums[curr] == 0:
                nums[curr], nums[p0] = nums[p0], nums[curr]
                p0 += 1
                curr += 1 # 
            elif nums[curr] == 1:
                curr += 1
            else:
                nums[curr], nums[p2] = nums[p2], nums[curr]
                p2 -= 1