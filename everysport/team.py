#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''team.py

Everysport teams are defined with an ID. They always have a name, and may also have a short name and an abbreviation.


'''

from collections import namedtuple


class Team(namedtuple('Team', "id, name, short_name, abbreviation")):
    '''Team object

    Properties:
    id - Everysport Team ID
    name - e.g. "Malmö FF"
    short_name - e.g. "Malmö"
    abbreviation - e.g. "MFF"

    '''
    __slots__ = () 
    @classmethod
    def from_dict(cls, data):
        return cls(
            data.get('id', None),
            data.get('name', None),
            data.get('short_name', None),
            data.get('abbreviation', None)
        )


    def __str__(self):
        return self.name.encode('utf-8')

    def __eq__(self, other):
        return self.id == other.id