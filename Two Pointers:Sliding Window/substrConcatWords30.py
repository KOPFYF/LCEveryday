class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        # brute force　O(len(s) * len(word))
        wordDict = Counter(words)
        wordLen, numWords = len(words[0]), len(words)
        totalLen, res = wordLen * numWords, []
        for i in range(len(s) - totalLen + 1):
            seen = defaultdict(int) # reset seen dict for each i
            for j in range(i, i + totalLen, wordLen): # window size is fixed, gap is wordLen
                curWord = s[j:j + wordLen]
                if curWord in wordDict:
                    seen[curWord] += 1
                    if seen[curWord] > wordDict[curWord]:
                        # see enough
                        break
                else:
                    break
            if seen == wordDict:
                res.append(i)
        return res