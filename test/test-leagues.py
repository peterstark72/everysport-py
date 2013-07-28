#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import os


import everysport

APIKEY = os.environ['EVERYSPORT_APIKEY'] 


class TestLeagues(unittest.TestCase):

    def setUp(self):        
        self.es = everysport.Everysport(APIKEY)


    def test_allsvenskan(self):
        allsvenskan = self.es.getleague(everysport.ALLSVENSKAN)
        self.assertTrue(allsvenskan) 


    def test_season(self):
        allsvenskan = self.es.getleague(everysport.ALLSVENSKAN)
        self.assertTrue(allsvenskan.season.isactive())   


    def test_sport(self):
        hockey = self.es.leagues.sport("Hockey")
        for league in hockey:
            self.assertEqual(league.sport.id, 2) 




if __name__ == '__main__': 
    unittest.main()