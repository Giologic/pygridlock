# -*- coding: utf-8 -*-

"""
A Random Network Layout

This class implements a random network layout. In this layout, network stops are arranged randomly across an area.
"""

import abc
from .base import Layout

class Random(Layout):
    
    def __init__(self, max_nodes, max_walking_dist, boundaries, **kwargs):
        """ Initializes Lattice class """
        super(Random, self).__init__(max_nodes, max_walking_dist, boundaries)
        
        # TODO : Logger

    def generate_layout(self):
        """ Generate Network Layout """


    
    