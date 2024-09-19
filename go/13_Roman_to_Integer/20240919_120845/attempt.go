package q13

func romanToInt(s string) int {
	lookaheads := map[byte](map[byte]bool){
		'I': map[byte]bool{
			'V': true,
			'X': true,
		},

		'X': map[byte]bool{
			'L': true,
			'C': true,
		},

		'C': map[byte]bool{
			'D': true,
			'M': true,
		},
	}
	values := map[byte]int{
		'I': 1,
		'V': 5,
		'X': 10,
		'L': 50,
		'C': 100,
		'D': 500,
		'M': 1000,
	}
	result := 0
	i := 0
	for i < len(s) {
		var val int
		var offset int
		if next, inLookaheads := lookaheads[s[i]]; i < len(s)-1 && inLookaheads {
			if _, modified := next[s[i+1]]; modified {
				val = values[s[i+1]] - values[s[i]]
				offset = 2
			} else {
				val = values[s[i]]
				offset = 1
			}
		} else {
			val = values[s[i]]
			offset = 1
		}
		i += offset
		result += val
	}
	return result
}

