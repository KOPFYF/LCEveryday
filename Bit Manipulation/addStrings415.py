class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        l1, l2 = len(num1), len(num2)
        i, j = l1 - 1, l2 - 1
        carrier = 0
        res = ''
        while i >= 0 or j >= 0:
            n1 = int(num1[i]) if i >= 0 else 0
            n2 = int(num2[j]) if j >= 0 else 0
            carrier += n1 + n2
            res += str(carrier % 10)
            carrier //= 10
            i -= 1
            j -= 1
        if carrier:
            res += str(carrier)
        return res[::-1]


# https://leetcode.com/problems/add-strings/discuss/1553409/Facebook-Followup%3A-input-with-negative-numbers-python3

class Solution_fb_follow_up:
    def addStrings(self, num1: str, num2: str) -> str:
        def isGreater(num1, num2):
            # input does not contain sign
            if len(num1) == len(num2):
                if int(num1[0]) == int(num2[0]):
                    return isGreater(num1[1:], num2[1:])
                else:
                    return num1[0] > num2[0]
            else:
                return len(num1) > len(num2)
        
        def add(num1, num2):
            res = ''
            i, j = len(num1) - 1, len(num2) - 1
            plus = 0
            while i >= 0 or j >= 0:
                cur = 0
                if i >= 0 and j >= 0:
                    cur += int(num1[i]) + int(num2[j]) + plus
                    i -= 1
                    j -= 1
                else:
                    if i >= 0:
                        cur += int(num1[i]) + plus
                        i -= 1
                    elif j >= 0:
                        cur += int(num2[j]) + plus
                        j -= 1
                plus = cur // 10
                cur = cur % 10
                res += str(cur)
            if plus:
                res += str(plus)
            return res[::-1]
            
        def substract(num1, num2):
            '''
             412
            -315
            '''

            res = ''
            i, j = len(num1) - 1, len(num2) - 1
            borrow = 0
            while i >= 0 or j >= 0:
                cur = 0
                if i >= 0 and j >= 0:
                    cur = int(num1[i]) - int(num2[j]) - borrow
                    i -= 1
                    j -= 1
                else:
                    if i >= 0:
                        cur += int(num1[i]) - borrow
                        i -= 1
                    elif j >= 0:
                        cur += int(num2[j]) - borrow
                        j -= 1
                if cur < 0:
                    borrow = 1
                    cur = cur + 10
                else:
                    borrow = 0
                res += str(cur)
                print(res)
            k = len(res) - 1
            while res[k] == '0':
                k -= 1
            return res[:k+1][::-1]
        
        if num1[0] != '-' and num2[0] != '-':
            return add(num1, num2)
        
        elif num1[0] == '-' and num2[0] == '-':
            return '-' + add(num1[1:], num2[1:])
        
        else:
            if num1[0] == '-':
                num1, num2 = num2, num1 #keep num1 >= 0 and num2 < 0
            if num1 == num2[1:]:
                return '0'
            
            if isGreater(num1, num2[1:]):
                return substract(num1, num2[1:])
            else:
                return '-' + substract(num2[1:], num1)