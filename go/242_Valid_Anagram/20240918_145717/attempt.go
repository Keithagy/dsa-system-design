package q242

func isAnagram(s string, t string) bool {
	t_count := make(map[rune]int)
	for _, r := range t {
		t_count[r]++
	}
	for _, r := range s {
		if _, exists := t_count[r]; !exists {
			return false
		} else {
			t_count[r]--
			if newCount := t_count[r]; newCount == 0 {
				delete(t_count, r)
			}
		}
	}
	return len(t_count) == 0
}

