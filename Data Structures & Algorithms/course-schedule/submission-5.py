class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        indegree = [0] * numCourses

        for a,b in prerequisites:
            graph[b].append(a)
            indegree[a] += 1
        
        queue = deque([i for i in range(numCourses) if indegree[i] == 0])
        count = 0

        while queue:
            course = queue.popleft()
            count += 1

            for child in graph[course]:
                indegree[child] -= 1
                if indegree[child] == 0:
                    queue.append(child)
            
        
        return count == numCourses

