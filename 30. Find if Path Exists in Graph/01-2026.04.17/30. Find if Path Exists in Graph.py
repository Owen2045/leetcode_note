from typing import List
from collections import deque


class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        
        graph = {}

        for i in range(n):
            graph[i] = []

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
            
        
        # 已拜訪
        visited = set()
        visited.add(source)
        
        queue = deque()
        queue.append(source)

        print(graph)

        while queue:
            node = queue.popleft()
            print(node)
            if node == destination:
                return True
            
            for nib in graph[node]:
                if nib not in visited:
                    visited.add(nib)
                    queue.append(nib)

        
        
n = 3
edges = [[0,1],[1,2],[2,0]]
source = 0
destination = 2


a = Solution()
b = a.validPath(n, edges, source, destination)
print(b)

