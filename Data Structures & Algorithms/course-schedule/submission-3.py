class Solution:    
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        nodes = {}

        for i in range(numCourses):
            nodes[i] = []
        
        for prereq in prerequisites:
            nodes[prereq[1]].append(prereq[0])
        
        for node in nodes:
            visits = []
            queue = [(node,visits)]
            while queue:
                i, visits = queue.pop()
                if i in visits:
                    return False               
                visits.append(i)
                for n in nodes[i]:
                    queue.append((n, visits))
                nodes[i] = []
        
        return True