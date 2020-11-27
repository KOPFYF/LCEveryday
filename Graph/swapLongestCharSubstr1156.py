class Solution:
    def maxRepOpt1(self, s: str) -> int:
        # Sliding window
        # At each character, check if it is the same as the previous character.
        # If yes,   Increment curr counter by 1.
        # If no,    Try to skip one character and continue expanding.
        # If curr counter is less than the total number of occurences of character in
        # entire string, increment curr counter by 1.
        # Answer = max(Answer, curr counter)
        
        i = res = 0
        count = collections.Counter()
        countChar = collections.Counter(s)
        maxCount, maxChar = 0, s[0]
        
        for j in range(len(s)):
            count[s[j]] += 1
            if count[s[j]] > maxCount:
                maxChar = s[j]
                maxCount = count[s[j]]            
            if j - i + 1 - maxCount > 1:
                # skip one char wont work, inc left ptr
                count[s[i]] -= 1
                i += 1
            res = max(res, j - i + 1)
        return min(res, countChar[maxChar])