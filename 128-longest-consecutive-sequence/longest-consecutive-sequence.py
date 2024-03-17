class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        # Convert the input list into a set for O(1) lookup.
        num_set = set(nums)
        max_length = 0
        
        for num in num_set:
            # Check if the current number is the start of a sequence.
            if num - 1 not in num_set:
                current_num = num
                current_length = 1
                
                # Increment current_num and current_length until the consecutive sequence ends.
                while current_num + 1 in num_set:
                    current_num += 1
                    current_length += 1
                
                # Update the max_length if the current sequence length is greater.
                max_length = max(max_length, current_length)
        
        return max_length
