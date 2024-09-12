from typing import Optional


class LinkedList:
    class Node:
        def __init__(self, val: int) -> None:
           self.val = val
           self.next :Optional[LinkedList.Node] =  None
           self.prev :Optional[LinkedList.Node] =  None
    def __init__(self) -> None:
       self.head, self.tail = LinkedList.Node(0), LinkedList.Node(0) # dummy nodes
       self.tail.prev = self.head
       self.head.next = self.tail


class RandomizedSet:

   """
   Inner data structure likely has to be set
   the key requirement is to return a random element, with same probably of returning each
   all operations have to be O(1)

   to get random, you can randint an array index >> but if you remove from middle that's not O(1)
   linked list?

   you randint a hashmap key, and value is a linked list node
   inserting appends linked list tail and adds to key 

   remove deletes linked list node and removes from hash map
   """ 
    def __init__(self):
        self.s = set()

    def insert(self, val: int) -> bool:
        if val in self.s:
            return False
        self.s.add(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.s:
            return False
        self.s.remove(val)
        return True

    def getRandom(self) -> int:
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
