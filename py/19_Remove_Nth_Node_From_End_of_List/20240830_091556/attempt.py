# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    # Fast pointer to get node count at tail
    # Slow pointer to find nth node from tail
    # disconnect node from list
    # O(n) from 2 list traversals
    # constant time removal
    # input: [1,3], n=1
    # input: [1,2,3], n=2
    # input: [1,2], n=2
    # input: [1], n=1
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
      if not head:
        return head
      cur = head # 3
      node_count = 1 # 3
      while cur and cur.next:
        cur = cur.next 
        node_count+=1
      traversals = node_count-n # 1
      prev = None # 1
      cur = head # 2
      for _ in range(traversals): #[0]
        prev = cur
        cur = cur.next
      if not prev:
        return cur.next # [2]
      prev.next = cur.next 
      return head #[1]
