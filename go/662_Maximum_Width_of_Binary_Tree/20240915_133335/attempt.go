package q662

import (
	"container/list"
	"math"
)

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

type QElement struct {
	node *TreeNode
	idx  uint64
}

func intMin(a uint64, b uint64) uint64 {
	if a < b {
		return a
	}
	return b
}

func intMax(a uint64, b uint64) uint64 {
	if a > b {
		return a
	}
	return b
}

func leftChild(idx uint64) uint64 {
	return 2*idx + 1
}

func rightChild(idx uint64) uint64 {
	return 2*idx + 2
}

// for each level, you are looking for width as the max index - min index
func widthOfBinaryTree(root *TreeNode) int {
	q := list.New()
	q.PushBack(QElement{root, 0})

	maxWidth := uint64(0)
	for q.Len() > 0 {
		nodesInLevel := q.Len()
		var minIdx, maxIdx uint64 = math.MaxUint64, 0
		for i := 0; i < nodesInLevel; i++ {
			head := q.Front()
			q.Remove(head)

			qe := head.Value.(QElement)
			node := qe.node
			idx := qe.idx
			minIdx, maxIdx = intMin(minIdx, idx), intMax(maxIdx, idx)

			if (*node).Left != nil {
				q.PushBack(QElement{node.Left, leftChild(idx)})
			}
			if (*node).Right != nil {
				q.PushBack(QElement{node.Right, rightChild(idx)})
			}
		}
		width := maxIdx - minIdx + 1
		maxWidth = intMax(maxWidth, width)
	}
	return int(maxWidth)
}

