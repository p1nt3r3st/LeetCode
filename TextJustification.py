class Solution:

    def left_justify(self, words: list[str], maxWidth: int) -> str:
        line = ' '.join(words)
        line += (maxWidth - len(line)) * ' '
        return line

    def middle_justify(self, words: list[str], maxWidth: int) -> str:
        sum_len = 0
        for i in range(len(words)):
            sum_len += len(words[i])
        n = maxWidth - sum_len
        count_space = n // (len(words) - 1)
        rest_space = n % (len(words) - 1)
        result = ''
        for i in range(len(words) - 1):
            result = result + words[i] + ' ' * count_space
            if rest_space > 0:
                result += ' '
                rest_space -= 1
            else:
                continue
        result += words[-1]
        return result

    def fullJustify(self, words: list[str], maxWidth: int) -> list[str]:
        i = 1
        len_line = len(words[0])
        result = []
        line = [words[0]]
        while i < len(words):
            len_line = len_line + len(words[i]) + 1
            if len_line <= maxWidth:
                line.append(words[i])
            else:
                result.append(line)
                len_line = len(words[i])
                line = [words[i]]
            i += 1
        result.append(line)
        final = []
        for i in range(len(result) - 1):
            if len(result[i]) == 1:
                final.append(self.left_justify(result[i], maxWidth))
            else:
                final.append(self.middle_justify(result[i], maxWidth))
        final.append(self.left_justify(result[-1], maxWidth))
        return final
