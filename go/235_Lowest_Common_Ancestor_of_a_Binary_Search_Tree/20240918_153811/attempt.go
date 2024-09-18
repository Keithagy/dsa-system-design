package q235

/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val   int
 *     Left  *TreeNode
 *     Right *TreeNode
 * }
 */
type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func lowestCommonAncestor(root, p, q *TreeNode) *TreeNode {
	inBetween := func() bool {
		return (root.Val >= p.Val && root.Val <= q.Val) || (root.Val <= p.Val && root.Val >= q.Val)
	}
	if (root == p || root == q) || inBetween() {
		return root
	}
	if root.Val > p.Val && root.Val > q.Val {
		return lowestCommonAncestor(root.Left, p, q)
	}
	return lowestCommonAncestor(root.Right, p, q)
}

