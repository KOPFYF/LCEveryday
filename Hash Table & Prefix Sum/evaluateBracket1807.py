class Solution:
    def evaluate(self, s: str, knowledge: List[List[str]]) -> str:
        # Split s into parts, using (. Imagine, that s = (name)is(age)yearsold, 
        # then splitted list will be ['', 'name)is', 'age)yearsold']
        d = {k:v for k, v in knowledge}
        t = s.split("(")
        ans = t[0]
        for i in range(1, len(t)):
            a, b = t[i].split(")")
            ans += d.get(a, "?") + b
        return ans
        
        # hash table O(n)/O(n)
        d = {}
        for k, v in knowledge:
            d[k] = v
         
        res, word, inbracket = [], "", False
        for ch in s:
            if ch == '(':
                inbracket = True
            elif ch == ')':
                res.append(d.get(word, '?'))
                inbracket = False # reset
                word = ''
            elif inbracket:
                word += ch
            else:
                res.append(ch)
        
        return ''.join(res)