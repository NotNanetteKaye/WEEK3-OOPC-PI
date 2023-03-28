# Given an array of integers nums, calculate the pivot index of this array.

# The pivot index is the index where the sum of all the numbers strictly to the 
# left of the index is equal to the sum of all the numbers strictly to the index's right.

# If the index is on the left edge of the array, 
# then the left sum is 0 because there are no elements to the left. 
# This also applies to the right edge of the array.

# Return the leftmost pivot index. If no such index exists, return -1.

nums = [1, 7, 3, 6, 5, 6]

def find_pivot_index(nums):
    total = sum(nums)
    left_sum = 0
    pivot_index = 0
    for i in range(len(nums)):
        right_sum = total - nums[i] - left_sum
        if left_sum == right_sum:
            pivot_index += i
            print(f'{pivot_index} is the pivot index!')
            return i
        left_sum += nums[i]
    print('-1 is the pivot index')
    return -1


start = find_pivot_index(nums)
