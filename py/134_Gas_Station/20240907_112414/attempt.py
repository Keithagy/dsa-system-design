from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(cost) - sum(gas) > 0:
            return (
                -1
            )  # no solutions exist, since you need to consider all the costs and all the benefits
        tank = 0
        start_station = 0
        for station in range(len(gas)):
            tank = tank + gas[station] - cost[station]
            if tank < 0:
                tank = 0
                start_station = station + 1
        return start_station

