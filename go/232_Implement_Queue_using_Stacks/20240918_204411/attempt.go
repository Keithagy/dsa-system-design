package q232

type MyQueue struct {
	front []int
	back  []int
}

func Constructor() MyQueue {
	return MyQueue{
		make([]int, 0),
		make([]int, 0),
	}
}

func (this *MyQueue) Push(x int) {
	this.back = append(this.back, x)
}

func (this *MyQueue) transfer() {
	for i, j := 0, len(this.back)-1; i < j; i, j = i+1, j-1 {
		this.back[i], this.back[j] = this.back[j], this.back[i]
	}
	this.front = append(this.front, this.back...)
	this.back = make([]int, 0)
}

func (this *MyQueue) Pop() int {
	if len(this.front) == 0 {
		this.transfer()
	}
	popped := this.front[len(this.front)-1]
	this.front = this.front[:len(this.front)-1]
	return popped
}

func (this *MyQueue) Peek() int {
	if len(this.front) == 0 {
		return this.back[0]
	}
	return this.front[len(this.front)-1]
}

func (this *MyQueue) Empty() bool {
	return len(this.back)+len(this.front) == 0
}

/**
 * Your MyQueue object will be instantiated and called as such:
 * obj := Constructor();
 * obj.Push(x);
 * param_2 := obj.Pop();
 * param_3 := obj.Peek();
 * param_4 := obj.Empty();
 */

