from functools import lru_cache
from typing import List


def coin_change_with_logging(coins: List[int], amount: int) -> int:
    coins.sort(reverse=True)

    @lru_cache(maxsize=None)
    def dp(remaining: int, depth: int = 0) -> int:
        indent = "  " * depth
        print(f"{indent}Calculating dp({remaining})")

        if remaining == 0:
            print(f"{indent}Base case: remaining = 0, returning 0")
            return 0
        if remaining < 0:
            print(f"{indent}Invalid: remaining < 0, returning inf")
            return float("inf")

        min_coins = float("inf")
        for coin in coins:
            print(f"{indent}Trying coin {coin}")
            result = dp(remaining - coin, depth + 1)
            if result != float("inf"):
                min_coins = min(min_coins, result + 1)
                print(f"{indent}Updated min_coins to {min_coins}")

        print(f"{indent}Returning {min_coins} for dp({remaining})")
        return min_coins

    result = dp(amount)
    return result if result != float("inf") else -1


# Example usage
coins = [1, 5]
amount = 6
print(f"Coins: {coins}, Amount: {amount}")
result = coin_change_with_logging(coins, amount)
print(f"Minimum coins needed: {result}")

"""
Coins: [1, 5], Amount: 6
Calculating dp(6)
Trying coin 5
  Calculating dp(1)
  Trying coin 5
    Calculating dp(-4)
    Invalid: remaining < 0, returning inf
  Trying coin 1
    Calculating dp(0)
    Base case: remaining = 0, returning 0
  Updated min_coins to 1
  Returning 1 for dp(1)
Updated min_coins to 2
Trying coin 1
  Calculating dp(5)
  Trying coin 5
  Updated min_coins to 1
  Trying coin 1
    Calculating dp(4)
    Trying coin 5
      Calculating dp(-1)
      Invalid: remaining < 0, returning inf
    Trying coin 1
      Calculating dp(3)
      Trying coin 5
        Calculating dp(-2)
        Invalid: remaining < 0, returning inf
      Trying coin 1
        Calculating dp(2)
        Trying coin 5
          Calculating dp(-3)
          Invalid: remaining < 0, returning inf
        Trying coin 1
          Calculating dp(1)
          Trying coin 5
            Calculating dp(-4)
            Invalid: remaining < 0, returning inf
          Trying coin 1
            Calculating dp(0)
            Base case: remaining = 0, returning 0
          Updated min_coins to 1
          Returning 1 for dp(1)
        Updated min_coins to 2
        Returning 2 for dp(2)
      Updated min_coins to 3
      Returning 3 for dp(3)
    Updated min_coins to 4
    Returning 4 for dp(4)
  Updated min_coins to 1
  Returning 1 for dp(5)
Updated min_coins to 2
Returning 2 for dp(6)
Minimum coins needed: 2
"""
