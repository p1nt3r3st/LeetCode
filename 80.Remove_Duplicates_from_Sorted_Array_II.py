class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        tmp = nums[0]
        count = 1
        x_max = max(nums) + 1
        error = 0
        for i in range(1, len(nums)):
            if nums[i] != tmp:
                tmp = nums[i]
                count = 1
            else:
                if count == 2:
                    nums[i] = x_max
                    error += 1
                else:
                    count += 1
        nums.sort()
        return len(nums) - error
