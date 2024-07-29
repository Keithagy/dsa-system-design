package q1431

func kidsWithCandies(candies []int, extraCandies int) []bool {
	// len(candies) >= 2
	mostCandies := candies[0]
	for _, count := range candies {
		if mostCandies < count {
			mostCandies = count
		}
	}
	result := make([]bool, 0, len(candies))
	for _, count := range candies {
		if count+extraCandies >= mostCandies {
			result = append(result, true)
		} else {
			result = append(result, false)
		}
	}
	return result
}
