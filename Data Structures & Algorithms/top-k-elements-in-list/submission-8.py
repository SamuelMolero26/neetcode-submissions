from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        counts = Counter(nums)

        #convert to list

        freq = list(counts.items())

        #sort in descending
        freq.sort(key= lambda x: x[1], reverse=True)
    
        res = []

        for i in range(k):
            res.append(freq[i][0])

        return res