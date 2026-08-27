class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distanceMap = {} # recording distance: [points]
        for x,y in points:
            dis = math.sqrt(x*x + y*y)
            if dis in distanceMap:
                distanceMap[dis].append((x,y))
            else:
                distanceMap[dis] = [(x,y)]
        # print(distanceMap)
        dists = list(distanceMap.keys())
        heapq.heapify(dists) # default is the min heap
        count = k
        res = []
        while count != 0:
            # print(dists)
            dis = heapq.heappop(dists)
            points = distanceMap[dis]
            # print(points)
            for p in points:
                res.append(list(p))
                count -= 1
                # print(p, count)
                if count == 0:
                    return res
        return res
        

        