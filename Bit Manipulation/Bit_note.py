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
'''

num = 6
num2 = num & (num-1)
num3 = num ^ (num-1)
print(num3, num2, bin(num), bin(num - 1), bin(num3), bin(num2))

print(bin(2), bin(1), bin(2 ^ 1) )