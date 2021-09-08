class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        '''
        Characters in one group will always have a lesser attack value than the characters of the           next group. Hence, we will only need to check if there is a higher defense value present in         the next groups.
        '''
        # like 354. Russian Doll Envelopes, sort in 2 dims
        # sort by attack desc, defense asc
        properties.sort(key=lambda x:(-x[0], x[1]))
        # print(properties) # [[6, 3], [5, 5], [3, 6]]
        
        cnt, cur_max = 0, 0
        for _, defense in properties:
            if defense < cur_max:
                cnt += 1 # current property is weak 
            else:
                cur_max = defense
        return cnt
    
        # stack
        properties.sort(key=lambda x: (x[0], -x[1]))
        stack = []
        ans = 0
        
        for a, d in properties:
            while stack and stack[-1] < d: # mono-dec stack
                stack.pop()
                ans += 1
            stack.append(d)
        return ans