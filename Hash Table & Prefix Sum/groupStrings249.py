class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        dic = defaultdict(list)
        
        for word in strings:
            encode = []
            for ch in word[1:]:
                encode.append((ord(ch) - ord(word[0])) % 26)
            dic[tuple(encode)].append(word)
        
        # print(dic)
        return list(dic.values())