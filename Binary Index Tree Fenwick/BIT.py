# https://www.topcoder.com/community/competitive-programming/tutorials/binary-indexed-trees/
'''
BIT => O(logn)/O(logn)

Update: 
i += lowbit(i), i <= n

Query => presum(0, i)
i -= lowbit(i), i > 0
'''

class FenwickTree:
	def __init__(self, n):
		self.sums = [0] * (n + 1)


	def update(self, i, delta):
		# O(logn), go down
		while i < len(self.sums):
			self.sums[i] += delta
			i += self._lowbit(i)


	def query(self, i):
		# O(logn), go up/go to parent
		s = 0
		while i > 0:
			s += self.sums[i]
			i -= self._lowbit(i)
		return s


	def _lowbit(self, x):
		'''
		get rightmost 1,  
		https://www.geeksforgeeks.org/position-of-rightmost-set-bit
		https://stackoverflow.com/questions/31393100/how-to-get-position-of-right-most-set-bit-in-c
		example: x = 112
		// example for get rightmost set bit
		x:             01110000
		~x:            10001111
		-x or ~x + 1:  10010000
		x & -x:        00010000

		// example for unset rightmost set bit
		x:             01110000
		x-1:           01101111
		x & (x-1):     01100000
		'''
		# return x & (~x + 1)
		return x & -x


class Fenwick2:
	def __init__(self, l=[]):                   #initialize the fenwick tree
        self.N = len(l)
        self.BIT = [0 for i in range(self.N)]
        for i in range(1,self.N+1):
            self.update(i, l[i-1])


    def update(self, i, x):                     #add x to the ith position
        while i <= self.x:
            self.BIT[i-1] += x                  #because we're working with an 1-based array 
            i += i & (-i)                       #magic! don't touch!


    def query(self, i):                         #find the ith prefix sum
        s = 0
        while i > 0:
            s += self.BIT[i-1]
            i -= i & (-i)
        return s
    

