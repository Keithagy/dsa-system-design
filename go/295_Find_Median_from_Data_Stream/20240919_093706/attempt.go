package q295

// For some sorted array of length n, median index can be found at
// n // 2 if odd, avg(n//2,( n//2 )+1) if even
// the tricky part is that add num gives you data out of order
// you need to maintain the ordering of nums as they come in
// That likely involves you inserting in the middle >> linked list
// however, you likely still need the ability to lookup quickly for findMedian
// which means you need to index the linked list nodes with a hashmap
// addNum would be log n, because you do binary search for insertion (but then do you need to update all the other elements..?)
//
// Do you actually need a BST?
// adding to a BST would be
type MedianFinder struct{}

func Constructor() MedianFinder {
}

func (this *MedianFinder) AddNum(num int) {
}

func (this *MedianFinder) FindMedian() float64 {
}

/**
 * Your MedianFinder object will be instantiated and called as such:
 * obj := Constructor();
 * obj.AddNum(num);
 * param_2 := obj.FindMedian();
 */

