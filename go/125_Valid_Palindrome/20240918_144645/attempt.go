package q125

import "unicode"

func isAlphaNumeric(r rune) bool {
	return unicode.IsLetter(r) || unicode.IsNumber(r)
}

func toLower(r rune) rune {
	return unicode.ToLower(r)
}

func isPalindrome(s string) bool {
	runes := []rune(s)
	left, right := 0, len(runes)-1
	for left < right {
		for left < right && !isAlphaNumeric(runes[left]) {
			left++
		}
		for left < right && !isAlphaNumeric(runes[right]) {
			right--
		}
		if toLower(runes[left]) != toLower(runes[right]) {
			return false
		}
		left++
		right--
	}
	return true
}

