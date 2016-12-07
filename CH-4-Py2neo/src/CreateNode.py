'''
Created on 09-Mar-2015

@author: sagupta
'''

import py2neo
from py2neo import Graph, Node

def creatNodeWithLabelProperties():
    print("Start - Creating Node with Label and Properties")
    # Authenticate the user using py2neo.authentication
    # Ensure that you change the password 'sumit' as per your database configuration.
    py2neo.authenticate("localhost:7474", "neo4j", "sumit")
    # Connect to Graph and get the instance of Graph
    graph = Graph("http://localhost:7474/db/data/")
    # Create Nodes, where all positional arguments to constructor is Label.
    # And rest (keyword arguments) are Node Properties.
    #Below is a Node with 1 Label and 2 properties 
    node1 = Node("FirstLabel", name="MyPythonNode1", neo4j_version="2.2")
    #Below is a Node with 2 Label and 2 properties
    node2 = Node("FirstLabel", "SecondLabel",name="MyPythonNode2", neo4j_version="2.2")
    #Now Use object of graph to create Node, the return type is a python tuple
    #Multiple Nodes can be created in a single Graph command 
    resultNodes = graph.create(node1, node2)
    #Iterate Over Tuple and print all the values in the Tuple
    for index in range(len(resultNodes)):
        print("Created Node - ", index, ", ", resultNodes[index])
    print("End - Creating Node with Label and Properties")


def createNodeWithLabelPropertiesWithCast():
    print("Start - Creating Node with Label and Properties")
    # Authenticate the user using py2neo.authentication
    # Ensure that you change the password 'sumit' as per your database configuration.
    py2neo.authenticate("localhost:7474", "neo4j", "sumit")
    # Connect to Graph and get the instance of Graph
    graph = Graph("http://localhost:7474/db/data/")
    #Define a LIST of Labels
    labels = [ 'FirstLabel' ,'SecondLabel' ]
    #Define a DICTIONARY
    properties = {'name':'MyPythonNode2', 'neo4j_version':'2.2'}
    #CAST the node and invoke graph.create method.
    node = Node.cast(labels,properties)
    resultNode, = graph.create(node)
    print("Node - ", resultNode)
        
    print("End - Creating Node with Label and Properties")                                  

if __name__ == '__main__':
    print("Start Creating Nodes")
    creatNodeWithLabelProperties
    createNodeWithLabelPropertiesWithCast()
    print("End Creating Nodes")      
      
