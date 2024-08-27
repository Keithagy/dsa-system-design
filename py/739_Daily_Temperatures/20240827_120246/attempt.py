from typing import List


class Solution:
    # [69,72,71,76,73]
    # [4,6,3,5]
    # [1,0,1,0]
    # [
    #   4: [6]
    #   6: [5]
    #   3: [5]
    #   5: []
    # ]
    # need orering so can't sort
    # last element always 0
    # next last element can check the element ahead. if it is higher, you have to wait 1 day
    # if next element is not higher, then you can't necessarily compute based on the previous value
    # because in this case 6 is higher than 5 while 3 isn't
    # maybe your dp value needs to track the distance to days
    # earlier days' set of subsequent days are always smaller than later days set of subsequent days
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        
