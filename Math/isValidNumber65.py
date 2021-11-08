class Solution:
    def isNumber(self, s: str) -> bool:
        '''
        Digits (one of ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
          - seenDigit, at least once
          
        A sign ("+" or "-")
          - first char or after e, e.x. -6e-7
          
        An exponent ("e" or "E")
          - <= 1 occur, seenExp
        
        A dot (".")
          - <= 1 occur, seenDot
          - cannot be after exp
        
        '''
        seenDigit, seenExp, seenDot = False, False, False
        s = s.strip()
        for i, ch in enumerate(s):
            if ch in '+-':
                if i > 0 and s[i-1] != 'e':
                    return False
            elif ch in 'eE':
                if seenExp or not seenDigit:
                    return False # has to see digit before
                seenExp = True
                seenDigit = False # reset to build a new number
            elif ch == '.':
                if seenDot or seenExp:
                    return False
                seenDot = True
            elif ch.isdigit():
                seenDigit = True
            else:
                return False # illegal char
        return seenDigit
            