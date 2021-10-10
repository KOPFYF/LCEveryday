
class Solution:
    def judgePoint24(self, cards: List[int]) -> bool:
        '''
        cards.length == 4
        1 <= cards[i] <= 9
        I actually just realized that there is in fact an input where simple floats fail, namely [3, 3, 8, 8]. 
        Floats calculate 23.999999999999989341858963598497211933135986328125 instead of 24. It's not in the judge's test suite, but it should be soon (Edit: it now is). 
        Using Fraction however made my solution exceed the time limit, so I settled for the above approximation solution.
        '''

        if len(cards) == 1:
            # return cards[0] == 24 # fail on [3,3,8,8], 8 / (3 - 8/3) = 8 / (1/3) = 24
            return round(cards[0], 2) == 24 # have to round to check division


        for i, a in enumerate(cards):
            for j, b in enumerate(cards):
                if i == j:
                    continue
                nxt_cards = [c for k, c in enumerate(cards) if k != i and k != j]
                ops = {a + b, abs(a - b), a*b}
                if a:
                    ops.add(b/a)
                if b:
                    ops.add(a/b)
                for nxt_num in ops:
                    if self.judgePoint24(nxt_cards + [nxt_num]):
                        print(nxt_cards + [nxt_num])
                        return True
        return False

class Solution:
    # backtracking: 4 -> 3 -> 2 -> 1
    # each step we randomely select 2 numbers and try 4 operations
    # [Comb(4, 2) + Comb(3, 2) + Comb(2, 2)] * operations, operations = 5
    
    def judgePoint24(self, cards: List[int]) -> bool:
        # '/' represents real division, not integer division
        if len(cards) == 1:
            return round(cards[0], 2) == 24
        for (i, a), (j, b) in itertools.combinations(enumerate(cards), 2):
            # try all possible pairs
            new_cards = [x for idx, x in enumerate(cards) if i != idx and j != idx]
            
            # just try any 2 pairs with 4 kinds of operations
            ops = {a + b, abs(a - b), a * b}
            if b: # divided by 0
                ops.add(a / b)
            if a:
                ops.add(b / a)
            for new_num in ops:
                if self.judgePoint24(new_cards + [new_num]):
                    return True
        return False