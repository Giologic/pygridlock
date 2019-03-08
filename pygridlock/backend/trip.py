# -*- coding: utf-8 -*-

"""
    Trip Class Backend

    This module implements a Trip class containing attributes such as from_stop_id, to_stop_id, options, etc.
"""

import attr
from attr.validators import instance_of


@attr.s
class Trip(object):
    """ GTFS Trip Class

        This class follows the implementation of a gtfs trips.txt file. This class will only 
        require you to supply the following parameters: route_id, service_id, trip_id.

        Required Attributes
        ----------
        route_id : int
            ID that uniquely identifies a route.
        trip_id : int
            contains an ID that identifies a trip.


        Optional Attributes
        ----------
        service_id : int
            contains an ID that uniquely identifies a set of dates when service is available for one or more routes. 
        trip_headsign : str
            contains the text that appears on a sign that identifies the trip's destination to passengers.
        trip_short_name : str
            contains the text that appears in schedules and sign boards to identify the trip to passengers,
            for example, to identify train numbers for commuter rail trips.
        direction_id : int
            contains a binary value that indicates the direction of travel for a trip.
            Use this field to distinguish between bi-directional trips with the same route_id.
        block_id : int
            identifies the block to which the trip belongs.
        shape_id : int
            contains an ID that defines a shape for the trip.
        wheelchair_accessible : int
            contains a value that indicates wheelchair accesibility statuses
        bikes_allowed : int
            contains a value that indicates whether bikes are allowed or not
        

        For further reference, you may check the GTFS documentation in https://developers.google.com/transit/gtfs/reference/#tripstxt
    """


    #required attributes
    route_id = attr.ib(type=int, validator=instance_of(int))
    trip_id = attr.ib(type=int, validator=instance_of(int))
    

    #optional attributes with default
    service_id = attr.ib(type=int, validator=instance_of(int), default=0)
    trip_headsign = attr.ib(type=str, validator=instance_of(str), default="")
    trip_short_name = attr.ib(type=str, validator=instance_of(str), default="")
    direction_id = attr.ib(type=int, validator=instance_of(int), default=0)
    shape_id = attr.ib(type=int, validator=instance_of(int), default=0)
    wheelchair_accessible = attr.ib(type=int, validator=instance_of(int), default=0)
    bikes_allowed = attr.ib(type=int, validator=instance_of(int), default=0)

        
    #extra parameters
    options = attr.ib(type=dict, validator=instance_of(dict), default={})

    @classmethod
    def as_dict(cls):
        return attr.asdict(cls)



    