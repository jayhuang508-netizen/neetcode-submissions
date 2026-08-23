class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj = [[] for _ in range(n)]
        for node1, node2 in edges:
            adj[node1].append(node2)
            adj[node2].append(node1)
        visited = set()

        def dfs(node, parent):
            if node in visited:
                return False
            visited.add(node)
            for n in adj[node]:
                if n == parent:
                    continue
                if not dfs(n, node):
                    return False
            return True
        
        return dfs(0,-1) and len(visited) == n
        