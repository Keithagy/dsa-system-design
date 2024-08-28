from typing import List


class Solution:
    # brute force method is to test every index >> n^2
    # but, 4>>5 always remains the same. you just need to know if you can make that journey with that amount
    # if you can depart 4 with n gas, then you can depart 3 with n + cost[3]
    # net cost of departing station i = cost[i] - gas[(i+1)%len(gas)]
    # you can't sum up the net cost like that because you might not have enough liquidity

    # gas = [1], cost=[1]
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
      # [0]
      net_costs = [cost[i]-gas[(i+1)%len(gas)]for i in range(len(gas))]
      for (station,starting) in enumerate(gas):
        if starting < cost[station]:
          continue
        total_net_costs = 0
        j = station
        while ((j+1)%len(gas)) != station:
          total_net_costs += net_costs[j]
          j = (j+1)%len(gas)
        total_net_costs += cost[j]
        if starting >= total_net_costs:
          return station
      return -1
