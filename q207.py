class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        res = []
        if numCourses <= 0: return res

        inDegrees = {i: 0 for i in range(numCourses)}
        adjList = {i: [] for i in range(numCourses)}

        for u, v in prerequisites:
            inDegrees[v] += 1
            adjList[u].append(v)
        
        queue = deque()
        for v in adjList:
            if inDegrees[v] == 0: queue.append(v)
        
        while queue:
            v = queue.popleft()
            res.append(v)
            for child in adjList[v]:
                inDegrees[child] -= 1
                if inDegrees[child] == 0: queue.append(child)
        
        return len(res) == numCourses
