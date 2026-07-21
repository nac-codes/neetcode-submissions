class Solution:
    

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for _ in range(numCourses)]
        for a, b in prerequisites:
            graph[b].append(a)
        
        state = [0] * numCourses

        def dfs(course: int) -> bool:            
            if state[course] == 1:
                return False
            if state[course] == 2:
                return True
            
            state[course] = 1
            for child in graph[course]: 
                if not dfs(child):
                    return False
            state[course] = 2
            return True

        
        for i in range(numCourses):
            if state[i] == 0 and not dfs(i):
                return False
        
        return True