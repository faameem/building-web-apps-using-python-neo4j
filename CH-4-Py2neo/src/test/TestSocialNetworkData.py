'''
Created on 15-Mar-2015

@author: sagupta
'''
import unittest

from CreateSocialNetworkData import *

class TestingGraph(unittest.TestCase):
    
    def testServerConnection(self):
        graph = CreateSocialNetworkData.connectGraph(self)
        #Check whether Graph Object is created and bound to the remote entities
        self.assertTrue (graph.bound)
    

class TestingNodes(unittest.TestCase):


    def setUp(self):
        py2neo.authenticate("localhost:7474", "neo4j", "sumit")
        # Connect to Graph and get the instance of Graph
        graph = Graph("http://localhost:7474/db/data/")
        self.graph = graph


    def tearDown(self):
        self.graph.unbind()

    def testLabelCount(self):
        results = self.graph.cypher.execute("MATCH (n) return count(DISTINCT labels(n)) as countLabel")
        #We should have only 5 Labels "FEMALE(2) MALE(4) MOVIE(3) STUDENT(1) TEACHER(1)"
        self.assertEqual(5, results[0].countLabel)
        
    def testIndividualNodes(self):
        #Define a Node which we need to check
        bradley = Node('MALE','TEACHER',name='Bradley', surname='Green', age=24, country='US') 
        #Now get the Node from server
        results = self.graph.cypher.execute("MATCH (n) where n.name='Bradley' return n as bradley")
        #Both Nodes should be equal
        self.assertEqual(results[0].bradley,bradley)
        
class TestingPaths(unittest.TestCase):
    def setUp(self):
        py2neo.authenticate("localhost:7474", "neo4j", "sumit")
        # Connect to Graph and get the instance of Graph
        graph = Graph("http://localhost:7474/db/data/")
        self.graph = graph


    def tearDown(self):
        self.graph.unbind()
        
    def testPathFRIENDExists(self):
        #Query whether there are Nodes linked with Relationship - FRIEND
        results = self.graph.cypher.execute("MATCH (n{name:'Bradley'})-[r:FRIEND]->(n1{name:'Matthew'}) return count(r) as countPath")
        #Ensure that count=1. Not more, neither less
        self.assertEqual(1,results[0].countPath)
        
    def testPathTEACHESFRIENDExists(self):
        #Query whether there are Nodes linked with Relationship - TEACHES
        results = self.graph.cypher.execute("MATCH (n{name:'Bradley'})-[r:TEACHES]->(n1{name:'Matthew'}) return count(r) as countPath")
        #Ensure that count=1. Not more, neither less
        self.assertEqual(1,results[0].countPath)
        
        
            