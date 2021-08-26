'''
The company would pay anyway : 
price_A to send a person to the city A, or price_B to send a person to the city B. By sending the person to the city A, the company would lose price_A - price_B, which could negative or positive.

Sort the persons in the ascending order by price_A - price_B parameter, which indicates the company additional costs.

To minimise the costs, send n persons with the smallest price_A - price_B to the city A, and the others to the city B.

'''
class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        # greedy
        n = len(costs) // 2
        costs.sort(key=lambda x: x[0] - x[1])
        res = 0
        for i in range(n):
            res += costs[i][0] + costs[i + n][1]
        return res