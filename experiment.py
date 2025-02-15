"""Tournament play experiment."""
from __future__ import absolute_import
import netbuilder
import gp
import pickle
# Use cuda
CUDA = True

if __name__=='__main__':
    # setup a tournament!
    nb_evolution_steps = 20
    tournament = \
        gp.TournamentOptimizer(
            population_sz=50,
            init_fn=netbuilder.randomize_network,
            mutate_fn=netbuilder.mutate_net,
            nb_workers=5,
            use_cuda=True)

    for i in range(nb_evolution_steps):
        print('\nEvolution step:{}'.format(i))
        print('================')
        tournament.step()
        # keep track of the experiment results & corresponding architectures
        name = "tourney_{}".format(i)
        pickle.dump(tournament.stats, open(name + '.stats','wb'))
        pickle.dump(tournament.history, open(name +'.pop','wb'))
