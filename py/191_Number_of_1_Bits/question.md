Write a function that takes the binary representation of a positive
integer and returns the number of [set bits]{keyword="set-bit"} it has
(also known as the [Hamming
weight](http://en.wikipedia.org/wiki/Hamming_weight){target="_blank"}).

 

**Example 1:**

::: example-block
**Input:** [n = 11]{.example-io}

**Output:** [3]{.example-io}

**Explanation:**

The input binary string **1011** has a total of three set bits.
:::

**Example 2:**

::: example-block
**Input:** [n = 128]{.example-io}

**Output:** [1]{.example-io}

**Explanation:**

The input binary string **10000000** has a total of one set bit.
:::

**Example 3:**

::: example-block
**Input:** [n = 2147483645]{.example-io}

**Output:** [30]{.example-io}

**Explanation:**

The input binary string **1111111111111111111111111111101** has a total
of thirty set bits.
:::

 

**Constraints:**

-   `1 <= n <= 2`^`31`^` - 1`

 

**Follow up:** If this function is called many times, how would you
optimize it?
