from collections import Counter, deque
import heapq
import queue
from typing import List


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        current_time = 0
        counter = Counter(tasks)
        h = []
        ready_tasks: deque = deque()  # int: count, int: ready time
        for k, v in counter.items():
            heapq.heappush(h, -v)

        while h or ready_tasks:
            # 冷卻任務
            if len(ready_tasks) > 0 and ready_tasks[0][1] <= current_time:
                f, _ = ready_tasks.popleft()
                heapq.heappush(h, -f)
            if h:
                f = heapq.heappop(h)
                f = -f - 1
                if f > 0:
                    ready_tasks.append((f, current_time + n + 1))

            current_time += 1

        return current_time


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        current_time = 0
        counter = Counter(tasks)
        maxheap: list = []
        cooldown: deque = deque()  # int: count, int: ready time
        for k, v in counter.items():
            heapq.heappush(maxheap, -v)

        while maxheap or cooldown:
            # 先確認cooldown最左邊的任務可不可以再次執行了
            if cooldown and cooldown[0][1] <= current_time:
                f, _ = cooldown.popleft()  # -2
                # 重新加入
                heapq.heappush(maxheap, f)

            if maxheap:
                # 執行任務
                f = heapq.heappop(maxheap)  # -3
                f += 1
                if f < 0:  # 代表還有工作
                    next_time = current_time + n + 1
                    cooldown.append((f, next_time))  # -2

            current_time += 1

        return current_time


Solution().leastInterval(tasks=["A", "A", "A", "B", "B", "B"], n=2)
