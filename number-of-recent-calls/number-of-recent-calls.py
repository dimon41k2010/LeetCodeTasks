class RecentCounter:

    def __init__(self):
        self.queue = []

    def ping(self, t: int) -> int:
        while len(self.queue) != 0 and (t - self.queue[0]) > 3000:
            self.queue.pop(0)

        self.queue.append(t)

        return len(self.queue)

# Time: O(N) // N = count(ping) -> 10 000
# Space: O(W) // W = window -> 3000 milsec
        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)