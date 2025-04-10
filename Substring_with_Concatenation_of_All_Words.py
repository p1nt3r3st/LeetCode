class Solution:
    def findSubstring(self, s: str, words: list[str]) -> list[int]:
        result = []
        word_length = len(words[0])
        s_length = len(s)
        concat_length = len(words) * word_length

        words_dict_start = {}
        for word in words:
            words_dict_start[word] = words_dict_start.get(word, 0) + 1

        for i in range(0, s_length - concat_length + 1):
            words_dict = words_dict_start.copy()
            line = s[i:i+concat_length]
            flag = True
            for j in range(0, len(line), word_length):
                new_line = line[j:j+word_length]
                value = words_dict.get(new_line, 0)
                if value == 0:
                    flag = False
                    break
                else:
                    words_dict[new_line] -= 1
            if flag:
                result.append(i)
        return result
