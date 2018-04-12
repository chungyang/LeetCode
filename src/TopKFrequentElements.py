from heapq import heappush, heappop

class TopKFrequentElements:
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        
        num_dict = {}
        h = []
        answer = []
        for i in nums:
            if i in num_dict:
                num_dict[i] = num_dict.get(i) + 1
            else:
                num_dict[i] = 1

        for key,value in num_dict.items():
            heappush(h,(-value,key))
        
        for i in range(k):
            answer.append(heappop(h)[1])
        
        return answer