class LUPrefix:

    def __init__(self, n: int):
        self.lup = 0
        self.uploaded = [ False for _ in range(n+1)]

    def upload(self, video: int) -> None:
        self.uploaded[video] = True
        while self.lup+1 < len(self.uploaded) and self.uploaded[self.lup+1] == True:
            self.lup += 1

    def longest(self) -> int:
        return self.lup

# Your LUPrefix object will be instantiated and called as such:
# obj = LUPrefix(n)
# obj.upload(video)
# param_2 = obj.longest()