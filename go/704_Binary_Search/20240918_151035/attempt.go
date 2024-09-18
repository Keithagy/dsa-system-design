package q704

func search(nums []int, target int) int {
	atLeastTarget := func(candidate int) bool {
		return candidate >= target
	}
	left, right := 0, len(nums)-1
	for left < right {
		mid := left + ((right - left) / 2)
		if atLeastTarget(nums[mid]) {
			right = mid
		} else {
			left = mid + 1
		}
	}
	if nums[left] == target {
		return left
	}
	return -1
}

