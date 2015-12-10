from random import Random
from time import time
import inspyred


def main(prng=None, display=False):
    if prng is None:
        prng = Random()
        prng.seed(time())

    items = [(80, 1),
             (0, 0),
             (80, 10)]

    problem = inspyred.benchmarks.Knapsack(100, items, duplicates=False)
    ea = inspyred.ec.EvolutionaryComputation(prng)
    ea.selector = inspyred.ec.selectors.tournament_selection
    ea.variator = [inspyred.ec.variators.uniform_crossover,
                   inspyred.ec.variators.gaussian_mutation]
    ea.replacer = inspyred.ec.replacers.steady_state_replacement
    ea.terminator = inspyred.ec.terminators.evaluation_termination

    final_pop = ea.evolve(generator=problem.generator,
                          evaluator=problem.evaluator,
                          bounder=problem.bounder,
                          maximize=problem.maximize,
                          pop_size=100,
                          max_evaluations=2500,
                          tournament_size=5,
                          num_selected=2)

    if display:
        best = max(ea.population)
        print('Best Solution: {0}: {1}'.format(str(best.candidate),
                                               best.fitness))
    return ea

if __name__ == '__main__':
    main(display=True)
