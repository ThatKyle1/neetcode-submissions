class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # using a min heap k closest
        # some how mark points as there distance
        # key is distance, value is point( a list of points cause can be same)
        if k == 0:
            return [[]]

        hashmap = defaultdict(list) # its going to start with empty list because multiple points can be added
        minHeap = []
        # getting every point and calculating distance mapping key as distance and point add to distance list
        for point in points:
            x1, y1 = point[0],point[1]
            distance = math.sqrt(abs(((x1 - 0)** 2) + ((y1 - 0)** 2)))
            hashmap[distance].append(point)
        
        for dist, pointLst in hashmap.items():
            heapq.heappush(minHeap ,(dist, pointLst)) # pointLst is a 2D array
        
        res = []

        while len(res) < k:
            dist , points = heapq.heappop(minHeap) # getting value poping smallest
            for i in points:
                res.append(i)
                if len(res) == k:
                    return res
        
