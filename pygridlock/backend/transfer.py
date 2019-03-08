# -*- coding: utf-8 -*-

"""
    Transfer Class Backend

    This module implements a Transfer class containing attributes such as from_stop_id, to_stop_id, options, etc.
"""

import attr
from attr.validators import instance_of


@attr.s
class Transfer(object):
    """ Modified GTFS Transfer Class

        This class follows the implementation of a gtfs transfers.txt file. This class will only 
        require you to supply the following parameters: from_stop_id, to_stop_id, transfer_type

        Required Attributes
        ----------
        from_stop_id : int
            contains a stop ID that identifies a stop or station where a connection between routes begins.
        to_stop_id : int
            contains a stop ID that identifies a stop or station where a connection between routes ends.


        Optional Attributes
        ----------
        transfer_type : int
            specifies the type of connection for the specified :code:`(from_stop_id, to_stop_id)` pair.
        min_transfer_time : int
            defines the amount of time that must be available in an itinerary to permit a transfer between routes at these stops.
            The min_transfer_time value must be entered in seconds, and must be a non-negative integer.
        walking_distance: int
            specifies the walking distance between the sepcified :code:`(from_stop_id, to_stop_id)`
        

        For further reference, you may check the GTFS documentation in 
        https://developers.google.com/transit/gtfs/reference/#transferstxt
    """


    #required attributes
    
    from_stop_id = attr.ib(type=int, validator=instance_of(int))
    to_stop_id = attr.ib(type=int, validator=instance_of(int))
    

    #optional attributes with default
    transfer_type = attr.ib(type=int, validator=instance_of(int), default=0)
    min_transfer_time = attr.ib(type=int, validator=instance_of(int), default=0)
    walking_distance = attr.ib(type=int, validator=instance_of(int), default=0)

        
    #extra parameters
    options = attr.ib(type=dict, validator=instance_of(dict), default={})

    @classmethod
    def as_dict(cls):
        return attr.asdict(cls)






    