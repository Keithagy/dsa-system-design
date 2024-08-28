from typing import List


class Solution:
    # because the travelling wraps around
    # travelling starting from the first half (accumulating nett costs)
    # is equivalent to starting from the second half and wrapping around
    # use tank to represent a particular section of the journey
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
      if sum(gas) < sum(cost):
        return -1 # no way any solution exists

      start = 0
      tank = 0
      for station in range(len(gas)):
        tank += gas[station] - cost[station]
        if tank < 0:
          tank = 0
          start = station + 1
      return start
