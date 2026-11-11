class Solution:
    def minimumCost(self, cost1: int, cost2: int, costBoth: int, need1: int, need2: int) -> int:
        cost_for_simultaneous_unit = min(costBoth, cost1 + cost2)

        common_need_units = min(need1, need2)
        
        total_cost = common_need_units * cost_for_simultaneous_unit
        
        remaining_need1 = need1 - common_need_units
        remaining_need2 = need2 - common_need_units
        
        if remaining_need1 > 0:
            total_cost += remaining_need1 * min(cost1, costBoth)
            
        if remaining_need2 > 0:
            total_cost += remaining_need2 * min(cost2, costBoth)
            
        return total_cost