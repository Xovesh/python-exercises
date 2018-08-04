import Tower


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
            abc = {"Tower 1": self.towers[0], "Tower 2": self.towers[1], "Tower 3": self.towers[2]}
            abc[tp].adddisk(abc[fp].removefirst().getwidth())
            print("moving disk from", fp, "to", tp)
            self.visualize()

        movetower(self.ndisk, "Tower 1", "Tower 3", "Tower 2")

    def visualize(self):
        print("Tower 1")
        print(self.towers[0])
        print("Tower 2")
        print(self.towers[1])
        print("Tower 3")
        print(self.towers[2])
        print("-------------------------")
