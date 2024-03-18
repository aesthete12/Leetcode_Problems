from enum import Enum


class State(Enum):
    kInit = 0
    kVisiting = 1
    kVisited = 2


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for _ in range(numCourses)]
        states = [State.kInit] * numCourses

        for v, u in prerequisites:
            graph[u].append(v)

        def hasCycle(u: int) -> bool:
            if states[u] == State.kVisiting:
                return True
            if states[u] == State.kVisited:
                return False

            states[u] = State.kVisiting
            for v in graph[u]:
                if hasCycle(v):
                    return True
            states[u] = State.kVisited

            return False

        for i in range(numCourses):
            if hasCycle(i):
                return False

        return True
