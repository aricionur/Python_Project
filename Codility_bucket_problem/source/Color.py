class Color:

    def __init__(self, id):
        self.id = id
        self.counter = 1

    def __eq__(self, other):
        if isinstance(other, int):
            return self.id == other
        elif isinstance(other, Color):
            return self.id == other.id and self.counter == other.counter

    def increase_counter(self):
        self.counter += 1