A = [1,2,3,4,5,6]
import collections
d = collections.defaultdict(int)
for a in A:
	for b in A:
		for c in A:
			d[a + b + c] += 1
print(d)

