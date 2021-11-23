
"""
Given an array with repeated elements, the task is to find the maximum distance between two occurrences of an element.
"""
# Input : arr[] = {3, 2, 1, 2, 1, 4, 5, 8, 6, 7, 4, 2}
# Output: 10
# first occurance, current distance, max distance
def maxDistance(arr):
    myDict = {}
    for i in range(0, len(arr)):
        if arr[i] in myDict:
            newDistance = i - myDict[arr[i]][0]
            myDict[arr[i]][1] = newDistance
            myDict[arr[i]][2] = max(myDict[arr[i]][2], newDistance) 
        else:
            myDict[arr[i]] = [i, 0, 0]
    maxValue = 0
    for i in range(0, len(myDict)):
        maxValue = max(maxValue, myDict[arr[i]][2])
    return maxValue


arr = [3, 2, 1, 2, 1, 4, 5, 8, 6, 7, 4, 2]
 
print(maxDistance(arr))
