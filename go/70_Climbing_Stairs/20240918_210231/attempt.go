package q70

func climbStairs(n int) int {
	i := 0
	prev, cur := 0, 1
	for i < n {
		tmp := prev + cur
		prev = cur
		cur = tmp
		i++
	}
	return cur
}

