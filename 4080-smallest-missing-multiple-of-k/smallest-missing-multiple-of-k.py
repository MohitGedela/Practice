class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:

        counter = 1

        while True:

            if (k * counter) in nums:
                counter += 1
            else:
                return k * counter
        