from collections import deque

class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        maxNum = max(nums)
        ans = 0
        count = 0

        l = 0
        max_count = 0
        max_count_queue = deque()

        for r, num in enumerate(nums):
            if num == maxNum:
                count += 1
                max_count += 1
                max_count_queue.append(r)
            while count == k:
                if nums[l] == maxNum:
                    count -= 1
                l += 1
            while max_count > k - 1:
                max_count_start = max_count_queue.popleft()
                max_count = r - max_count_start
            ans += l

        return ans
