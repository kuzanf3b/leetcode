class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        results = [0] * len(nums)
        results[0] = nums[0]

        for num in range(1, len(nums)):
            results[num] = nums[num] + results[num - 1]

        return results

    # time complexity: O(n)
    # space complexity: O(1)
