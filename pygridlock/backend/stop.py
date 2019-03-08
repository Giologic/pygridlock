# -*- coding: utf-8 -*-

"""
    Stop Class Backend

    This module implements a Stop class containing attributes such as stop_id, latitude, longitude, options, etc.
"""

import attr
import pytz
from collections import namedtuple
from attr.validators import instance_of



@attr.s
class Stop(object):
    """ GTFS Stop Class

        This class follows the implementation of a gtfs stops.txt file. This class will only 
        require you to supply the following parameters: stop_id, name, latitude, longitude.

        Required Attributes
        ----------
        stop_id : int
            ID that uniquely identifies a stop, station, or station entrance.
        lat : float
            contains the latitude of a stop, station, or station entrance.
        lon : float
            contains the longitude of a stop, station, or station entrance.


        Optional Attributes
        ----------
        name : str (Required but default is an empty string)
            contains the name of a stop, station, or station entrance.
        code : str
            short text or a number that uniquely identifies the stop for passengers.
        desc : str
            contains a description of a stop.
        zone_id : int
            defines the fare zone for a stop ID. Zone IDs are required if you want 
            to provide fare information using fare_rules.txt.
        url : str
            contains the URL of a web page about a particular stop.
        location_type : int
            identifies whether this stop ID represents a stop, station, or station entrance.
        parent_station : int
            for stops that are physically located inside stations, the parent_station field
            identifies the station associated with the stop.
        timezone : str
            field contains the timezone in which this stop, station, or station entrance is located.
        wheelchair_boarding : int
            identifies whether wheelchair boardings are possible from the specified stop, station, or station entrance.

        For further reference, you may check the GTFS documentation in https://developers.google.com/transit/gtfs/reference/#stopstxt
    """

    #required attributes
    stop_id = attr.ib(type=int, validator=instance_of(int))
    lat = attr.ib(type=float , validator=instance_of(float))
    lon = attr.ib(type=float, validator=instance_of(float))

    #optional attributes with default
    name = attr.ib(type=str, validator=instance_of(str), default="")
    code = attr.ib(type=str, validator=instance_of(str), default="")
    desc = attr.ib(type=str, validator=instance_of(str), default="")
    zone_id = attr.ib(type=int, validator=instance_of(int), default=0)
    url = attr.ib(type=str, validator=instance_of(str), default="")
    location_type = attr.ib(type=int, validator=instance_of(int), default=0)
    parent_station = attr.ib(type=int, validator=instance_of(int), default=0)
    timezone = attr.ib(type=str, validator=instance_of(str))
    wheelchair_boarding = attr.ib(type=int, validator=instance_of(int), default=0)

    #extra parameters
    options = attr.ib(type=dict, validator=instance_of(dict), default={})
    
    @timezone.default
    def timezone_default(self):
        return str(pytz.timezone('Asia/Singapore'))

    @classmethod
    def as_dict(cls):
        return attr.asdict(cls)

    def as_tuple(self):
        return (self.lat, self.lon)
        

if __name__ == "__main__":
    s = Stop(stop_id=1, lat=12.86, lon=118.23)
    print(s.as_tuple())

    





    