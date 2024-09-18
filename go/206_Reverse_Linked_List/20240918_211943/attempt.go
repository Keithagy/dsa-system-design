package q206

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

func rev(node *ListNode) (*ListNode, *ListNode) {
	if node == nil || node.Next == nil {
		return node, node
	}
	revHead, revTail := rev(node.Next)
	node.Next = nil
	revTail.Next = node
	return revHead, node
}

func reverseList(head *ListNode) *ListNode {
	revHead, _ := rev(head)
	return revHead
}

