package q67

func addBinary(a string, b string) string {
	result := []rune{}
	carry := uint8(0)
	i, j := len(a)-1, len(b)-1
	for i >= 0 || j >= 0 {
		var aBit, bBit uint8
		if i >= 0 && a[i] == '1' {
			aBit = 1
		}
		if i >= 0 {
			i--
		}
		if j >= 0 && b[j] == '1' {
			bBit = 1
		}
		if j >= 0 {
			j--
		}
		sum := carry + aBit + bBit
		bit := sum % 2
		if bit == 0 {
			result = append(result, '0')
		} else {
			result = append(result, '1')
		}
		carry = sum / 2
	}
	if carry != 0 {
		result = append(result, '1')
	}

	for i, j := 0, len(result)-1; i < j; i, j = i+1, j-1 {
		result[i], result[j] = result[j], result[i]
	}
	return string(result)
}

