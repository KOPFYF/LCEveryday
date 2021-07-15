'''
Observation I
If there is only one '?', Alice will win. Alice have at least one choice to make the sum uneven.

Observation II
If Alice play last, Alice will win. Same as Observations I.

Observation III
Now we have even number of '?', say they are on left and right. Alice pick first '?', Bob should pick '?' on the other side with same number to cancel out Alice's move. Repeat this until all '?' are on one side.

Now the problem becomes: can Alice and Bob pick to make up the difference between left sum and right sum.

Observation IV
If there are only 2 '?' left, the difference has to be 9 for Bob to win. Because no matter what Alice choose, Bob can pick one to make 9. This means, at any rounds, whatever Alice pick, Bob can counter and make the pair sum 9. [0,9] [1,8] [2,7] [3,6] [4,5]

Final Observation V
If there are 4 '?' left, then the difference has to be 18 for Bob to win.

'''
class Solution:
    def sumGame(self, num: str) -> bool:
        # 2 <= num.length <= 10**5
        n = len(num) // 2
        left, right, lcnt, rcnt = 0, 0, 0, 0
        for i, ch in enumerate(num):
            if 0 <= i < n:
                if ch == '?':
                    lcnt += 1
                else:
                    left += int(ch)
            else:
                if ch == '?':
                    rcnt += 1
                else:
                    right += int(ch)
        res = left - right + (lcnt - rcnt) * 4.5 # ? expection is 4.5
        return res != 0
    
#         if lcnt + rcnt == 0:
#             return left != right
#         if left == right:
#             return (lcnt + rcnt) % 2 == 1
        
#         if left > right:
#             gap = left - right

                