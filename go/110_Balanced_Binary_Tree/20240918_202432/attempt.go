package q110

import "math"

/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func inner(node *TreeNode) (int, bool) {
	if node == nil {
		return 0, true
	}
	leftHeight, leftBal := inner(node.Left)
	rightHeight, rightBal := inner(node.Right)
	isBal := leftBal && rightBal && int(math.Abs(float64(leftHeight-rightHeight))) <= 1
	return 1 + max(leftHeight, rightHeight), isBal
}

func isBalanced(root *TreeNode) bool {
	_, bal := inner(root)
	return bal
}

