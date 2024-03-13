class Solution:
    def hammingWeight(self, n: int) -> int:
        ans = 0

        # Counting the set bits using Brian Kernighan's Algorithm
        while n:
            n &= (n - 1)  # Toggle the least significant set bit
            ans += 1

        return ans