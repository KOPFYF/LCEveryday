'''
If the order is a buy order, you look at the sell order with the smallest price in the backlog. If that sell order's price is smaller than or equal to the current buy order's price, they will match and be executed, and that sell order will be removed from the backlog. Else, the buy order is added to the backlog.

Vice versa, if the order is a sell order, you look at the buy order with the largest price in the backlog. If that buy order's price is larger than or equal to the current sell order's price, they will match and be executed, and that buy order will be removed from the backlog. Else, the sell order is added to the backlog.

0 if it is a batch of buy orders, or
1 if it is a batch of sell orders.
'''

class Solution:
    def getNumberOfBacklogOrders(self, orders: List[List[int]]) -> int:
        mod = 10**9 + 7
        hq_buy, hq_sell = [], [] # (price, amt), buy max_heap, sell min_heap
        for price, amt, orderType in orders:
            if orderType == 0: # buy order, check min sell <= price and fill
                flag1 = False
                while hq_sell:
                    min_p, amt1 = hq_sell[0]
                    # print(min_p, price, amt1, amt)
                    if min_p <= price:
                        min_p, amt1 = heapq.heappop(hq_sell)
                        if amt1 >= amt: 
                            heapq.heappush(hq_sell, (min_p, amt1 - amt))
                            flag1 = True
                            break
                        else:
                            amt = amt - amt1
                    else:
                        break
                if not flag1:
                    heapq.heappush(hq_buy, (-price, amt))
                
            else:
                flag2 = False
                while hq_buy:
                    max_p, amt2 = hq_buy[0]
                    if -max_p >= price:
                        neg_max_p, amt2 = heapq.heappop(hq_buy)
                        if amt2 >= amt: # match and be executed
                            heapq.heappush(hq_buy, (neg_max_p, amt2 - amt))
                            flag2 = True
                            break
                        else:
                            amt = amt - amt2
                    else:
                        break
                if not flag2:
                    heapq.heappush(hq_sell, (price, amt))
            # print(hq_sell, hq_buy)
        res = 0
        for p, amt in hq_sell:
            res += amt
        for p, amt in hq_buy:
            res += amt
                        
        return res % mod