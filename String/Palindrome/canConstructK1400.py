'''
If the s.length < k we cannot construct k strings from s and answer is false.

If the number of characters that have odd counts is > k then the minimum number of palindrome strings 
we can construct is > k and answer is false.

Otherwise you can construct exactly k palindrome strings and answer is true (why ?).


'''

class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        n = len(s)
        if n < k:
            return False
        cnt = Counter(s)
        odd_cnt = 0
        for ch, freq in cnt.items():
            if freq & 1:
                odd_cnt += 1
                if odd_cnt > k:
                    return False
        return True