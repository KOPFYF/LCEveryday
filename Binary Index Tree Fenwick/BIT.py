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



