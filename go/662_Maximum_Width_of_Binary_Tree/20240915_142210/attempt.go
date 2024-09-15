package q662

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

type qElement struct {
	node *TreeNode
	idx  int
}

func widthOfBinaryTree(root *TreeNode) int {
	q := []qElement{{root, 0}}
	maxWidth := 0
	for len(q) > 0 {
		nodesInLevel := len(q)
		first, last := q[0], q[nodesInLevel-1]
		maxWidth = max(maxWidth, last.idx-first.idx+1)

		for i := 0; i < nodesInLevel; i++ {
			currNode, currIdx := first.node, first.idx
			q = q[1:]
			if currNode.Left != nil {
				q = append(q, qElement{currNode.Left, currIdx*2 + 1})
			}
			if currNode.Right != nil {
				q = append(q, qElement{currNode.Right, currIdx*2 + 2})
			}
		}

	}
	return maxWidth
}

