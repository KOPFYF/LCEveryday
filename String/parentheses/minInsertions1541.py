class Solution:
    def minInsertions(self, s: str) -> int:
        # res represents the number of left/right parentheses already added.
        # right represents the number of right parentheses needed.
        count = 0
        s = s.replace('))', '}')
        open_bracket_count = 0
        
        for ch in s:
            if ch == '(':
                open_bracket_count += 1
            else: 
                if ch == ')':
                    count += 1 # For ) you need to add 1 char to get ))
                
                # Matching ( for } or ))
                if open_bracket_count > 0:
                    open_bracket_count -= 1
                # Need to insert ( to balance string
                else:
                    count += 1 # add a left

        return count + open_bracket_count * 2