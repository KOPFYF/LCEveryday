'''
Given the input

"abcde"
["a","bb","acd","ace"]
Create a word dict to keep track of prefix -> candidates

{
  "a": ["a", "acd", "ace"],
  "b": ["bb"]
}
Go through each char in s and find candidates that start with char. The candidate has length of 1, then we found one of the subsequences

For char "a", we found these candidates

["a", "acd", "ace"]
Only "a" is a subsequence, then we increment count
Then we update the word dict by:

taking out all the candidates start with "a" becuase we have processed them
add new candidates with the prefix "a" removed, aka ["cd", "ce"]
{
  "a": [],
  "b": ["bb"],
  "c": ["cd", "ce"]
}
Keep repeating until the input s is processed.

'''

class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        res = 0
        trie = defaultdict(list)
        for word in words:
            trie[word[0]].append(word[1:])
            
        for ch in s:
            leftover = trie[ch]
            trie[ch] = [] # mark as seen
            for suffix in leftover:
                if not suffix:
                    res += 1
                else:
                    trie[suffix[0]].append(suffix[1:])
        
        return res