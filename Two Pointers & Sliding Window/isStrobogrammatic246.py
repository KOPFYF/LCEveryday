class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        maps = {("0", "0"), ("1", "1"), ("6", "9"), ("8", "8"), ("9", "6")}
        i, j = 0, len(num) - 1
        while i <= j:
            if (num[i], num[j]) not in maps:
                return False
            i += 1
            j -= 1
        return True


        # rotated = {'0':'0', '1':'1', '2':'2', '5':'5', '6':'9', '8':'8', '9':'6'}
        rotated = {'0':'0', '1':'1', '6':'9', '8':'8', '9':'6'}
        i, j = 0, len(num) - 1
        while i <= j:
            l, r = num[i], num[j]
            # print(i, j, l, r)
            if l not in rotated or r not in rotated or rotated[l] != r:
                return False
            i += 1
            j -= 1
        return True