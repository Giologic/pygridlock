# -*- coding: utf-8 -*-

"""
Base class for Network Layouts

Abstract from this Base Class to create your own network layouts.

"""

import abc

class Layout(abc.ABC):
    
    def __init__(self, **kwargs):
        """ Initializes Layout class """

    @abc.abstractmethod
    def generate_layout(self, stops):
        """ Generate Network Layout """
        raise NotImplementedError("Layout::generate_layout()")

    
    