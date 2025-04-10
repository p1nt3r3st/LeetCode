class Solution:
    def minWindow(self, s: str, t: str) -> str:
        chars = list(t)
        words = 'a' * len(s)
        result = []
        for i in range(len(s)):
            if s[i] in t and s[i] in chars:
                result.append((s[i], i))
                chars.pop(chars.index(s[i]))
            elif s[i] in t and s[i] not in chars:
                result.append((s[i], i))
                j = 0
                for j in range(len(result)):
                    if result[j][0] == s[i]:
                        break
                result.pop(j)
            else:
                continue
            if len(chars) == 0:
                line = s[result[0][1]:result[-1][1]+1]
                if len(words) >= len(line):
                    words = line
        if len(chars) != 0:
            return ''
        else:
            return words
