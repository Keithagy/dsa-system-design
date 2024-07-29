from typing import List


# This is not really a standard way to implement bubble sort. Correct according to ChatGPT though!
def bubble_sort(nums: List[int]) -> None:
    if len(nums) <= 1:
        return  # already sorted

    sorted_sub_start = len(nums)
    while (
        sorted_sub_start > 1
    ):  # idx 1 onwards being sorted implies 0 is in the right place
        i = 0
        j = 1
        while j < sorted_sub_start:
            if nums[i] > nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
            i = j
            j = i + 1
        sorted_sub_start -= 1


# A more standard appraoch
def bubble_sort_standard(nums: List[int]) -> None:
    for i in range(len(nums)):
        swapped = False
        for j in range(len(nums) - 1 - i):
            if nums[j] > nums[j + 1]:
                nums[j + 1], nums[j] = nums[j], nums[j + 1]
                swapped = True
            if not swapped:
                break
