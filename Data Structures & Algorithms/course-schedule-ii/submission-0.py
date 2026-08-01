class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        course_to_deps = defaultdict(list)
        num_deps = [0] * numCourses
        for a, b in prerequisites:
            course_to_deps[b].append(a)
            num_deps[a] += 1
        # c_to_d = 0 -> 1
        # num_deps[]
        q = deque()
        for i in range(numCourses):
            if num_deps[i] == 0:
                q.append(i)
        
        visited = set()
        output = []
        while q and len(visited) < numCourses:
            node = q.popleft()
            if node in visited:
                continue
            output.append(node)
            visited.add(node)
            for dep in course_to_deps[node]:
                num_deps[dep] -= 1
                if num_deps[dep] == 0:
                    q.append(dep)
        
        return [] if len(visited) != numCourses else output