class Solution:
    def minAbbreviation(self, target: str, dictionary: List[str]) -> str:
        # soln 1, use code from 320(bt), check match with 2 pointers
        abbr = []
        dictionary = set(dictionary)
        self.generateAbbreviations320(target, 0, [], 0, abbr)
        abbr.sort(key=len) 
        # print(abbr) # list of list, 5, a4, 4e, ap3, ...
        for w in abbr:
            if all(not self.check_ambiguity(w, word) for word in dictionary): 
                return "".join(w)
        return target
  
    def generateAbbreviations320(self, s, pos, path, cnt, ans):
        if pos == len(s):
            ans.append(path + [str(cnt)] if cnt > 0 else path)
            return
        # keep acc count, or reset count to 0 and append
        self.generateAbbreviations320(s, pos+1, path + ([str(cnt)] if cnt else []) + [s[pos]], 0, ans)
        self.generateAbbreviations320(s, pos+1, path, cnt+1, ans)
        
    def check_ambiguity(self, abbr, s):
        # O(max(len(abbr), len(s))) 
        # Decide if abbr can be an abbreviation of s. Compare letter by letter. 
        i = j = 0
        while True:
            if i == len(abbr) and j == len(s): return True
            if i >= len(abbr) or j >= len(s): return False
            if abbr[i].isdigit():
                step = int(abbr[i])
                i += 1
                j += step # jump
            else:
                if abbr[i] != s[j]: return False
                i += 1
                j += 1
        return True


class Solution2_bit_mask:
    '''
    a p p l e
    a m b l e
    1 0 0 1 1


    m a n i p u l a t i o n (word)
    m  2  i p      6      n (abbr)
    1 0 0 1 1 0 0 0 0 0 0 1

    If abbr & word == abbr, then abbr matched word

    '''
    def minAbbreviation(self, target: str, dictionary: List[str]) -> str:
        self.size = len(target)
        self.wlist = [self.toNumber(target, d) for d in dictionary if len(d) == self.size]
        self.ans = (1 << self.size) - 1
        self.length = self.size
        self.dfs(0, 0, 0)
        return self.toWord(self.ans, target)
    
    def dfs(self, number, depth, length):
        if length >= self.length: return
        if depth == self.size:
            if not any(number & w == number for w in self.wlist):
                self.ans = number
                self.length = length
            return
        self.dfs((number << 1) + 1, depth + 1, length + 1)
        if length == 0 or number & 1:
            for x in range(2, self.size - depth + 1):
                self.dfs(number << x, depth + x, length + 1)
                
    def toNumber(self, target, word):
        ans = 0
        for x in range(self.size):
            ans <<= 1
            ans += target[x] == word[x]
        return ans
    
    def toWord(self, number, target):
        ans = ''
        cnt = 0
        for x in range(self.size):
            if number & (1 << self.size - x - 1):
                if cnt:
                    ans += str(cnt)
                    cnt = 0
                ans += target[x]
            else:
                cnt += 1
        return ans + str(cnt or '')