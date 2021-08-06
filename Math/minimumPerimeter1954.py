'''
For a single area, using the sum of arithmetic progression:
n = 3
[1..n]: n * (n + 1) / 2
[2..n + 1]: n * (n + 1) / 2 + n * 1
[3..n + 2]: n * (n + 1) / 2 + n * 2
[4..n + 3]: n * (n + 1) / 2 + n * 3

So we have n * (n + 1) / 2, then we add n * (n + 1) / 2 times n, then we add n times n * n (n + 1) / 2, which is [n * (n + 1) / 2] * (1 + n + n)

Since we have 4 areas, the final formula looks like this: 2 * n * (n + 1) * (1 + 2 * n).
'''

class Solution:
    def minimumPerimeter(self, neededApples: int) -> int:
        # apple = |x| + |y|
        # constain: square plot centered at 0, 0
        # return: l * 4
        n = 0
        while 2 * n * (n + 1) * (1 + 2 * n) < neededApples:
            n += 1
        return n * 8