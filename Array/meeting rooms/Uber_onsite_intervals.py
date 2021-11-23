'''
https://leetcode.com/discuss/interview-question/934777/Uber-Onsite

Given a list[ [s,e],[s1,e2],[s2,e2]]. Return the frequency of intervals

[[0,3],[1,4],[2,7]]

[0,1]->1
[1-2]->2
[2-3]->3
[3-4]->2
[4-7]->1


'''
from collections import defaultdict


def getFreq(intervals):
	events = defaultdict(int)
	for s, e in intervals:
		events[s] += 1
		events[e] -= 1

	print(events)

	keys = sorted(events.keys())

	prev_time = keys[0]
	cnt = events[keys[0]]
	for cur_time in keys[1:]:
		print("[{}-{}]->{}".format(prev_time, cur_time, cnt))
		cnt += events[cur_time]
		# print(key, events[key], cnt)
		prev_time = cur_time
	
	return cnt

intervals = [[0,3],[1,4],[2,7]]
getFreq(intervals)