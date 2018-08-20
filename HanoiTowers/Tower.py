from HanoiTowers import Disk


class Tower:

    def __init__(self):
        self.tower = []
        self.height = 0

    def adddisk(self, i):
        self.tower.insert(0, Disk.Disk(i))
        self.height += 1

    def removefirst(self):
        self.height -= 1
        return self.tower.pop(0)

    def __str__(self):
        height = self.height - 1
        a = ""

        for i in self.tower:
            a = a + height * " " + i.visualize() + "\n"
            height -= 1

        return a
