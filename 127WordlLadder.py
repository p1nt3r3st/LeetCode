class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: list[str]) -> int:

        def diff2words(a, b):
            counter = 0
            for i in range(len(a)):
                if a[i] != b[i]:
                    counter += 1
            return counter

        queue = [beginWord]
        distance = {}
        for key in wordList:
            distance[key] = -1
        distance[beginWord] = 0

        while len(queue) != 0:
            x = queue.pop(0)
            for c in wordList:
                if distance[x] != -1 and distance[c] == -1 and diff2words(x, c) == 1:
                    distance[c] = distance[x] + 1
                    queue.append(c)

        return distance.get(endWord, -1) + 1


solution = Solution()
begin = 'a'
end = 'c'
words = ['a', 'b', 'c']
print(solution.ladderLength(begin, end, words))
