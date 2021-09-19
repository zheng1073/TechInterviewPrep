"""
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
"""
def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if strs == [""]:
            return [[""]]
        dict = {}
        for word in strs:
            x = list(word)
            y = "".join(sorted(x))
            if y in dict:
                dict[y].append(word)
            else:
                dict[y] = [word]
        result = []
        for key in dict:
            result.append(dict[key])
        return result
"""
Runtime: 100 ms, faster than 68.60% of Python3 online submissions for Group Anagrams.
Memory Usage: 17 MB, less than 98.38% of Python3 online submissions for Group Anagrams.
"""
