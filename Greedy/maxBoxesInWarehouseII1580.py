'''
Try to put at least one box in the house pushing it from either side

Once you put one box to the house, you can solve the problem with the same logic used to solve version I. 

You have a warehouse open from the left only and a warehouse open from the right only.

https://leetcode.com/problems/put-boxes-into-the-warehouse-ii/discuss/1069002/Python3-greedy

'''

class Solution:
    def maxBoxesInWarehouse(self, boxes: List[int], warehouse: List[int]) -> int:
        # 2 pointers + greedy, O(n + mlogm) / O(m) -- for sorting or O(1) for sorting in place
        res, i, j = 0, 0, len(warehouse) - 1
        boxes.sort(reverse=True)
        for box in boxes:
            # greedily pushing biggest box on 2 sides. then smallest box will be in the middle
            if i <= j:
                if box <= warehouse[i]:
                    i += 1
                    res += 1
                elif box <= warehouse[j]:
                    j -= 1
                    res += 1
            else:
                break
        return res