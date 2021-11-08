class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        # binary search
        if num < 2:
            return True
        l, r = 1, num // 2 + 1 # find x*x = num
        while l < r:
            mid = (l + r) // 2
            guess = mid ** 2
            # print(l, r, mid, guess)
            if guess < num:
                l = mid + 1
            elif guess > num:
                r = mid
            else:
                return True
        return False
        
        
        
        return num**0.5 == int(num**0.5)