package q1

func twoSum(nums []int, target int) []int {
	seeking := make(map[int]int)
	n := len(nums)
	for i := 0; i < n; i++ {
		num := nums[i]
		if compIdx, exists := seeking[num]; exists {
			return []int{compIdx, i}
		}
		comp := target - num
		seeking[comp] = i
	}
	return []int{}
}

