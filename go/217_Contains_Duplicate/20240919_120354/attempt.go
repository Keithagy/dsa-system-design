package q217

func containsDuplicate(nums []int) bool {
	seen := make(map[int]bool)
	for _, num := range nums {
		if seen[num] {
			return true
		} else {
			seen[num] = true
		}
	}
	return false
}

