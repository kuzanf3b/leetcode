class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        for num in range(1, len(nums)):
            nums[num] = nums[num - 1]

        return nums

    # time complexity: O(n)
    # space complexity: O(1)
