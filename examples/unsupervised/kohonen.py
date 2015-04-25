#!/usr/bin/env python
# #################################################
# Example for Kohonen Map
#
# Clusters random 2D coordinates in range [0,1]
# with a Kohonen Map of 5x5 neurons.
#
# Note: you need pylab to show the results
##################################################

__author__ = 'Thomas Rueckstiess, ruecksti@in.tum.de'

import pylab
from scipy import random

from pybrain.structure.modules import KohonenMap
from pybrain.tools.plotting.colormaps import show_map
from pybrain.tools.plotting import ColorMap

som = KohonenMap(2, 5, keys=['rand1', 'rand2'])

pylab.ion()
p = pylab.plot(som.neurons[:, :, 0].flatten(), som.neurons[:, :, 1].flatten(), 's')

for i in range(250):
    # one forward and one backward (training) pass
    som.activate(random.random(2))
    som.backward()

    # plot every 100th step
    if i % 100 == 0:
        p[0].set_data(som.neurons[:, :, 0].flatten(), som.neurons[:, :, 1].flatten())
        pylab.draw()

pylab.ioff()
show_map(som)
ColorMap(som.get_freqmatrix(), name='FreqMat').show()