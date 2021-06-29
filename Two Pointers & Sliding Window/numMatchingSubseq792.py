class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        # binary search
        m = dict()
        def isMatch(word, d):
            if word in m:
                return m[word]
            prev = -1
            for w in word:
                i = bisect.bisect_left(d[w], prev + 1)
                if i == len(d[w]):
                    return 0
                prev = d[w][i]
            m[word] = 1
            return 1
        
        d = collections.defaultdict(list)
        for i, char in enumerate(s):
            d[char].append(i)
        ans = [isMatch(word, d) for word in words]
        return sum(ans)
    
    
class Solution1:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:        
        # hash table 500 ms
        word_dict = defaultdict(list)
        count = 0
        
        for word in words:
            word_dict[word[0]].append(word)  
        # print(word_dict)
        
        for char in s:
            # print(word_dict)
            words_expecting_char = word_dict[char]
            word_dict[char] = []
            for word in words_expecting_char:
                if len(word) == 1:
                    # Finished subsequence! 
                    count += 1
                else:
                    word_dict[word[1]].append(word[1:])
        
        return count
        
        
        
class Solution2:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:        
        # two pointers, very slow, 2500 ms
        def check(word, s):
            # O(m + n)
            i, j = 0, 0
            m, n = len(word), len(s)
            if m > n:
                return False
            while i < m and j < n:
                if word[i] == s[j]:
                    i += 1
                    j += 1
                else:
                    j += 1
            # print(i, j, m, n)
            if i == m and j <= n:
                return True
            else:
                return False
            
        # print(check("ace", "abcde"))
        unmatch, match, res = set(), set(), 0
        for word in words:
            if word in unmatch:
                continue
            if word in match:
                res += 1
                continue
            if check(word, s):
                res += 1
                match.add(word)
            else:
                unmatch.add(word)
        # print(match, unmatch)
        return res