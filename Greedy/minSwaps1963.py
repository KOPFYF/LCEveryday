'''
        greedy, (min. swaps) = (mismatches + 1) / 2
        decrease it at most by 2: for this we need to take the leftest ] with negative balance
        and the rightest [ with negative balance and change them. For example in our case we have:
        ]]][]]][[[[[ : [-1, -2, -3, -2, -3, -4, -5, -4, -3, -2, -1, 0]
        
        []][]]][[[[] : [1, 0, -1, 0, -1, -2, -3, -2, -1, 0, 1, 0]

        [][[]]][][[] : [1, 0, 1, 2, 1, 0, -1, 0, -1, 0, 1, 0]

        [][[]][[]][] : [1, 0, 1, 2, 1, 0, 1, 2, 1, 0, 1, 0]


'''
class Solution:
    def minSwaps(self, s: str) -> int:
        cnt, mismatch = 0, 0
        for symb in s:
            if symb == "[": 
                cnt -= 1
            else: 
                cnt += 1
            mismatch = max(cnt, mismatch)
        return (mismatch + 1) // 2