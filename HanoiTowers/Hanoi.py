from HanoiTowers import Tower


class Hanoi:

    def __init__(self, ndisk):
        self.towers = (Tower.Tower(), Tower.Tower(), Tower.Tower())
        self.ndisk = ndisk
        self.start()

    def start(self):
        # adding disks
        for i in range(3 + 2 * (self.ndisk - 1), 2, -2):
            self.towers[0].adddisk(i)
        self.visualize()

        self.algorithm()

    def algorithm(self):
        def movetower(height, fromPole, toPole, withPole):
            if height >= 1:
                movetower(height - 1, fromPole, withPole, toPole)
                movedisk(fromPole, toPole)
                movetower(height - 1, withPole, toPole, fromPole)

        def movedisk(fp, tp):
            tp.adddisk(fp.removefirst().getwidth())
            self.visualize()

        movetower(self.ndisk, self.towers[0], self.towers[2], self.towers[1])

    def visualize(self):
        print("Tower 1")
        print(self.towers[0])
        print("Tower 2")
        print(self.towers[1])
        print("Tower 3")
        print(self.towers[2])
        print("-------------------------")
