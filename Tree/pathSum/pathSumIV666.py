class Solution:
    def pathSum(self, nums: List[int]) -> int:
        # (pos + 1) // 2 to find parent position
        # pos * 2 - 1 to find left, pos * 2 to find right
        # Create a dict of depth and pos
        dic = collections.defaultdict(int)
        for num in nums:
            depth, pos, val = num // 100, (num // 10) % 10, num % 10
            # At each level, store the sum of all the previous nodes covered
            dic[depth, pos] = dic[depth - 1, (pos + 1) // 2] + val
        
        # print(dic)
        res = 0
        for depth, pos in dic.keys():
            # Since the leaf nodes contain sum of the entire path from root to each leaf nodes, just check whether it is a leaf node or not and then add up all the leaf nodes
            if (depth + 1, pos * 2 - 1) not in dic and \
               (depth + 1, pos * 2) not in dic:
                res += dic[depth, pos]
        return res