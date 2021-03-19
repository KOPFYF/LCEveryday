'''
We start to delievery boxes from each A[i],
and we load boxes from A[i] to A[j] as many as possible.
Also we record the biggest lastj that has the same port target,
that is A[lastj][0] = A[j][0].

dp[i] means the number trips we need to finish the first i boxes.
Note that we can calulated dp[i] for each i,
but here we apply a greediest solution and a second greediest solution,
we don't calculate and we don't need all dp[i] in this process.
'''

class Solution:
    def boxDelivering(self, boxes: List[List[int]], portsCount: int, maxBoxes: int, maxWeight: int) -> int:
        # dp + sliding win, O(n)/O(n)
        n = len(boxes)
        
        # dp records the minimal number of the trips to deliver i box
		# dp[1] means we delivered the first (0th) box
        dp = [0] + [float('inf')] * n
        
        # need: needed trips from i to j for this shipment
        need, j, last_j = 0, 0, 0
        for i in range(n):
            while j < n and maxBoxes > 0 and maxWeight >= boxes[j][1]:
                maxBoxes -= 1
                maxWeight -= boxes[j][1]
                
                # if switch to the new port
                if j == 0 or boxes[j][0] != boxes[j - 1][0]: 
                    # we need to add the number of needed trip by 1
					# lastj moves to current position to mark the start of boxes with different ports
                    lastj = j
                    need += 1
                j += 1
                
            # greedies solution: if we keep loading as far right as we can
            dp[j] = min(dp[j], dp[i] + need + 1)
            
            # second greedies solution: if we decide to sacrifice a little weight to save a trip
            # dp[j] = min(dp[j], dp[i] + need + 1);
            # And we don't deliver A[lastj] ... A[j], so we save one trip
            dp[lastj] = min(dp[j], dp[i] + need) # corner case
            
            maxBoxes += 1
            maxWeight += boxes[i][1]
            
            # if this box is different from the prior box
			# we removed the prior box, so the needed trip is reduced by 1.
            if i == n - 1 or boxes[i][0] != boxes[i + 1][0]:
                need -= 1
                
        return dp[-1]