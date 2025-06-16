class Solution:
    def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:
        adj = [[] * numCourses for _ in range(numCourses)]
        visited = [0] * numCourses
        best = True
        sort_graph = []

        for a_i, b_i in prerequisites:
            if a_i != b_i:
                adj[b_i].append(a_i)
            else:
                best = False

        def dfs(s):
            nonlocal best
            if visited[s] == 2:
                return
            if visited[s] == 1:
                best = False
                return
            visited[s] = 1
            for c in adj[s]:
                dfs(c)
            sort_graph.append(s)
            visited[s] = 2

        if best:
            for i in range(numCourses):
                if visited[i] == 0:
                    dfs(i)

        if best:
            return sort_graph[::-1]
        else:
            return []


solution = Solution()
numCourses = 4
prerequisites = [[1, 0], [0, 2], [3, 1], [2, 3]]
print(solution.findOrder(numCourses, prerequisites))
