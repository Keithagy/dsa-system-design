package q20

type char rune

func (c char) isOpen() bool {
	return c == '{' || c == '[' || c == '('
}

func (c char) isClosed() bool {
	return c == '}' || c == ']' || c == ')'
}

func (c char) matchesMostRecentOpen(stack *[]char) bool {
	if len(*stack) == 0 {
		return false
	}
	stackTop := (*stack)[len(*stack)-1]
	*stack = (*stack)[:len(*stack)-1]
	switch c {
	case '}':
		return stackTop == '{'
	case ']':
		return stackTop == '['
	case ')':
		return stackTop == '('
	}
	return false
}

func isValid(s string) bool {
	stack := []char{}
	for _, r := range s {
		c := char(r) // This conversion is necessary
		if c.isOpen() {
			stack = append(stack, c)
			continue
		}
		if c.isClosed() {
			if c.matchesMostRecentOpen(&stack) {
				continue
			} else {
				return false
			}
		}
	}
	return len(stack) == 0
}

