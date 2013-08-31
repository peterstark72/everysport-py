#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''Example use of everysport.events queries'''

import os
import everysport

APIKEY = os.environ['EVERYSPORT_APIKEY']

es = everysport.Everysport(APIKEY)


for e in es.get_events_query().football().today():
    print e








