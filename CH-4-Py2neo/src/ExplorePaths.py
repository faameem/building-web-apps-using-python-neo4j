'''
Created on 14-Mar-2015

@author: sagupta
'''
import py2neo
from py2neo import Graph, Node, Path, Rev

def connectGraph():
    # Authenticate the user using py2neo.authentication
    # Ensure that you change the password 'sumit' as per your database configuration.
    py2neo.authenticate("localhost:7474", "neo4j", "sumit")
    # Connect to Graph and get the instance of Graph
    graph = Graph("http://localhost:7474/db/data/")
    return graph

def createPaths():
    #Connect to Neo4j Database
    graph = connectGraph()
    #Let us define few Nodes
    bradley,matthew,lisa = Node(name="Bradley"),Node(name="Matthew"), Node(name="Lisa")
    #Connect these Node and form a Path
    path_1 = Path(bradley,"Knows",matthew,Rev("Knows"),lisa)
    #Let us create this Path on the server
    graph.create(path_1)
    #Let us create some more Nodes
    john, annie, ripley = Node(name="John"), Node(name="Annie"), Node(name="Ripley")
    #Define another Path for these New Nodes
    path_2 = Path(john,"Knows",annie,"Knows",ripley)
    #Now, we will join path_1 and path_2 using function append(), and it will give us a new path
    path_3 = path_1.append("Knows",path_2)
    #Let us Create this new path in the server
    resultPath = graph.create(path_3)
    
    #Now we will print and see the results on the Console
    print("Print Raw Data")
    print("Nodes in the Path-1 = ",resultPath[0].nodes)
    print("Relationships in the Path-1 = ",resultPath[0].relationships)
    
    print("Print - All Relationships")
    for rels in resultPath[0].relationships:
        print(rels)
        
if __name__ == '__main__':
    createPaths()
    