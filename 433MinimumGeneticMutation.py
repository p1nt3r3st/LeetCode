class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: list[str]) -> int:
        if endGene not in bank:
            return -1
        else:

            queue = [startGene]
            queue.extend(bank)
            distance = {}
            for gene in queue:
                distance[gene] = -1
            distance[startGene] = 0

            def bfs():
                nonlocal distance, queue

                while len(queue) != 0:
                    x = queue.pop(0)
                    queue = sorted(queue, key=lambda y: sum(1 for a, b in zip(x, y) if a != b))
                    for gene in queue:
                        if distance[gene] == -1 and sum(1 for a, b in zip(x, gene) if a != b) == 1:
                            distance[gene] = distance[x] + 1

            bfs()
            return distance[endGene]


solution = Solution()
startGene = "AAAACCCC"
endGene = "CCCCCCCC"
bank = ["AAAACCCA", "AAACCCCA", "AACCCCCA", "AACCCCCC", "ACCCCCCC", "CCCCCCCC", "AAACCCCC", "AACCCCCC"]
print(solution.minMutation(startGene, endGene, bank))
