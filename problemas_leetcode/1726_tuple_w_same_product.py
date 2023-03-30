# 1. calculate # of pairs for a product
# 2. for each pair, 8 * (n * n - 1)/2

nums = [2, 3, 4, 6]

counts = {}
for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
        prod = nums[i] * nums[j]
        if prod in counts:
            counts[prod] = counts[prod] + 1
        else:
            counts[prod] = 1

    ans = 0
    for x, y in counts.items():
        if y > 1:
            ans = ans + ((y * (y-1))//2)*8


# leetcode explanation video: https://www.youtube.com/watch?v=xID4T_GUFeQ
# tuple explanation: https://www.youtube.com/watch?v=NI26dqhs2Rk
# actual leetcode problem: https://leetcode.com/problems/tuple-with-same-product/