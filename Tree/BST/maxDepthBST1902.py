import sortedcontainers

class Solution:
    def maxDepthBST(self, order: List[int]) -> int:
        # python way for binary treemap
        depths = sortedcontainers.SortedDict()
		# add dummy bounds to avoid extra ifs
        depths[-math.inf] = 0
        depths[math.inf] = 0
        
		# for every value find bounds and take the lowest depth + 1
		# put the value back to depths
        for x in order:
            i = depths.bisect_left(x)
            # There are at most 2 possible places where a new node can be inserted
            depths[x] = 1 + max(depths.values()[i - 1:i + 1])
        # return the maximum value so far
        return max(depths.values())