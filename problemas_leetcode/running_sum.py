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

# https://leetcode.com/study-plan/leetcode-75/?progress=xz3itpu1
# https://leetcode.com/problems/running-sum-of-1d-array/?envType=study-plan&id=level-1
