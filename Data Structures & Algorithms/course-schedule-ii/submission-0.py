class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        indegree = [0] * numCourses

        for a,b in prerequisites:
            graph[b].append(a)
            indegree[a] += 1
        
        queue = deque([i for i in range(len(indegree)) if indegree[i] == 0])

        return_array = [] 
        while queue:
            parent = queue.popleft()
            return_array.append(parent)
            for child in graph[parent]:                
                indegree[child] -= 1
                if indegree[child] == 0:
                    queue.append(child)
        
        return return_array if len(return_array) == numCourses else []
                