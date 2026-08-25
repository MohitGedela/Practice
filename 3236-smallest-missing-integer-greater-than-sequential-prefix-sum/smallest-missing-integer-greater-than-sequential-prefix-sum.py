class Solution:
    def missingInteger(self, nums: List[int]) -> int:

        seq = nums[0]
        counter = 0
        
        for i in range(len(nums) - 1):
            if nums[i] + 1 == nums[i + 1]:
                seq += nums[i+1]
            else:
                break

        while True:
            counter = seq

            if counter not in nums:
                return counter
            else:
                seq += 1
