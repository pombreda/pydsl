#!/usr/bin/python
# -*- coding: utf-8 -*-
#This file is part of ColonyDSL.
#
#ColonyDSL is free software: you can redistribute it and/or modify
#it under the terms of the GNU General Public License as published by
#the Free Software Foundation, either version 3 of the License, or
#(at your option) any later version.
#
#ColonyDSL is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#GNU General Public License for more details.
#
#You should have received a copy of the GNU General Public License
#along with ColonyDSL.  If not, see <http://www.gnu.org/licenses/>.

"""Abstract Classes"""

__author__ = "Néstor Arocha Rodríguez"
__copyright__ = "Copyright 2008-2012, Néstor Arocha Rodríguez"
__email__ = "nesaro@colonymbus.com"

import logging
LOG = logging.getLogger("Abstract")
from abc import ABCMeta, abstractmethod, abstractproperty

class Singleton(type):
    """singleton pattern metaclass"""
    #Only problem here is that classes can't have two metaclasses (ABCMeta conflict)
    def __init__(self, name, bases, dct):
        self.__instance = None
        type.__init__(self, name, bases, dct)
    def __call__(self, *args, **kw):
        if self.__instance is None:
            self.__instance = type.__call__(self, *args,**kw)
        return self.__instance
 
class InmutableDict(dict):
    """A dict with a hash method for dictionary use"""
    def __hash__(self):
        if not self:
            return 0
        items = tuple(self.items())
        res = hash(items[0])
        for item in items[1:]:
            res ^= hash(item)
        return res

    def __eq__(self, other):
        if len(self.keys()) != len(other.keys()):
            return False
        for key in self:
            if other[key] != self.__getitem__(key):
                return False
        return True

class Indexable(metaclass = ABCMeta):
    """ This class is searchable """
    def __init__(self, identifier):
        self.identifier = identifier

    def rename(self, identifier):
        """Permite renombrar un elemento indexable"""
        self.identifier = identifier

    @abstractproperty
    def summary(self) -> InmutableDict:
        pass

    @classmethod
    def ancestors(cls):
        result = [cls.__name__]
        for x in cls.__bases__:
            if issubclass(x, Indexable):
                if not x in result:
                    result += x.ancestors()
        return tuple(result)

class Event:
    def __init__(self, source, destination, msgid:int, content):
        self.source = source 
        self.destination = destination 
        self.msg = content
        self.msgid = msgid

class TypeCheckList(list):
    def __init__(self, instancetype, *args):
        self.instancetype = instancetype
        list.__init__(self, *args)

    def append(self, item):
        assert(isinstance(item, self.instancetype))
        list.append(self, item)

    def __add__(self, item):
        for element in item:
            assert(isinstance(element, self.instancetype))
        return list.__add__(self, item)

    def __iadd__(self, item):
        for element in item:
            assert(isinstance(element, self.instancetype))
        return list.__iadd__(self, item)

class HostInterface(metaclass = ABCMeta):
    pass

