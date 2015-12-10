import random
import string

__author__ = "Marek Czaplicki"


def calc_fitness(src, dst):
    in_fit_value = 0
    for n in range(0, len(src)):
        in_fit_value += (ord(dst[n]) - ord(src[n])) ** 2
    return in_fit_value


def mutate(parent1, parent2):
    child_dna = parent1['dna'][:]

    # Mix both DNAs
    start = random.randint(0, len(parent2['dna']) - 1)
    stop = random.randint(0, len(parent2['dna']) - 1)
    if start > stop:
        stop, start = start, stop
    child_dna[start:stop] = parent2['dna'][start:stop]

    # Mutate one position
    charpos = random.randint(0, len(child_dna) - 1)
    child_dna[charpos] = chr(ord(child_dna[charpos]) + random.randint(-1,1))
    child_fitness = calc_fitness(child_dna, target)
    return {'dna': child_dna, 'fitness': child_fitness}


if __name__ == '__main__':
    target = "Hello World!"

    population = 20
    genetic_pool = []
    for i in range(0, population):
        dna = [random.choice(string.printable[:-5]) for j in range(0, len(target))]
        fitness = calc_fitness(dna, target)
        candidate = {'dna': dna, 'fitness': fitness}
        genetic_pool.append(candidate)

    def random_parent(arg_genetic_pool):
        random_number = random.random() * random.random() * (population - 1)
        random_number = int(random_number)
        return arg_genetic_pool[random_number]

    f_out = open('KP.log', 'w')
    i = 0
    while True:
        i += 1
        genetic_pool.sort(key=lambda candidate: candidate['fitness'])
        f_out.writelines("\n".join(["%5i %5i %s" % (i, x['fitness'], ''.join(x['dna'])) for x in genetic_pool]))
        f_out.write("\n\n")
        if genetic_pool[0]['fitness'] == 0:
            # Target reached
            break

        parent1 = random_parent(genetic_pool)
        parent2 = random_parent(genetic_pool)

        child = mutate(parent1, parent2)
        if child['fitness'] < genetic_pool[-1]['fitness']:
            genetic_pool[-1] = child
