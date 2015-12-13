__author__ = "Marek Czaplicki"


class KnapsackEvolutionary:
    def __init__(self, capacity, items, iterations=None, source=None, destination=None):
        self.capacity = capacity
        self.items = items
        self.destination = destination
        self.iterations = iterations
        self.no_change = 0
        if not source:
            self.source = [0] * len(items)
        else:
            self.source = source
        if len(self.source) != len(self.items):
            raise Exception("Length of source is not applicable to items provided.")
        self.fitness = self.__calc_fitness__(self.source)

    def __calc_fitness__(self, src) -> int:
        value = 0
        for i in range(len(self.items)):
            if src[i] == 1:
                value += self.items[i][1]
        return value

    def __mutate__(self, src) -> list:
        import random
        allele = random.randint(0, len(self.items) - 1)
        src[allele] = int(not src[allele])
        weight = 0
        for i in range(len(self.items)):
            if src[i] == 1:
                weight += self.items[i][0]
        if weight > self.capacity:
            return self.__mutate__(src)
        return src

# # <editor-fold desc="Adder/Setter/Remover">
    def add_item(self, item):
        if not isinstance(item, tuple):
            raise Exception("Please provide a tuple (weight, value).")
        self.items.append(item)
        self.source.append(0)

    def remove_item(self, item):
        if not isinstance(item, tuple):
            raise Exception("Please provide a tuple (weight, value).")
        if item in self.items:
            index = self.items.index(item)
            self.items.pop(index)
            self.source.pop(index)

    def set_destination(self, dst):
        self.destination = dst

    def remove_destination(self):
        self.destination = None

    def set_iterations(self, iterations):
        self.iterations = iterations

    def remove_iterations(self):
        self.iterations = None

    def set_source(self, source):
        if len(source) != len(self.items):
            raise Exception("Please provide right length of source.")
        self.source = source

    def remove_source(self):
        self.source = [0] * len(self.items)

# # </editor-fold>

    def evolve(self):
        n = 0
        self.no_change = 0
        while True if not self.iterations else n < self.iterations:
            n += 1
            mutated = self.__mutate__(self.source)
            mutated_fitness = self.__calc_fitness__(mutated)
            if mutated_fitness > self.fitness:
                self.fitness = mutated_fitness
                self.source = mutated
                self.no_change = 0
            else:
                self.no_change += 1
            yield (n, self.fitness)
            # print("%5i %5i %s" % (n, self.fitness, self.source))
            if (self.destination and self.fitness >= self.destination) or self.no_change >= 100:
                break


if __name__ == '__main__':
    ke = KnapsackEvolutionary(50, [(2, 10), (23, 14), (5, 20), (16, 2), (25, 16)], destination=48)
    for i in ke.evolve():
        print(i)


