"""
Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.
"""
def firstUniqChar(self, s: str) -> int:
        dict = {}
        result = []
        for i, e in enumerate(s):
            if e not in dict:
                result.append(e)
                dict[e] = i
            else:
                if e in result:
                    result.remove(e)
        if len(result) == 0:
            return -1
        minVal = dict[result[0]]
        for val in result:
            minVal = min(minVal, dict[val]) 
        return minVal
"""
Runtime: 125 ms, faster than 60.76% of Python3 online submissions for First Unique Character in a String.
Memory Usage: 14.6 MB, less than 20.76% of Python3 online submissions for First Unique Character in a String.
"""
