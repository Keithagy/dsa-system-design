## Explanation: Flood Fill

### Analysis of problem & input data

This problem is a classic example of a flood fill algorithm, which is essentially a graph traversal problem on a 2D grid. The key characteristics of this problem are:

1. We're working with a 2D grid (the image) where each cell represents a pixel.
2. We need to traverse the grid starting from a given point (sr, sc) and change the color of connected pixels.
3. The connectivity is defined as 4-directional (up, down, left, right).
4. We only change the color of pixels that have the same original color as the starting pixel.

The problem maps well to either a depth-first search (DFS) or breadth-first search (BFS) approach. DFS is often preferred for its simplicity in implementation, especially in recursive form.

The key principle that makes this question simple is that we can treat the 2D grid as a graph, where each pixel is a node, and adjacent pixels of the same color are connected nodes. By performing a graph traversal (DFS or BFS) from the starting pixel, we can efficiently find and color all connected pixels.

### Test cases

1. Normal case: As given in Example 1
2. No change needed: As given in Example 2
3. Single pixel image: `[[1]]`, sr = 0, sc = 0, color = 2
4. Large image with all same color: `[[1,1,1,1],[1,1,1,1],[1,1,1,1]]`, sr = 1, sc = 1, color = 2
5. Image with multiple disconnected areas: `[[1,1,2],[1,1,2],[2,2,1]]`, sr = 0, sc = 0, color = 3

Here's the Go code to set up these test cases:

```go
func runTestCases() {
    testCases := []struct {
        image [][]int
        sr, sc, color int
    }{
        {[][]int{{1,1,1},{1,1,0},{1,0,1}}, 1, 1, 2},
        {[][]int{{0,0,0},{0,0,0}}, 0, 0, 0},
        {[][]int{{1}}, 0, 0, 2},
        {[][]int{{1,1,1,1},{1,1,1,1},{1,1,1,1}}, 1, 1, 2},
        {[][]int{{1,1,2},{1,1,2},{2,2,1}}, 0, 0, 3},
    }

    for i, tc := range testCases {
        fmt.Printf("Test Case %d:\n", i+1)
        fmt.Printf("Input: %v, sr=%d, sc=%d, color=%d\n", tc.image, tc.sr, tc.sc, tc.color)
        result := floodFill(tc.image, tc.sr, tc.sc, tc.color)
        fmt.Printf("Output: %v\n\n", result)
    }
}
```

### Solutions

#### Overview of solution approaches

##### Solutions worth learning

1. Depth-First Search (DFS) - Recursive (Neetcode solution)
2. Depth-First Search (DFS) - Iterative
3. Breadth-First Search (BFS)

Count: 3 solutions (1 Neetcode solution)

##### Rejected solutions

1. Brute Force: Checking every pixel in the image is inefficient and doesn't leverage the connected nature of the problem.
2. Union-Find: While theoretically possible, it's overcomplicated for this problem and less efficient than DFS or BFS.

#### Worthy Solutions

##### Depth-First Search (DFS) - Recursive

```go
func floodFill(image [][]int, sr int, sc int, color int) [][]int {
    // If the starting color is already the target color, no change is needed
    if image[sr][sc] == color {
        return image
    }

    // Store the original color
    originalColor := image[sr][sc]

    // Define a nested DFS function
    var dfs func(r, c int)
    dfs = func(r, c int) {
        // Check if we're out of bounds or if the current pixel is not the original color
        if r < 0 || r >= len(image) || c < 0 || c >= len(image[0]) || image[r][c] != originalColor {
            return
        }

        // Color the current pixel
        image[r][c] = color

        // Recursively call DFS on all 4 directions
        dfs(r-1, c) // Up
        dfs(r+1, c) // Down
        dfs(r, c-1) // Left
        dfs(r, c+1) // Right
    }

    // Start the DFS from the given starting point
    dfs(sr, sc)

    return image
}
```

Time Complexity: O(N), where N is the number of pixels in the image. In the worst case, we might need to visit every pixel in the image.

Space Complexity: O(N) in the worst case for the call stack. This happens when the image is filled with pixels of the same color, and the graph becomes a long snake-like structure, causing the recursion to go as deep as the number of pixels.

- The algorithm uses depth-first search to traverse all connected pixels of the same color.
- It first checks if any change is needed (when starting color is already the target color).
- The DFS function recursively explores in all four directions, coloring pixels as it goes.
- The base case for recursion is when we go out of bounds or encounter a pixel of a different color.
- This approach is elegant and intuitive, directly mapping the problem description to code.

