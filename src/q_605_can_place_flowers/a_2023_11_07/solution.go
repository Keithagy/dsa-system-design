package q605

func canPlaceFlowers(flowerbed []int, n int) bool {
	decrementN := func() {
		n--
	}
	visitingBeginning := func(idx int) bool {
		return idx == 0
	}
	visitingEnd := func(flowerbed []int, idx int) bool {
		return idx == len(flowerbed)-1
	}
	plantIfThisAndRightEmpty := func(flowerbed []int, idx int) {
		if flowerbed[idx] == 0 && flowerbed[idx+1] == 0 {
			flowerbed[idx] = 1
			decrementN()
		}
	}
	plantIfThisAndLeftEmpty := func(flowerbed []int, idx int) {
		if flowerbed[idx] == 0 && flowerbed[idx-1] == 0 {
			flowerbed[idx] = 1
			decrementN()
		}
	}
	plantIfThisAndRightLeftEmpty := func(flowerbed []int, idx int) {
		if flowerbed[idx] == 0 && flowerbed[idx-1] == 0 && flowerbed[idx+1] == 0 {
			flowerbed[idx] = 1
			decrementN()
		}
	}
	if n == 0 {
		return true
	}
	if len(flowerbed) == 0 {
		return false
	}
	if len(flowerbed) == 1 {
		return flowerbed[0] == 0 && n == 1
	}
	for i := range flowerbed {
		if n <= 0 {
			return true
		}
		if visitingBeginning(i) {
			plantIfThisAndRightEmpty(flowerbed, i)
			continue
		}
		if visitingEnd(flowerbed, i) {
			plantIfThisAndLeftEmpty(flowerbed, i)
			continue
		}

		// in-between cases
		plantIfThisAndRightLeftEmpty(flowerbed, i)
	}
	return n <= 0
}
