'''
XOR: exclusive or

a ^ b = b ^ a
a ^ (b ^ c) = (a ^ b) ^ c
a ^ 0 = a
a ^ a = 0

a, b equal? <=> a ^ b == 0
0 ^ 1 = 1
1 ^ 1 = 0

num & (num - 1) # 将num（二进制）中最右边的‘1’变成‘0’
num & ^(num - 1) # 提取num（二进制）中最右边的‘1’，其他变成‘0’


print(bin(3)) # '0b11'
print(bin(-3))  # '-0b11'?
-3 should be 011 -> 100 -> 101



Four-bit, positive, two's complement numbers would be 0000 = 0, 0001 = 1, up to 0111 = 7. 
The smallest positive number is the smallest binary value.

Negative numbers always start with a 1. 
The smallest negative number is the largest binary value. 
1111 is -1, 1110 is -2, 1101 is -3, etc down to 1000 which represents -8.

Using two's complement for negative numbers

1. Find the positive binary value for the negative number you want to represent.
2. Add a 0 to the front of the number, to indicate that it is positive.
3. Invert or find the complement of each bit in the number.
4. Add 1 to this number.

Examples
Find -1 using two's complement numbers

1 = 001
Adding 0 to the front becomes 0001
'Inverted' becomes 1110
Add 1 = 1111 (-8 + 4 + 2 + 1 = -1)
Find -4 using two's complement numbers

4 = 100
Adding 0 to the front becomes 0100
'Inverted' becomes 1011
Add 1 = 1100 (-8 + 4 = -4)
'''

num = 6
num2 = num & (num-1)
num3 = num ^ (num-1)
print(num3, num2, bin(num), bin(num - 1), bin(num3), bin(num2))

print(bin(2), bin(1), bin(2 ^ 1) )