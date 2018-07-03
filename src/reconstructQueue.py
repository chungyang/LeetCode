class Solution:
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        reconstructedQueue = []
        
        # key: h, value = [h,k]
        sorted_map = {}
        
        # Create a map for people that have the same h
        for person in people:
            
            if person[0] in sorted_map:
                sorted_map[person[0]].append(person)
            else:
                sorted_map[person[0]] = [person]
        
        for key in sorted_map:
            sorted_map[key] = sorted(sorted_map[key])
            
        for key in sorted(sorted_map,reverse = True):
            
            for person in sorted_map[key]:
                reconstructedQueue.insert(person[1],person[:])
                
        return reconstructedQueue