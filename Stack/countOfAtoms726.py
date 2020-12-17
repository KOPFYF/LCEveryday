class Solution:
    def countOfAtoms(self, formula: str) -> str:
        d = defaultdict(int)
        atom = ''
        stack = []
        cnt = i = 0
        prod = 1
        for c in formula[::-1]:
            if c.isdigit(): 
                cnt += int(c) * (10 ** i)
                i += 1
            elif c.islower():
                atom += c
            else:
                if c == ')':
                    # prod for multi-layers, forward   
                    stack.append(cnt or 1)
                    prod *= cnt or 1      
                elif c == '(':
                    # prod for multi-layers, backward   
                    prod = prod // stack.pop() 
                elif c.isupper(): # He, Mg
                    atom += c
                    d[atom[::-1]] += cnt * prod if cnt else prod
                    atom = '' # reset atom only when see Cap
                i = cnt = 0 # reset cnt if not see lower case            
            # print(cnt, i, prod, atom, stack, d)
    
        return "".join(k + str(v if v > 1 else "") for k, v in sorted(d.items()))