package solutions

import "strings"

// mergeAlternatelyAsciiOnly works only because the problem states that words consist only of lowercase English letters.
func mergeAlternatelyAsciiOnly(word1 string, word2 string) string {
	var result strings.Builder
	i := 0

	for i < len(word1) && i < len(word2) {
		result.WriteByte(word1[i])
		result.WriteByte(word2[i])
	}

	if len(word1) == len(word2) {
		return result.String()
	}

	var longerWord *string
	if len(word1) > len(word2) {
		longerWord = &word1
	} else {
		longerWord = &word2
	}

	result.WriteString((*longerWord)[i:])
	return result.String()
}

// mergeAlternatelyUtfSafe has a higher memory + runtime overhead on account of needing to maintain an internal copy of the words expressed as runes, but is correct in the general case
func mergeAlternatelyUtfSafe(word1 string, word2 string) string {
	word1Runes := []rune(word1)
	word2Runes := []rune(word2)
	mergedRunes := make([]rune, 0, len(word1Runes)+len(word2Runes))
	i := 0

	for i < len(word1Runes) && i < len(word2Runes) {
		mergedRunes = append(mergedRunes, word1Runes[i], word2Runes[i])
		i++
	}

	if len(word1Runes) == len(word2Runes) {
		return string(mergedRunes)
	}

	var longerWord *[]rune
	if len(word1Runes) > len(word2Runes) {
		longerWord = &word1Runes
	} else {
		longerWord = &word2Runes
	}

	mergedRunes = append(mergedRunes, (*longerWord)[i:]...)
	return string(mergedRunes)
}
