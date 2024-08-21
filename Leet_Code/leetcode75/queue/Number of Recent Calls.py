from collections import deque


class RecentCounter:

    def __init__(self):

        self.requests = deque()

    def ping(self, t: int) -> int:

        self.requests.append(t)
        t0 = t - 3000

        while self.requests[0] < t0:
            self.requests.popleft()
        return len(self.requests)


s = RecentCounter()
s.ping(0)
