class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = [[] for _ in range(n)]

        for node1, node2 in edges:
            adj[node1].append(node2)
            adj[node2].append(node1)
        
        visited = set()
        res = 0
        def dfs(node, parent):
            if node in visited:
                return
            visited.add(node)
            for nei in adj[node]:
                if nei == parent:
                    continue
                # to go through every node it connects 
                dfs(nei, node)
        
        while len(visited) != n:
            for i in range(n):
                if i not in visited:
                    res += 1
                    dfs(i, -1)
                    continue
        return res

        