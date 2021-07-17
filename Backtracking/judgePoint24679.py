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