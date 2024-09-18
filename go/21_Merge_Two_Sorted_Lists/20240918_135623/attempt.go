package q21

/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */

type ListNode struct {
	Val  int
	Next *ListNode
}

func mergeTwoLists(list1 *ListNode, list2 *ListNode) *ListNode {
	if list1 == nil && list2 == nil {
		return nil
	}
	if list1 == nil {
		return list2
	}
	if list2 == nil {
		return list1
	}

	head := &ListNode{
		0, nil, // dummy
	}
	tail := head
	for list1 != nil && list2 != nil {
		var next *ListNode
		if list1.Val < list2.Val {
			next = list1
			list1 = list1.Next
		} else {
			next = list2
			list2 = list2.Next
		}
		tail.Next = next
		tail = tail.Next
	}
	if list1 != nil {
		tail.Next = list1
	} else {
		tail.Next = list2
	}
	return head.Next
}

