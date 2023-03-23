nums = [1, 2, 3, 4]
# output = [1,3,6,10]

def running_sum(nums):
    output = [] # create a new list
    sum_value = 0 # define new integer in variable
    for i in nums: # go through list of integers 
        sum_value = i + sum_value
        output.append(sum_value)
        print(output)


start = running_sum(nums)

# https://leetcode.com/study-plan/leetcode-75/?progress=xz3itpu1
# https://leetcode.com/problems/running-sum-of-1d-array/?envType=study-plan&id=level-1
