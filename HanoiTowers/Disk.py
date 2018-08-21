
class Disk:
    def __init__(self, width):
        self.width = width

    def getwidth(self):
        return self.width

    def visualize(self):
        return self.getwidth()*"■"
