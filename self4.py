class Counter:
    def __init__(self):
        self.count = 0

    def up(self):
        self.count += 1
        print(self.count)

c = Counter()
c.up()
c.up()