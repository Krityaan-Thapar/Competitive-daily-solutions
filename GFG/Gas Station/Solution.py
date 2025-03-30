class Solution:
    def startStation(self, gas, cost):
        s = sum(gas)
        c = sum(cost)
        n = len(gas)
        
        if c > s:
            return -1
        
        # Kadane's
        curr_fuel = 0
        best = 0
        for i in range(n):
            if curr_fuel < 0:
                curr_fuel = 0
                best = i
            curr_fuel += gas[i] - cost[i]
        return best