class Solution(object):
    def backspaceCompare(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        
        Case 1: 当值等于`#`, `count`增值
        Case 2: 如果`count == 0` 说明这个值没有被`#`给抵消，返回
        Case 3: 如果`count != 0` 切这个值不为`#`，这个值要被`#`抵消掉
        """  
    
        # O(1) space
        # iterate through the string in reverse
        m, n = len(s), len(t)
        i, j = m - 1, n - 1
        
        def getChar(s, i):
            char = ''
            cnt = 0
            while i >= 0 and not char:
                if s[i] == '#':
                    cnt += 1
                elif cnt == 0:
                    char = s[i]
                else:
                    cnt -= 1
                i -= 1
            return char, i

        
        while i >= 0 or j >= 0:
            char1, char2 = '', ''
            if i >= 0:
                char1, i = getChar(s, i)
            if j >= 0:
                char2, j = getChar(t, j)
            # print(i, j, char1, char2)
            if char1 != char2:
                return False
        return True