class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}

        for index, value in enumerate(nums):
            val = target - value        
            if val  in hash_map:
                return [hash_map[val], index]
            hash_map[value] = index

        return 
            



        