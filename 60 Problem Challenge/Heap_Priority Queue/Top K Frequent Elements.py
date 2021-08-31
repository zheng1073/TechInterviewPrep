"""
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.
"""
def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        results = []
        count = {}
        final = []
        for num in nums:
            if num in count:
                count[num] = count[num]+1
            else:
                count[num] = 1
        # key --> num, value --> count
        for key, value in count.items():
            
            hq.heappush(results, (value, key))
            if len(results) > k:
                hq.heappop(results)
        for x in results:
            final.append(x[1])
        return final
"""
Runtime: 194 ms, faster than 5.17% of Python3 online submissions for Top K Frequent Elements.
Memory Usage: 18.6 MB, less than 95.15% of Python3 online submissions for Top K Frequent Elements.
"""
