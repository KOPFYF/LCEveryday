'''
sorted by frequency from highest to lowest. 
If two words have the same frequency, then the word with the lower alphabetical order comes first.

so for min heap it's (freq, -alphabetical), pop out smallest freq
'''

class Solution1:
    def topKFrequent(self, words, k):
        ctr = collections.Counter(words)
        max_len = len(max(ctr.keys(), key = len)) # longest word length
        # print(ord('a'), ord('z')) # (97, 122)
        # print(ctr, max_len, ord(" ")) 
        # (Counter({u'i': 2, u'love': 2, u'coding': 1, u'leetcode': 1}), 8, 32)
        q = [(-float('inf'), tuple(), '') for _ in range(k)]
        for word, count in ctr.items():
        	# # need padding, this is wrong for ["a","aa","aaa"]
         #    heapq.heappushpop(q, \
         #                      (count, tuple(-ord(c) for c in list(word)), \ 
         #                       word))
            heapq.heappushpop(q, \
                              (count, tuple(-ord(c) for c in list(word + ' '*(max_len-len(word)))), \
                               word))
        return [word for (_, _, word) in sorted(q, reverse=True)]


class Solution2:
    # heap, time O(nlogk) 48 ms, Space O(n), 13.5 MB  
    def topKFrequent(self, words, k):
        count = collections.Counter(words)
        heap = [] # maintain a min heap
        for key, value in count.items():
            heapq.heappush(heap, Word(value, key)) 
            if len(heap) > k: # if heap size == k, pop out the smallest one
                heapq.heappop(heap)
        res = []
        for _ in range(k):
            res.append(heapq.heappop(heap).word)
        return res[::-1]

class Word:
    def __init__(self, freq, word):
        self.freq = freq
        self.word = word
    
    def __lt__(self, other):
        # order by alpha if tie
        if self.freq == other.freq:
            return self.word > other.word
        # order by freq
        return self.freq < other.freq
    
    def __eq__(self, other):
        return self.freq == other.freq and self.word == other.word
            