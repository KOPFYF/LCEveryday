class Solution:
    def decodeCiphertext(self, encodedText: str, m: int) -> str:
        # O(mn)
        n = len(encodedText) // m
        res = []
        for i in range(n):
            while i < len(encodedText):
                # s[i] and s[i+cols+1] are adjacent characters in original text.
                res.append(encodedText[i])
                i += n + 1
        return ''.join(res).rstrip()
        
        
        mn = len(encodedText)
        n = mn // m
        dic = defaultdict(str)
        for i in range(m):
            for j in range(n):
                dic[j - i] += encodedText[i*n + j]
        # print(dic)
        res = ''
        for k, chunk in dic.items():
            if k >= 0 and chunk:
                res += chunk
        return res.rstrip()