class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}
        for i, num in enumerate(nums):
            x = target - num
            if x in hash_map:
                return [hash_map[x], i]
            hash_map[num] = i