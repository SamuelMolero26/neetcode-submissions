class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        check = []

        for i in range(0, len(nums)):
            if nums[i] in check:
                return True

            check.append(nums[i])


        return False
        