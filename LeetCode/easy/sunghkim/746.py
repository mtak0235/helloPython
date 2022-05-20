class Solution(object):
    def minCostClimbingStairs(self, cost):
        A = len(cost)
        if A <= 2:
            return min(cost)
        for i in range(2, A):
            cost[i] += min(cost[i - 1], cost[i - 2])
        return min(cost[-1], cost[-2])
        
