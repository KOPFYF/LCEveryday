'''
Interval DP

https://leetcode.com/problems/remove-boxes/discuss/1402561/C%2B%2BJavaPython-Top-down-DP-Clear-explanation-with-Picture-Clean-and-Concise

This is really a hard problem, so feel free to enjoy it if you can't solve this problem. I will try my best to explain in the easiest way.
Let dp(l, r, k) denote the maximum points we can get in boxes[l..r] if we have extra k boxes which is the same color with boxes[l] in the left side.
For example: boxes = [3, 3, 1, 3, 3]
The dp(l=3, r=4, k=2) is the maximum points we can get in boxes[3..4] if we have extra 2 boxes the same color with boxes[3] in the left side, it's the same as we find the maximum points in boxes = [3, 3, 3, 3].
Since (a+b)^2 > a^2 + b^2, where a > 0, b > 0, so it's better to greedy to remove all contiguous boxes of the same color, instead of split them.
So we increase both l and k while boxes[l+1] == boxes[l].
Now, we have many options to consider:
Option 1, remove all boxes which has the same with boxes[l], total points we can get is dp(l+1, r, 0) + (k+1)*(k+1) (k left boxes and the lth box have the same color)
Other options, we try to merge non-contiguous boxes of the same color together, by:
Find the index j, where l+1 <= j <= r so that boxes[j] == boxes[l].
Total points we can get is dp(j, r, k+1) + dp(l+1, j-1, 0)
Choose the option which has the maximum score we can get.

'''

class Solution:
    def removeBoxes(self, boxes: List[int]) -> int:
        # O(n^4) / O(n^3)
        @cache
        def dp(l, r, k):
            if l > r: 
                return 0
            
            while l + 1 <= r and boxes[l] == boxes[l + 1]:  
                # Increase both `l` and `k` if they have consecutive colors with `boxes[l]`
                l += 1
                k += 1
            
            ans = (k+1) * (k+1) + dp(l+1, r, 0)  # Remove all boxes which has the same with `boxes[l]`
            for m in range(l + 1, r + 1):  # Try to merge non-contiguous boxes of the same color together
                if boxes[l] == boxes[m]:
                    ans = max(ans, dp(m, r, k+1) + dp(l+1, m-1, 0))
            return ans

        return dp(0, len(boxes) - 1, 0)