package q295

import (
	"container/heap"
)

type MedianFinder struct {
	smallHeap Heap // this is a maxHeap, so peeking gives largest of small half
	largeHeap Heap // this is a minHeap, so peeking gives smallest of large half
}
type Heap struct {
	Values   []int
	LessFunc func(int, int) bool
}

func (h *Heap) Less(i, j int) bool { return h.LessFunc(h.Values[i], h.Values[j]) }
func (h *Heap) Swap(i, j int)      { h.Values[i], h.Values[j] = h.Values[j], h.Values[i] }
func (h *Heap) Len() int           { return len(h.Values) }
func (h *Heap) Peek() int          { return h.Values[0] }
func (h *Heap) Push(v any)         { h.Values = append(h.Values, v.(int)) }
func (h *Heap) Pop() (v any) {
	h.Values, v = h.Values[:len(h.Values)-1], h.Values[len(h.Values)-1]
	return v
}

func NewHeap(less func(int, int) bool) Heap {
	return Heap{make([]int, 0), less}
}

func Constructor() MedianFinder {
	return MedianFinder{
		NewHeap(func(i, j int) bool {
			return i > j
		}),
		NewHeap(func(i, j int) bool {
			return i < j
		}),
	}
}

func (this *MedianFinder) AddNum(num int) {
	heap.Push(&this.smallHeap, num)
	if this.smallHeap.Len() > 0 && this.largeHeap.Len() > 0 && this.smallHeap.Peek() > this.largeHeap.Peek() {
		heap.Push(&this.largeHeap, heap.Pop(&this.smallHeap))
	}
	if this.smallHeap.Len()-this.largeHeap.Len() > 1 {
		heap.Push(&this.largeHeap, heap.Pop(&this.smallHeap))
	}
	if this.largeHeap.Len()-this.smallHeap.Len() > 1 {
		heap.Push(&this.smallHeap, heap.Pop(&this.largeHeap))
	}
}

func (this *MedianFinder) FindMedian() float64 {
	if this.largeHeap.Len() == this.smallHeap.Len() {
		return (float64(this.largeHeap.Peek()) + float64(this.smallHeap.Peek())) / 2
	}
	if this.largeHeap.Len() > this.smallHeap.Len() {
		return float64(this.largeHeap.Peek())
	}
	return float64(this.smallHeap.Peek())
}

/**
 * Your MedianFinder object will be instantiated and called as such:
 * obj := Constructor();
 * obj.AddNum(num);
 * param_2 := obj.FindMedian();
 */

