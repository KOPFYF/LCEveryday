'''
        1
       / \
      1   2
     / \ / \
    1  2 3  4
'''

class Solution(object):
    def pathSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # (pos + 1) // 2 to find parent position
        # pos * 2 - 1 to find left, pos * 2 to find right
        d = defaultdict(int)
        for num in nums:
            depth, pos, val = num // 100, (num // 10) % 10, num % 10
            d[depth, pos] = d[depth - 1, (1+pos) // 2] + val
        
        res = 0
        for depth, pos in d.keys():
            if (depth + 1, pos * 2 - 1) not in d.keys() and (depth + 1, pos * 2) not in d.keys():
                res += d[depth, pos]
        return res