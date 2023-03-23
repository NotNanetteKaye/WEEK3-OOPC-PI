nums = [1, 2, 3, 4]
# output = [1,3,6,10]

def running_sum(nums):
    output = []
    sum_value = 0
    for i in range(1, len(nums) + 1):
        sum_value += nums[i - 1]
        output.append(sum_value)
        print(output)


start = running_sum(nums)
