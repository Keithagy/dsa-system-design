package solutions

import (
	"strings"
)

func gcdOfStrings(str1 string, str2 string) string {
	var str1First, str2First strings.Builder

	str1First.WriteString(str1)
	str1First.WriteString(str2)

	str2First.WriteString(str2)
	str2First.WriteString(str1)

	if str1First.String() != str2First.String() {
		return ""
	}

	runes1 := []rune(str1)
	runes2 := []rune(str2)
	gcdStrLen := GCD(len(runes1), len(runes2))
	return string(runes1[:gcdStrLen])
}

func GCD(a, b int) int {
	for b != 0 {
		t := b
		b = a % b
		a = t
	}
	return a
}
