class Solution {
    public int characterReplacement(String s, int k) {
        int[] cnt = new int[26];
        int maxCnt = 0, i = 0, maxSize = 0;
        
        for (int j = 0; j < s.length(); j++) {
            cnt[s.charAt(j) - 'A']++;
            maxCnt = Math.max(maxCnt, cnt[s.charAt(j) - 'A']); // most frequent char
            
            int winSize = j - i + 1;
            if (winSize - maxCnt > k) {
                // we have considered changing more than k charactres. So time to shrink window
                cnt[s.charAt(i) - 'A']--;
                i++;
            }
            maxSize = Math.max(maxSize, j - i + 1);
        }
        
        return maxSize;
    }
}

// Python version
/*
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        d = defaultdict(int)
        maxCnt = i = res = 0
        
        for j, ch in enumerate(s):
            d[ch] += 1
            maxCnt = max(maxCnt, d[ch]) # capture most frequent one in the window
            if (j - i + 1 - maxCnt > k):
                d[s[i]] -= 1
                i += 1
            res = max(res, j - i + 1)
            
        return res
*/