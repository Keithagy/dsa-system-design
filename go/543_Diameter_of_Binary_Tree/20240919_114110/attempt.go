package q543

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

func inner(node *TreeNode) (int, int, int) {
	if node == nil {
		return -1, -1, -1
	}
	if node.Left == nil && node.Right == nil {
		return 0, 0, 0
	}
	left_left, left_sub_longest, left_right := inner(node.Left)
	right_left, right_sub_longest, right_right := inner(node.Right)
	node_sub_longest := max(left_sub_longest, right_sub_longest, max(left_left, left_right)+max(right_left, right_right)+2)
	return max(left_left, left_right) + 1, node_sub_longest, max(right_left, right_right) + 1
}

func diameterOfBinaryTree(root *TreeNode) int {
	_, diam, _ := inner(root)
	return diam
}

