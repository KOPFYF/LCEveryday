class Solution:
    def bulbSwitch(self, n: int) -> int:
        # A bulb ends up on if it is switched an odd number of times.
        # Bulb i is switched in round d if and only if d divides i
        # So bulb i ends up on if and only if it has an odd number of divisors.
        '''
        i = 12
        all divisiors: 1,12, 2,6, 3,4 (6 divisiors in total)
        
        i = 36:
        all divisiors: 1,36, 2,18, 3,12, 4,9, 6,6 (6 double!!, 9 divisiors)
        
        So bulb i ends up on if and only if i is a square
        So just count the square numbers.
        '''
        
        return int(sqrt(n))