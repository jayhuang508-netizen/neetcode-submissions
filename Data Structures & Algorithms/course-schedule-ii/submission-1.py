class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indgree = [0] * numCourses
        visited = set()
        cycle = set()
        adj = [[]for i in range(numCourses)]
        # print(adj)
        for src, dst in prerequisites:
            # print(src)
            adj[dst].append(src)
            indgree[src] += 1
        
        q = deque()
        for i in range(len(indgree)):
            if indgree[i] == 0:
                q.append(i)
                visited.add(i)

        res = []
        while len(q) != 0:
            node = q.popleft()
            res.append(node)
            for nei in adj[node]:
                indgree[nei] -=1
                if indgree[nei] == 0 and nei not in visited:
                    q.append(nei)
                    visited.add(nei)

        if len(res) != numCourses:
            return []
        
        return res





        
        