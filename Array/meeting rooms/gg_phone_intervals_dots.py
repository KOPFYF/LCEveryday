'''
题目很简单 输入两个list: intervals 和 dots

像meeting room那种 intervals = [[1,5],[3,7],[9,15], [10,13] 表示数轴上的一段段区间
dots就是一系列点 比如[2,3,6,8,10,15]

问你每个点在几个区间里
比如输入的是[2,3,6,8,10,15] 就返回[1, 2, 6, 0, 2, 1]

两个follow up
一个是有有字母怎么处理 比如在intervals加上区间['b', 'g'] ['k','p'] 然后输入里加上例如 ['a','f','l']
第二个是输入的点变为小数怎么处理

'''

from collections import defaultdict

def meeting_rooms(intervals, arr):
	events = defaultdict(int)
	for s, e in intervals:
		events[s] += 1
		events[e] -= 1

	print(events)
	cnt = 0 
	i = 0
	res = [0] * len(arr)
	for key in sorted(events.keys()):
		while arr[i] < key:
			res[i] = cnt 
			i += 1
		cnt += events[key]
	print(res)
	return res



intervals = [[1,5],[3,7],[9,15], [10,13]]
arr = [2,3,6,8,10,15]
meeting_rooms(intervals, arr)
