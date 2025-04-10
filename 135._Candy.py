import numpy as np


class Solution:
    def candy(self, ratings: list[int]) -> int:
        ratings = np.array(ratings)
        if len(ratings) >= 3:
            level_1 = np.full(fill_value=1, shape=ratings.shape)
            level_2 = np.full(fill_value=1, shape=ratings.shape)
            level_3 = np.full(fill_value=1, shape=ratings.shape)
            if ratings[0] > ratings[1]:
                level_1[0] += 1
            for i in range(1, len(ratings) - 1):
                if ratings[i] > ratings[i - 1]:
                    level_1[i] = level_1[i - 1] + 1
                elif ratings[i] > ratings[i + 1]:
                    level_1[i] += 1
                else:
                    continue
            if ratings[-1] > ratings[-2]:
                level_1[-1] = level_1[-2] + 1
            if ratings[-1] > ratings[-2]:
                level_2[-1] += 1
            for i in range(len(ratings) - 2, 0, -1):
                if ratings[i] > ratings[i + 1]:
                    level_2[i] = level_2[i + 1] + 1
                elif ratings[i] > ratings[i - 1]:
                    level_2[i] += 1
                else:
                    continue
            if ratings[0] > ratings[1]:
                level_2[0] = level_2[1] + 1
            for i in range(len(ratings)):
                level_3[i] = max(level_1[i], level_2[i])
            return np.sum(level_3)
        else:
            if len(ratings) == 1:
                return 1
            else:
                if ratings[0] == ratings[1]:
                    return 2
                else:
                    return 3
