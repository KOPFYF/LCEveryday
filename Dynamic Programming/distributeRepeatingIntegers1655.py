class Solution(object):
    def canDistribute(self, nums, quantity):
        """
        :type nums: List[int]
        :type quantity: List[int]
        :rtype: bool
        """
        c = Counter(nums)
        m = len(quantity)
		# we only need at most m different numbers, so we choose the ones which are most abundant
        left = sorted(c.values())[-m:]
        # print(c.values(), left)  
		# If the customer with most quantity required can't be fulfilled, we don't need to go further and answer will be false
        quantity.sort(reverse=True)
        
        def dfs(left, quantity, pos):
            if pos == len(quantity):
                return True
            
            for i in range(len(left)):
                # loop each requirement
                if left[i] >= quantity[pos]:
                    left[i] -= quantity[pos]
                    if dfs(left, quantity, pos + 1):
                        return True
                    left[i] += quantity[pos]
            return False
        
        return dfs(left, quantity, 0)