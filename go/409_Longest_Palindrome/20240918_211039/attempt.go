package q409

func longestPalindrome(s string) int {
	counts := make(map[rune]int)
	for _, r := range s {
		counts[r]++
	}
	result := 0
	odds := []rune{}
	for r, count := range counts {
		result += count
		if count%2 != 0 {
			odds = append(odds, r)
		}
	}
	if len(odds) != 0 {
		result -= len(odds) - 1
	}
	return result
}

