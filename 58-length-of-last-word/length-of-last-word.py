class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # Strip trailing white spaces
        s = s.rstrip()

        # Find the index of the last space character
        last_space_index = s.rfind(' ')

        # If there are no spaces, the entire string is a word
        if last_space_index == -1:
            return len(s)

        # Return the length of the last word
        return len(s) - last_space_index - 1
