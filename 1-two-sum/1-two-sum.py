class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        elements= {}
        for idx, element in enumerate(nums):
            if target - element in elements:
                return [elements[target-element], idx]
            else:
                elements[element] = idx