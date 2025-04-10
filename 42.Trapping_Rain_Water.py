import numpy as np


class Solution:
    def trap(self, height: list[int]) -> int:
        height = np.array(height)
        max_b = np.max(height)
        total = 0
        idx = 0
        tmp = height[0]
        for i in range(len(height)):
            if height[i] == max_b and i > idx:
                idx = i
        for i in range(1, idx):
            if tmp > height[i]:
                total += tmp - height[i]
            else:
                tmp = height[i]
        tmp = height[-1]
        for i in range(len(height) - 2, idx, -1):
            if tmp > height[i]:
                total += tmp - height[i]
            else:
                tmp = height[i]
        return total
