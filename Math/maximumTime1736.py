class Solution:
    def maximumTime(self, time: str) -> str:
        time = list(time)
        for i in range(len(time)): 
            if time[i] == "?": 
                if i == 0: 
                    time[i] = "2" if time[i+1] in "?0123" else "1"
                elif i == 1: 
                    time[i] = "3" if time[0] == "2" else "9"
                elif i == 3: 
                    time[i] = "5"
                else: 
                    time[i] = "9"
        return "".join(time)

class Solution:
    def maximumTime(self, time: str) -> str:        
        res = [t for t in time]
        if time[0] == '?' and time[1] == '?':
            res[0] = '2'
            res[1] = '3'
        # first bit
        if time[0] == '?' and '4' <= time[1] <= '9':
            res[0] = '1'
        elif time[0] == '?' and '0' <= time[1] <= '3':
            res[0] = '2'
        # 2nd bit
        if time[0] in ('0', '1') and time[1] == '?':
            res[1] = '9'
        elif time[0] == '2' and time[1] == '?':
            res[1] = '3'
        
        # 3rd bit
        if time[3] == '?':
            res[3] = '5'
        # 4th bit
        if time[4] == '?':
            res[4] = '9'

        return "".join(res)
                