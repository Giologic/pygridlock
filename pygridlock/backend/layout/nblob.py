# -*- coding: utf-8 -*-

"""
A NBlob Network Layout

This class implements a NBlob network layout. In this layout, network stops are arranged in Blobs/Hubs.
"""

import abc
from .base import Layout

class NBlob(Layout):
    
    def __init__(self, max_nodes, max_walking_dist, blob_coords):
        """ Initializes Lattice class """
        super(NBlob, self).__init__(max_nodes, max_walking_dist, blob_coords)
        
        # TODO : Logger

    def generate_layout(self):
        """ Generate Network Layout """


    
    