class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        for num in range(1, len(nums)):
            nums[num] = nums[num - 1]

        return nums

    # time complexity: 0(n) because we iterate through the entire array once
    # space complexity: 0(1) because we are not using any extra space
