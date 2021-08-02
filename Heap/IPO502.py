'''
The logic is, for each investment, we choose the largest profit from current doable projects, where doable means project's requested capital is no higher than current W.

And our W should keep increasing as capital doesn't decrease when we invest. Therefore, a greedy search can solve the problem by one-pass scan for each project with order of project's capital.

To implement it, we first sort project pair (profit, capital) by capital.

Then for each investment, we push all doable projects (project's capital < W) into a max heap ordered by project's profit. 

Then we just pop the project with the highest project and add its profit to our capital W.
We do it for k times and the maximum capital will be stored in W.
'''

class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        hq = [] # max heap stores profit
        events = sorted(zip(profits, capital), key=lambda x:x[-1]) # sort by capital
        i, n = 0, len(events)
        for _ in range(k):
            while i < n and events[i][1] <= w: # push all candidates
                heapq.heappush(hq, -events[i][0])
                i += 1
            if hq: # greedily pop out the candidate with the biggest profit
                w -= heapq.heappop(hq)
        return w
                