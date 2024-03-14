class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        # Sum of the indices from 0 to n
        expected_sum = n * (n + 1) // 2
        # Sum of the elements in the list
        actual_sum = sum(nums)
        # The difference between the expected sum and the actual sum will be the missing number
        return expected_sum - actual_sum

