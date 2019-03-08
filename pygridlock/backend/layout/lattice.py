# -*- coding: utf-8 -*-

"""
A Lattice Network Layout

This class implements a lattice network layout. In this layout, network stops are arranged in grid form.
"""

import abc
from .base import Layout

class Lattice(Layout):
    
    def __init__(self, max_nodes, max_walking_dist, start_coords):
        """ Initializes Lattice class """
        super(Lattice, self).__init__(max_nodes, max_walking_dist, start_coords)
        
        # TODO : Logger

    def generate_layout(self):
        """ Generate Network Layout """


    
    