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
        # print(res)
    k = len(res) - 1
    while res[k] == '0':
        k -= 1
    return res[:k+1][::-1]

num1 = '412'
num2 = '315'

print(substract(num1, num2)) # '97'

def subtractStrings_yifan(num1, num2):
    l1, l2 = len(num1), len(num2)
    i, j = l1 - 1, l2 - 1
    borrow = 0
    res = ''
    while i >= 0 or j >= 0:
        n1 = int(num1[i]) if i >= 0 else 0
        n2 = int(num2[j]) if j >= 0 else 0
        cur = n1 - n2 - borrow
        if cur < 0:
            borrow = 1
            cur += 10
        else:
            borrow = 0
        res += str(cur)
        i -= 1
        j -= 1
        # print(res)
    while len(res) > 1 and res[-1] == '0':
        res = res[:-1]
    return res[::-1]

print(subtractStrings_yifan(num1, num2)) # '97'


def addStrings_yifan(num1, num2):
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


def addStrings_decimal(num1, num2):
    '''
    计算“3.2” + “4.56”， 只考虑正数，不需要考虑“+”号。需要考虑不同edge case

    interger: same as addString
    decimal:
    - zero padding so -> 0.20 + 0.56
    - same as addString, add the carrier to the interger side
    '''
    int1, dec1 = num1.split('.')
    int2, dec2 = num2.split('.')

    if len(dec1) < len(dec2):
        # so l1 is longer
        dec1, dec2 = dec2, dec1
    while len(dec2) < len(dec1):
        dec2 += '0'
    print(int1, dec1, int2, dec2)
    len_decimal = len(dec1)

    def addStr(num1, num2, carrier):
        l1, l2 = len(num1), len(num2)
        i, j = l1 - 1, l2 - 1
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

    decimal_sum = addStr(dec1, dec2, 0) 

    int_carrier = 0
    if len(decimal_sum) > len_decimal:
        int_carrier = 1
        decimal_sum = decimal_sum[1:] # carrier to int part
    int_sum = addStr(int1, int2, int_carrier) 
    print(int_sum, decimal_sum)
    return str(int_sum) + '.' + str(decimal_sum)



print(addStrings_decimal('3.2', '4.56')) # 7.76
print(addStrings_decimal('3.5', '4.56')) # 8.06





