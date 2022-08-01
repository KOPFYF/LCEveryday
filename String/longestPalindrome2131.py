'''
2 letter words can be of 2 types:

Where both letters are same
Where both letters are different
Based on the above information:

If we are able to find the mirror of a word, ans += 4
The variable unpaired is used to store the number of unpaired words with both letters same.
Unpaired here means a word that has not found its mirror word.
At the end if unpaired same letter words are > 0, we can use one of them as the center of the palindromic string.

'''
class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        # build a 26*26 metrics, find symmetric
        counter, ans = [[0] * 26 for _ in range(26)], 0
        for w in words:
            a, b = ord(w[0]) - ord('a'), ord(w[1]) - ord('a')
            if counter[b][a]: # find a mirror pair
                ans += 4
                counter[b][a] -= 1 # remove mirror
            else: 
                counter[a][b] += 1
        
        for i in range(26):
            if counter[i][i]:
                ans += 2
                break
        return ans