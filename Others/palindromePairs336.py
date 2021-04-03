class Solution1(object):
    def palindromePairs(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """
        # Case 1: If s1 is a blank string, then for any string that is palindrome s2, s1+s2 and s2+s1 are palindrome.
        # Case 2: If s2 is the reversing string of s1, then s1+s2 and s2+s1 are palindrome.
        # Case 3: If s1[0:cut] is palindrome and there exists s2 is the reversing string of s1[cut+1:] , then s2+s1 is palindrome.
        # Case 4: Similiar to case3. If s1[cut+1: ] is palindrome and there exists s2 is the reversing string of s1[0:cut] , then s1+s2 is palindrome.
        
        res, d = [], {word: i for i, word in enumerate(words)}
        
        for i, s1 in enumerate(words):
            s1_rev = s1[::-1]
            if s1 == s1_rev and s1 != '' and '' in d: 
                # case 1, empty string
                res.append([i, d[""]])
                res.append([d[""], i])
                
            if s1 != s1_rev and s1_rev in d:
                # case 2: s1 = s2[::-1]
                res.append([i, d[s1_rev]])
                # res.append([d[s2], i]) # dont overcount!
                
            for j in range(1, len(s1)):
                s1_l, s1_r = s1[:j], s1[j:]
                s1_l_rev, s1_r_rev = s1_l[::-1], s1_r[::-1]
                if s1_l == s1_l_rev and s1_r_rev in d:
                    res.append([d[s1_r_rev], i])
                if s1_r == s1_r_rev and s1_l_rev in d: # not elif!!
                    res.append([i, d[s1_l_rev]])
        
        return res


class Solution2(object):
    def palindromePairs(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """

        dicts = {}
        for i, word in enumerate(words):
            dicts[word[::-1]] = i
        
        def isPalindrome(s):
            return s == s[::-1]
        
        res = set()
        for i, word in enumerate(words):
 
            for j in range(len(word) + 1): # to cover the case of empty string 
                # for the empty string
                left = word[:j]
                right = word[j:]
                # case 1: 
                if isPalindrome(left) and (right in dicts) and (i != dicts[right]): # make sure left != right
                    res.add((dicts[right], i))
                # case 2:
                if isPalindrome(right) and (left in dicts) and (i != dicts[left]):
                    res.add((i, dicts[left]))
        return res


a = ''
print(a[:0], '*', a[0:]) # a[:0] is '', a[0:] is ''
b = 'abc'
print(b[:4], '*', b[4:]) # b[:4] is full string, b[4:] is ''
            
