# Input : Input: nums1 = [1,2,2,1], nums2 = [2,2]
# Output: [2]
def intersection(nums1, nums2):
    results = []
    if len(nums1) < len(nums2):
        for val in nums1:
            if val in nums2 and val not in results:
                results.append(val)
    else:
        for val in nums2:
            if val in nums1 and val not in results:
                results.append(val)
    return results
    
nums1=[4,9,5]
nums2=[9,4,9,8,4]

print(intersection(nums1,nums2))
