from typing import List


class Solution:
    # gas  [ 1, 2, 3,4,5]
    # cost [ 3, 4, 5,1,2]
    # nett [-2,-2,-2,3,3]

    # gas  [ 2, 3, 4]
    # cost [ 3, 4, 3]
    # nett [-1,-1, 1]
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
      nett = [gas[i] - cost[i] for i in range(len(gas))]
      tank = 0 # 1
      starting = -1 # 2
      for station in range(len(gas)):
        if nett[station] < 0:
          continue # You can't start here
        starting = station if tank == 0 else starting
        tank += nett[station]
        if tank < 0:
          tank = 0 # previous journey ended in futility, keep looking for next starting
      return starting if tank + sum(nett[:starting]+nett[starting+1:]) >= 0 else -1
