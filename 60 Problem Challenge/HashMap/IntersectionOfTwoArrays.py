"""
Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must be unique and you may return the result in any order.
"""
def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dict = {}
        for val in nums1:
            if val not in dict:
                dict[val] = "Hit"
        result = []
        for val2 in nums2:
            if val2 in dict and val2 not in result:
                    result.append(val2)
        return result
"""
Runtime: 44 ms, faster than 80.44% of Python3 online submissions for Intersection of Two Arrays.
Memory Usage: 14.5 MB, less than 13.75% of Python3 online submissions for Intersection of Two Arrays.
"""
