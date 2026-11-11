class Solution:
    def minimumCost(self, cost1, cost2, costBoth, need1, need2):
        ans = need1 * cost1 + need2 * cost2
        mn = min(need1, need2)
        mx = max(need1, need2)
        if costBoth < cost1 + cost2:
            ans = min(ans, mn * costBoth + (need1 - mn) * cost1 + (need2 - mn) * cost2)
            if need1 > need2:
                if costBoth < cost1:
                    ans = min(ans, mx * costBoth)
                else:
                    ans = min(ans, mn * costBoth + (need1 - mn) * cost1)
            else:
                if costBoth < cost2:
                    ans = min(ans, mx * costBoth)
                else:
                    ans = min(ans, mn * costBoth + (need2 - mn) * cost2)
        ans = min(ans, mx * costBoth)
        return ans









        