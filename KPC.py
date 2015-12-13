__author__ = "Marek Czaplicki"


class KnapsackEvolutionaryCrossover:
    def __init__(self, capacity, items, population=10, iterations=None, destination=None):
        self.capacity = capacity
        self.items = items
        self.destination = destination
        self.iterations = iterations
        self.population = population
        self.source = []
        self.no_change = 0

    def __calc_fitness__(self, src) -> int:
        value = 0
        for i in range(len(self.items)):
            if src[i] == 1:
                value += self.items[i][1]
        return value

    def __mutate_solo__(self, src) -> dict:
        import random
        weight = self.capacity + 1
        while weight > self.capacity:
            weight = 0
            allele = random.randint(0, len(self.items) - 1)
            src[allele] = int(not src[allele])
            for i in range(len(self.items)):
                if src[i] == 1:
                    weight += self.items[i][0]
        return {'dna': src, 'fitness': self.__calc_fitness__(src)}

    def __mutate__(self, parent_1, parent_2) -> dict:
        import random
        child_dna = parent_1['dna'][:]

        start = random.randint(0, len(self.items) - 1)
        stop = random.randint(0, len(self.items) - 1)
        if start > stop:
            stop, start = start, stop
        child_dna[start:stop] = parent_2['dna'][start:stop]

        allele = random.randint(0, len(self.items) - 1)
        child_dna[allele] = int(not child_dna[allele])
        weight = 0
        for i in range(len(self.items)):
            if child_dna[i] == 1:
                weight += self.items[i][0]
        if weight > self.capacity:
            return self.__mutate_solo__(child_dna)
        return {'dna': child_dna, 'fitness': self.__calc_fitness__(child_dna)}

# # <editor-fold desc="Adder/Setter/Remover">
    def add_item(self, item):
        if not isinstance(item, tuple):
            raise Exception("Please provide a tuple (weight, value).")
        self.items.append(item)

    def remove_item(self, item):
        if not isinstance(item, tuple):
            raise Exception("Please provide a tuple (weight, value).")
        if item in self.items:
            index = self.items.index(item)
            self.items.pop(index)

    def set_destination(self, dst):
        self.destination = dst

    def remove_destination(self):
        self.destination = None

    def set_iterations(self, iterations):
        self.iterations = iterations

    def remove_iterations(self):
        self.iterations = None
# # </editor-fold>

    def evolve(self):
        from random import random

        def random_chromosome() -> list:
            random_dna = [int(random() < 0.15) for _ in range(len(self.items))]
            weight = 0
            for j in range(len(self.items)):
                if random_dna[j]:
                    weight += self.items[j][0]
            while weight > self.capacity:
                weight = 0
                random_dna = [int(random() < 0.15) for _ in range(len(self.items))]
                for j in range(len(self.items)):
                    if random_dna[j]:
                        weight += self.items[j][0]
            return random_dna

        genetic_pool = []
        for i in range(self.population):
            dna = random_chromosome()
            fitness = self.__calc_fitness__(dna)
            candidate = {'dna': dna, 'fitness': fitness}
            genetic_pool.append(candidate)

        def random_parent(gen_pool):
            random_index = random() * random() * (self.population - 1)
            random_index = int(random_index)
            return gen_pool[random_index]

        f_out = open('KPC.log', 'w')
        n = 0
        self.no_change = 0
        while True if not self.iterations else n < self.iterations:
            n += 1
            genetic_pool.sort(key=lambda c: c['fitness'])
            genetic_pool = genetic_pool[::-1]

            f_out.writelines("\n".join(["%5i %5i %s" % (n, x['fitness'], ''.join(str(x['dna']))) for x in genetic_pool]))
            f_out.write("\n\n")

            parent_1 = random_parent(genetic_pool)
            parent_2 = random_parent(genetic_pool)

            child = self.__mutate__(parent_1, parent_2)
            if child['fitness'] > genetic_pool[-1]['fitness']:
                genetic_pool[-1] = child
            #     self.no_change = 0
            # else:
            #     self.no_change += 1
            if child['fitness'] > genetic_pool[0]['fitness']:
                self.no_change = 0
            else:
                self.no_change += 1
            yield (n, genetic_pool[0]['fitness'])
            # print("%5i | %5i" % (n, self.no_change))
            if (self.destination and genetic_pool[0]['fitness'] >= self.destination) or self.no_change >= 300:
                self.source = genetic_pool[0]['dna']
                break


if __name__ == '__main__':
    import random
    capacity = 15
    items = [(random.randint(1, 15), random.randint(1, 20)) for _ in range(20)]
    print(items)
    ke = KnapsackEvolutionaryCrossover(capacity, items, 3, iterations=1000)
    a = ke.evolve()
    for i in a:
        pass


