package q151

import "strings"

func reverseWordsIdiomatic(s string) string {
	// Split the string into words using strings.Fields which automatically handles multiple spaces and trims the string.
	words := strings.Fields(s)

	// Reverse the slice of words.
	for i, j := 0, len(words)-1; i < j; i, j = i+1, j-1 {
		words[i], words[j] = words[j], words[i]
	}

	// Join the words back into a string with a space between each word.
	return strings.Join(words, " ")
}

func reverseWords(s string) string {
	runes := []rune(strings.TrimSpace(s))
	for i := 0; i < len(runes)/2; i++ {
		runes[i], runes[len(runes)-i-1] = runes[len(runes)-i-1], runes[i]
	}
	outputLen := len(runes)
	currStart := 0
	for currStart < outputLen {
		for currStart < outputLen && runes[currStart] == ' ' {
			currStart++
		}

		currEnd := currStart
		for currEnd < outputLen && runes[currEnd] != ' ' {
			currEnd++
		}

		for i := 0; i < (currEnd-currStart)/2; i++ {
			runes[currStart+i], runes[currEnd-i-1] = runes[currEnd-i-1], runes[currStart+i]
		}
		currStart = currEnd + 1
	}

	// Remove extra spaces between words.
	// This is done by using two pointers to read and write the runes.
	writeIndex := 0
	for readIndex := 0; readIndex < len(runes); {
		// Copy non-space runes directly.
		if runes[readIndex] != ' ' {
			runes[writeIndex] = runes[readIndex]
			writeIndex++
			readIndex++
		} else {
			// Skip all consecutive spaces.
			for readIndex < len(runes) && runes[readIndex] == ' ' {
				readIndex++
			}
			// Write a single space if we're not at the end of the runes slice.
			if readIndex < len(runes) {
				runes[writeIndex] = ' '
				writeIndex++
			}
		}
	}
	// Convert the slice of runes back to a string, up to the writeIndex.
	return string(runes[:writeIndex])
}
