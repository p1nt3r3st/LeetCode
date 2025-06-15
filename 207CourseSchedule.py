class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        adj = [[] * numCourses for _ in range(numCourses)]
        visited = [0] * numCourses
        best = True

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
            visited[s] = 2

        if best:
            for i in range(numCourses):
                if visited[i] == 0:
                    dfs(i)

        return best


solution = Solution()
numCourses = 4
prerequisites = [[0, 1], [3, 1], [1, 3], [3, 2]]
print(solution.canFinish(numCourses, prerequisites))