##### Depth-First Search (DFS) - Iterative

```go
func floodFill(image [][]int, sr int, sc int, color int) [][]int {
    if image[sr][sc] == color {
        return image
    }

    originalColor := image[sr][sc]
    stack := [][]int{{sr, sc}}
    directions := [][]int{{-1, 0}, {1, 0}, {0, -1}, {0, 1}} // Up, Down, Left, Right

    for len(stack) > 0 {
        pixel := stack[len(stack)-1]
        stack = stack[:len(stack)-1]
        r, c := pixel[0], pixel[1]

        if r < 0 || r >= len(image) || c < 0 || c >= len(image[0]) || image[r][c] != originalColor {
            continue
        }

        image[r][c] = color

        for _, dir := range directions {
            stack = append(stack, []int{r + dir[0], c + dir[1]})
        }
    }

    return image
}
```

Time Complexity: O(N), where N is the number of pixels in the image. We visit each pixel at most once.

Space Complexity: O(N) in the worst case, where we might need to store all pixels in the stack.

- This solution uses an explicit stack to mimic the recursive calls of the DFS approach.
- It's essentially the same algorithm as the recursive version, but with manual stack management.
- The iterative approach can be beneficial in languages with strict stack size limits or for very large images where deep recursion might cause stack overflow.
- The code is slightly more verbose but avoids the potential issues with deep recursion.

##### Breadth-First Search (BFS)

```go
func floodFill(image [][]int, sr int, sc int, color int) [][]int {
    if image[sr][sc] == color {
        return image
    }

    originalColor := image[sr][sc]
    queue := [][]int{{sr, sc}}
    directions := [][]int{{-1, 0}, {1, 0}, {0, -1}, {0, 1}} // Up, Down, Left, Right

    for len(queue) > 0 {
        pixel := queue[0]
        queue = queue[1:]
        r, c := pixel[0], pixel[1]

        if r < 0 || r >= len(image) || c < 0 || c >= len(image[0]) || image[r][c] != originalColor {
            continue
        }

        image[r][c] = color

        for _, dir := range directions {
            queue = append(queue, []int{r + dir[0], c + dir[1]})
        }
    }

    return image
}
```

Time Complexity: O(N), where N is the number of pixels in the image. We visit each pixel at most once.

Space Complexity: O(N) in the worst case, where we might need to store all pixels in the queue.

- This solution uses a queue to perform a breadth-first search of the connected pixels.
- BFS explores pixels in "layers", starting from the given pixel and expanding outwards.
- The main difference from DFS is the order in which pixels are processed: BFS processes all immediate neighbors before moving to the next level.
- In practice, for this problem, BFS and DFS will produce the same result and have similar performance characteristics.

#### Rejected Approaches

1. Brute Force: Checking every pixel in the image (O(m\*n) time complexity) and then determining if it's connected to the starting pixel is inefficient. It doesn't leverage the connected nature of the problem and would require additional complexity to determine connectivity.

2. Union-Find: While Union-Find is a powerful algorithm for connected components problems, it's overcomplicated for this specific task. The flood fill naturally lends itself to a traversal approach (DFS or BFS), and using Union-Find would introduce unnecessary complexity without any significant benefits.

#### Final Recommendations

The recursive DFS approach (Neetcode solution) is recommended as the best solution to learn for this problem. Here's why:

1. Simplicity: It's the most straightforward to understand and implement, directly mapping the problem description to code.
2. Efficiency: It solves the problem in optimal time and space complexity.
3. Elegance: The recursive nature of DFS matches well with the recursive nature of the flood fill problem.
4. Interview Performance: In an interview setting, this solution can be quickly coded and easily explained.

However, it's worth understanding the iterative DFS and BFS approaches as well, as they demonstrate important concepts (stack/queue usage, graph traversal) and can be preferable in certain situations (e.g., languages with strict stack limits).

### Visualization(s)

For this problem, a visual representation of the flood fill process can be helpful. Here's a simple ASCII representation of the flood fill process for the first example:

```
Initial state:     After flood fill:
1 1 1              2 2 2
1 1 0      ->      2 2 0
1 0 1              2 0 1

Start at (1,1), original color = 1, new color = 2

Step 1: Color (1,1)
2 1 1
1 2 0
1 0 1

Step 2: Spread to (0,1), (1,0), (2,1)
2 2 1
2 2 0
2 0 1

Step 3: Spread to (0,0), (0,2)
2 2 2
2 2 0
2 0 1
```

This visualization helps to understand how the flood fill algorithm spreads from the starting point, changing the color of connected pixels with the same original color.
