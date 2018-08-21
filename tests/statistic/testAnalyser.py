# -*- coding:utf-8 -*-
'''
Created on 13 april 2013

@author: vl
'''
import unittest
from statistic.analyser import Analyser


class TestAnalyser(unittest.TestCase):

    def setUp(self):
        import os
        self.__filename = os.path.join(os.path.dirname(__file__),'site.test.log')
        self.__logdata = list()
        self.__logdata.append(["172.0.0.1", "google.com", "ua"])
        self.__logdata.append(["172.0.0.2", "google.com", "en"])
        self.__logdata.append(["172.0.0.1", "google.com/index/", "ru"])
        self.createFile()
        
        self.__countries = ["ua","en","ru"]
        
        self.__resources = ["/index/", "/"]
        
        self.__analyser = Analyser(self.__filename)
        self.__analyser.load_file()

    def tearDown(self):
        import os
        os.remove(self.__filename)

    def createFile(self):
        f = open(self.__filename,'w')
        for r in self.__logdata:
            f.write("\t".join(r))
            f.write("\n")
        f.close()             
   
    def testCountriesList(self):
        actual = list(self.__analyser.countries())
        expected = self.__countries

        actual.sort()
        expected.sort()

        self.assertListEqual(actual, expected)  

    def testResourcesList(self):
        resources = self.__analyser.resources()
        actual, expected = list(resources), list(self.__resources)

        actual.sort()
        expected.sort()
        
        self.assertListEqual(actual, expected)


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
