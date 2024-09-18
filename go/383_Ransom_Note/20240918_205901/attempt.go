package q383

func canConstruct(ransomNote string, magazine string) bool {
	letters := make(map[rune]int)
	for _, r := range magazine {
		letters[r] += 1
	}
	for _, r := range ransomNote {
		letters[r] -= 1
		if letters[r] < 0 {
			return false
		}
	}
	return true
}

