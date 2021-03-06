class Solution:
    def compress(self, chars: List[str]) -> int:
        '''
        2 pointers
        
        case 1:
        a      c
        lag  lead
             new_lag
             
        case 2:
        a    a    a    c
        lag           lead
        set (this part) to the size
        a   3   c
               new_lag/new_lead
        '''
        # soln1
        i, j = 0, 0
        while j < len(chars):
            ch, cnt = chars[j], 0
            while j < len(chars) and chars[j] == ch:
                j += 1
                cnt += 1
            chars[i] = ch
            i += 1
            if cnt > 1:
                for num in str(cnt):
                    chars[i] = num
                    i += 1
        return i
                
                
        # soln2
        lag = lead = 0
        while lead < len(chars):
            while lead < len(chars) and chars[lead] == chars[lag]:
                lead += 1
            if lead - lag == 1:
                lag = lead # group size is 1, move left pointer to the next
            else:
                # print(str(lead - lag))
                chars[lag + 1 : lead] = str(lead - lag)
                lag = lag + 1 + len(str(lead - lag))
                lead = lag
            # print(chars)
            # ['a', '2', 'b', 'b', 'c', 'c', 'c']
            # ['a', '2', 'b', '2', 'c', 'c', 'c']
            # ['a', '2', 'b', '2', 'c', '3']
