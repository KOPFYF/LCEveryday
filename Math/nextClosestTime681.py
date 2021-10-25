class Solution:
    # https://leetcode.com/problems/next-closest-time/discuss/190816/Python-simple-20ms-solution
    def nextClosestTime(self, time: str) -> str:
        hrs, mins = time.split(':')
        cands = sorted(set(num for num in hrs + mins))
        # print(cands) # ['1', '3', '4', '9']
        two_digits = [a+b for a in cands for b in cands]
        # print(two_digits) # 16 sorted combinations, containing hrs&mins
        
        # check next cand for mins
        i = two_digits.index(mins)
        if i + 1 < len(two_digits) and two_digits[i+1] < "60":
            return hrs + ':' + two_digits[i+1]
        
        # check next cand for hrs, now set mins to smallest
        i = two_digits.index(hrs)
        if i + 1 < len(two_digits) and two_digits[i+1] < "24":
            return two_digits[i+1] + ':' + two_digits[0]
        
        return two_digits[0] + ':' + two_digits[0]