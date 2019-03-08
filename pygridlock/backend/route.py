# -*- coding: utf-8 -*-

"""
    Route Class Backend

    This module implements a Route class containing attributes such as route_id, route_type, options, etc.
"""

import attr
from attr.validators import instance_of


@attr.s
class Route(object):
    """ GTFS Route Class

        This class follows the implementation of a gtfs routes.txt file. This class will only 
        require you to supply the following parameters: route_id, route_type.

        Required Attributes
        ----------
        route_id : int
            ID that uniquely identifies a route.
        route_type : int (Required but default is Route.BUS)
            defines an agency for the specified route. Types are defined by using constants:
            (e.g Route.LIGHT_RAIL)
            LIGHT_RAIL = 0
            SUBWAY = 1
            RAIL = 2
            BUS = 3
            FERRY = 4
            CABLE_TRAM = 5
            AERIAL_LIFT = 6
            FUNICULAR = 7 


        Optional Attributes
        ----------
        agency_id : int
            defines an agency for the specified route.
        code : str
            short text or a number that uniquely identifies the stop for passengers.
        route_short_name : str
            contains the short name of a route.
        route_long_name : str
            contains the full name of a route.
        route_desc : str
            contains a description of a route.
        route_url : str
            contains the URL of a web page about that particular route.
        route_color : str
            defines a color that corresponds to a route.
        route_text_color : str
            used to specify a legible color to use for text drawn against a background of route_color.
        route_sort_order : int
            used to order the routes in a way which is ideal for presentation to customers. 
            It must be a non-negative integer.
        

        For further reference, you may check the GTFS documentation in https://developers.google.com/transit/gtfs/reference/#routestxt
    """

    # constants
    LIGHT_RAIL = 0
    SUBWAY = 1
    RAIL = 2
    BUS = 3
    FERRY = 4
    CABLE_TRAM = 5
    AERIAL_LIFT = 6
    FUNICULAR = 7  

    #required attributes
    
    route_id = attr.ib(type=int, validator=instance_of(int))
    route_type = attr.ib(type=int, validator=instance_of(int))
    

    #optional attributes with default
    agency_id = attr.ib(type=int, validator=instance_of(int), default=0)
    short_name = attr.ib(type=str, validator=instance_of(str), default="")
    long_name = attr.ib(type=str, validator=instance_of(str), default="")
    desc = attr.ib(type=str, validator=instance_of(str), default="")
    url = attr.ib(type=str, validator=instance_of(str), default="")
    color = attr.ib(type=str, validator=instance_of(str))
    text_color = attr.ib(type=str, validator=instance_of(str))
    sort_order = attr.ib(type=int, validator=instance_of(int), default=0)

        
    #extra parameters
    options = attr.ib(type=dict, validator=instance_of(dict), default={})

    @route_type.default
    def type_default(self):
        return Route.BUS

    @color.default
    def color_default(self):
        return "FFFFFF"

    @text_color.default
    def text_color_default(self):
        return "000000"

    @classmethod
    def as_dict(cls):
        return attr.asdict(cls)





    