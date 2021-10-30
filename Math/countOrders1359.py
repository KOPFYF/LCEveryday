'''
https://leetcode.com/problems/count-all-valid-pickup-and-delivery-options/discuss/516933/C%2B%2BPython-1-line-Simple-permutation-with-explanation


'''

class Solution:
    def countOrders(self, n: int) -> int:
        # n! * (1 * 3 * 5 * ... * (2n-1)) % 1000000007
        mod = 10**9 + 7
        pickup_permutation = math.factorial(n) % mod
        delivery_permutation = 1
        for i in range(1, 2*n, 2):
            delivery_permutation *= i
        return pickup_permutation * delivery_permutation % mod


'''

https://leetcode.com/discuss/interview-question/1245761/DoorDash-Onsite

Given array of pick up and delivery options, make sure that the array is valid.
Example 1:
Input: ['P1', 'D1']
Output: True
Explanation: P1 comes before D1
Example 2:
Input: ['P2', 'D1', 'P1', 'D2']
Output: False
Explanation: D1 comes before P1, but it should come after.
Note to future solver: Make sure you cover case like P11 and P99 etc. where number followed by P and D is in double digits.
My thoughts: Was able to solve this, got stuck at the P11 test case, they hide the test cases from you, so it's difficult to know/ think of all edge cases. Was able to produce working output.


Given N generate all valid combinations of Pick up and Delivery.
Example:
Input: 1
Output: ['P1', 'D1']
My thoughts: Was able to produce working output without any help for this one using recursion.
'''

def generateValidPickupDeliveriesCombination(n):
    if n is None or n == 0:
        return []
    
    if n == 1:
        return ['P1', 'D1']
    
    res = []
    pickup = set()
    delivery = set()
    dfs(n, [], res, pickup, delivery)

    return res
    

def dfs(n, curr, res, pickup, delivery):

    if len(curr) == n*2:
        res.append(curr)
        return 

    for i in range(n):
        if i not in pickup:
            pickup.add(i)
            dfs(n, curr+['P'+str(i+1)], res, pickup, delivery)
            pickup.remove(i)
        
    for j in range(n):
        if j in pickup and j not in delivery:
            delivery.add(j)
            dfs(n, curr+['D'+str(j+1)], res, pickup, delivery)
            delivery.remove(j)
        
    return



print(generateValidPickupDeliveriesCombination(2))







