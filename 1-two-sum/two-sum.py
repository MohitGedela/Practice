class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # retry sync
        for i in range(len(nums)):
            j = i+1
            for j in range(len(nums)):
                if (nums[i] + nums[j] == target and i != j):
                    return i, j

