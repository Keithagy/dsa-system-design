Here's the markdown table representation of the information in the image:
source: [binary cheatsheet](https://www.techinterviewhandbook.org/algorithms/binary/)

| Technique                         | Code                                            |
| --------------------------------- | ----------------------------------------------- |
| Test k^th bit is set              | `num & (1 << k) != 0.`                          |
| Set k^th bit                      | `num \|= (1 << k)`                              |
| Turn off k^th bit                 | `num &= ~(1 << k).`                             |
| Toggle the k^th bit               | `num ^= (1 << k).`                              |
| Multiply by 2^k                   | `num << k`                                      |
| Divide by 2^k                     | `num >> k`                                      |
| Check if a number is a power of 2 | `(num & num - 1) == 0 or (num & (-num)) == num` |
| Swapping two variables            | `num1 ^= num2; num2 ^= num1; num1 ^= num2`      |

Note: In the markdown table, I've used `^` for exponentiation in the "Technique" column to represent superscript, as markdown doesn't directly support superscript. In the "Code" column, `^` represents the bitwise XOR operation as it does in the original image.
