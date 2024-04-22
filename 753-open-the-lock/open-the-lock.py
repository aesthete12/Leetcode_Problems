from collections import deque

class Solution:
    def openLock(self, deadends, target):
        deadends = set(deadends)
        if "0000" in deadends:
            return -1
        if target == "0000":
            return 0

        ans = 0
        q = deque(["0000"])
        seen = set(["0000"])

        while q:
            ans += 1
            for _ in range(len(q)):
                word = q.popleft()
                for i in range(4):
                    for d in (-1, 1):
                        next_digit = str((int(word[i]) + d) % 10)
                        new_word = word[:i] + next_digit + word[i+1:]
                        if new_word == target:
                            return ans
                        if new_word not in deadends and new_word not in seen:
                            q.append(new_word)
                            seen.add(new_word)

        return -1
