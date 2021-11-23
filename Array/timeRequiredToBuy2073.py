class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        # O(n)
        res = 0
        for i, ticket in enumerate(tickets):
			if i <= k:
                # before k, take min for each person
				res += min(ticket, tickets[k])
			else:
				if ticket < tickets[k]:
                    # run out before tickets[k], take all
					res += ticket
				else:
                    # run out after tickets[k], take tickets[k] - 1
					res += tickets[k] - 1
		return res
        
        
        # O(sum(tickets))
        res = 0
        while True:
            # print(tickets)
            for i in range(len(tickets)):
                if tickets[i] == 0:
                    continue
                tickets[i] -= 1
                res += 1
                if tickets[k] == 0:
                    return res