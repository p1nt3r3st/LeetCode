class Solution:
    def calcEquation(self, equations: list[list[str]], values: list[float], queries: list[list[str]]) -> list[float]:

        def set_graph(start_key: str, key: str):
            if key in visited[start_key]:
                return
            else:
                visited[start_key].add(key)
                for div_sym in divs_for_one[key]:
                    if div_sym not in divs_for_one[start_key]:
                        divs_for_one[start_key].append(div_sym)
                        a_i, b_i, c_i = word2index[start_key], word2index[key], word2index[div_sym]
                        result = div_graph[a_i][b_i] * div_graph[b_i][c_i]
                        div_graph[a_i][c_i] = result
                        div_graph[c_i][a_i] = 1 / result
                    set_graph(start_key, div_sym)

        symbols = set()
        for syms in equations:
            for c in syms:
                symbols.add(c)
        symbols = sorted(symbols)

        n_len = len(symbols)
        div_graph = [[-1] * n_len for _ in range(n_len)]

        for i in range(n_len):
            div_graph[i][i] = 1

        i = 0
        word2index = {}
        divs_for_one = {}
        visited = {}
        for c in symbols:
            word2index[c] = i
            divs_for_one[c] = []
            visited[c] = set()
            i += 1

        for i in range(len(equations)):
            a, b = equations[i]
            a_i, b_i = word2index[a], word2index[b]
            result = values[i]

            div_graph[a_i][b_i] = result
            div_graph[b_i][a_i] = 1 / result

            divs_for_one[a].append(b)
            divs_for_one[b].append(a)

        for symbol in symbols:
            set_graph(symbol, symbol)

        result = []
        for a, b in queries:
            if a in word2index and b in word2index:
                a_i, b_i = word2index[a], word2index[b]
                result.append(div_graph[a_i][b_i])
            else:
                result.append(-1)
        return result


solution = Solution()
equations = [['a', 'b'], ['b', 'c']]
values = [2.0, 3.0]
queries = [["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]]
print(solution.calcEquation(equations, values, queries))


