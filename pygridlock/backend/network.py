# -*- coding: utf-8 -*-

"""
    Network Class Backend

    This module implements a Network class containing attributes such as stops, routes, trips and transfers.
"""

import attr
from attr.validators import instance_of


@attr.s
class Network(object):
    """ GTFS Class

        This class is a compiled representation of a transportation network information using stops, routes, trips
        and transfers which could be used for forming NetworkX Graphs.

        Initialize this class by adding stops, routes, trips and/or transfers.

        Attributes
        ----------
        stops : dict
            dictionary of stops in the transportation network
        routes : dict
            dictionary of routes in the transportation network
        stops : dict
            dictionary of routes in the transportation network
        

        For further reference, you may check the GTFS documentation in 
        https://developers.google.com/transit/gtfs/reference/#transferstxt
    """

    # attributes with default
    stops = attr.ib(type=dict, validator=instance_of(dict))
    routes = attr.ib(type=dict, validator=instance_of(dict), default={})
    trips = attr.ib(type=dict, validator=instance_of(dict), default={})
    transfers = attr.ib(type=dict, validator=instance_of(dict), default={})
        
    #extra parameters
    options = attr.ib(type=dict, validator=instance_of(dict), default={})





    