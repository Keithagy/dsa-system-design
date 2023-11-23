package q345

import "unicode"

func reverseVowels(s string) string {
	runes := []rune(s)
	beginning := 0
	end := len(runes) - 1
	vowels := map[rune]bool{'a': true, 'e': true, 'i': true, 'o': true, 'u': true}

	for beginning < end {
		for _, isVowel := vowels[unicode.ToLower(runes[beginning])]; !isVowel; {
			beginning++
		}
		for _, isVowel := vowels[unicode.ToLower(runes[end])]; !isVowel; {
			end--
		}
		runes[beginning], runes[end] = runes[end], runes[beginning]
		beginning++
		end--
	}
	return string(runes)
}
