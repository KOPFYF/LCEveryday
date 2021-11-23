'''
Just check every character from right to left
if character is digit, add to current numeric counter
if character is ")", multiply big coefficient and add numeric counter to stack
if character is "(", we won't multiply next elements with last numeric counter so remove last counter and divide big coefficient by last counter
if character is alphabetic and uppercase, we have to add element and its coefficient to dictionary
if character is alphabetic and lowercase, just add character to current element.
return string by joining sorted key and value pairs in dictionary

'''
class Solution:
    def countOfAtoms(self, formula: str) -> str:
        dic, stack = defaultdict(int), []
        prod = 1
        atom = ''
        cnt = i = 0
        for c in formula[::-1]:
            if c.isdigit():
                cnt += int(c) * (10**i)
                i += 1
            elif c == ')':
                stack.append(cnt or 1)
                prod *= cnt or 1
                i = cnt = 0
            elif c == '(':
                prod //= stack.pop()
                i = cnt = 0
            elif c.isupper():
                atom += c
                dic[atom[::-1]] += prod * (cnt or 1)
                atom = ''
                i = cnt = 0
            elif c.islower():
                atom += c
        
        res = ''
        for k, v in sorted(dic.items()):
            if v == 1:
                v = ''
            res = res + k + str(v)
        return res



class Solution:
    def countOfAtoms(self, formula: str) -> str:
        # recursion O(n^2)/O(n), stack O(n)/O(n)
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