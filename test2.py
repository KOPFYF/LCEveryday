def numberToBase(n, k):
    if n == 0:
        return [0]
    digits = []
    while n:
        digits.append(int(n % k))
        n //= k
    return digits[::-1]

base_10_palindrom = set()
for i in range(1, 10**8):
    if str(i) == str(i)[::-1]:
        base_10_palindrom.add(i)
print(len(base_10_palindrom), base_10_palindrom)