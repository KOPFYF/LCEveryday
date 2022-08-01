class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        # Stack, O(m+n)/O(m+n)
        def decode(s):
            # O(n)/O(n)
            stack = []
            for ch in s:
                if ch != '#':
                    stack.append(ch)
                elif stack:
                    stack.pop()
            return ''.join(stack)
        
        return decode(s) == decode(t)
    
        # 2 ptrs, O(m+n)/O(1)
        '''
        Iterate through the string in reverse. If we see a backspace character, the next non-backspace character is skipped. If a character isn't skipped, it is part of the final answer.
        '''
        def F(S):
            skip = 0
            for x in reversed(S):
                if x == '#':
                    skip += 1
                elif skip:
                    skip -= 1
                else:
                    yield x

        return all(x == y for x, y in itertools.izip_longest(F(S), F(T)))