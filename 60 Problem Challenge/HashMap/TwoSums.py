"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.
"""
def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        dict = {}
        for index, value in enumerate(nums):
            if (target - value) in dict:
                return [dict[target-value], index]
            else:
                dict[value] = index
"""
Runtime: 52 ms, faster than 96.81% of Python3 online submissions for Two Sum.
Memory Usage: 15.2 MB, less than 55.05% of Python3 online submissions for Two Sum.
"""
