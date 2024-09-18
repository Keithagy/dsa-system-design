package q141

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

func hasCycle(head *ListNode) bool {
	if head == nil || head.Next == nil {
		return false
	}
	slow, fast := head.Next, head.Next.Next
	for fast != nil && fast.Next != nil && fast != slow {
		slow = slow.Next
		fast = fast.Next.Next
	}
	if fast == nil || fast.Next == nil {
		return false
	}
	return true
}

