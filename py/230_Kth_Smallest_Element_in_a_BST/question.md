Given the `root` of a binary search tree, and an integer `k`, return
*the* `k`^`th`^ *smallest value (**1-indexed**) of all the values of the
nodes in the tree*.

 

**Example 1:**

![](https://assets.leetcode.com/uploads/2021/01/28/kthtree1.jpg){style="width: 212px; height: 301px;"}

    Input: root = [3,1,4,null,2], k = 1
    Output: 1

**Example 2:**

![](https://assets.leetcode.com/uploads/2021/01/28/kthtree2.jpg){style="width: 382px; height: 302px;"}

    Input: root = [5,3,6,2,4,null,null,1], k = 3
    Output: 3

 

**Constraints:**

-   The number of nodes in the tree is `n`.
-   `1 <= k <= n <= 10`^`4`^
-   `0 <= Node.val <= 10`^`4`^

 

**Follow up:** If the BST is modified often (i.e., we can do insert and
delete operations) and you need to find the kth smallest frequently, how
would you optimize?
