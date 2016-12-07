'''
Created on 15-Mar-2015

@author: sagupta
'''
import py2neo
from py2neo import Graph, Node, Relationship, Path, Rev

class CreateSocialNetworkData(object):
    
    def __init__(self):
        '''
        Constructor
        '''
    def connectGraph(self):
        # Authenticate the user using py2neo.authentication
        # Ensure that you change the password 'sumit' as per your database configuration.
        py2neo.authenticate("localhost:7474", "neo4j", "sumit")
        # Connect to Graph and get the instance of Graph
        graph = Graph("http://localhost:7474/db/data/")
        return graph
    
    def createPeople(self,graph):
        print("Creating People")
        bradley = Node('MALE','TEACHER',name='Bradley', surname='Green', age=24, country='US') 
        matthew = Node('MALE','STUDENT',name='Matthew', surname='Cooper', age=36, country='US')
        lisa = Node('FEMALE',name='Lisa', surname='Adams', age=15, country='Canada')
        john = Node('MALE',name='John', surname='Godman', age=24, country='Mexico')
        annie = Node('FEMALE',name='Annie', surname='Behr', age=25, country='Canada')
        ripley = Node('MALE',name='Ripley', surname='Aniston', country='US')
        graph.create(bradley,matthew,lisa,john,annie,ripley)
        print("People Created")
        #Create a Dictionary and return back the nodes for further operations
        people = {'bradley':bradley,'matthew':matthew,'lisa':lisa,'john':john,'annie':annie,'ripley':ripley}
        
        return people
  
    def createFriends(self,graph,people):
        print("Creating Relationships between People")
        
        path_1 = Path(people['bradley'],'FRIEND',people['matthew'],'FRIEND',people['lisa'],'FRIEND',people['john'])
        path_2 = path_1.prepend(people['lisa'],Rev('FRIEND'))
        path_3 = Path(people['annie'],'FRIEND',people['ripley'],'FRIEND',people['lisa'])
        path_4 = Path(people['bradley'],'TEACHES',people['matthew'])
        
        friendsPath = graph.create(path_2,path_3,path_4)
        
        print("Finished Creating Relationships between People")

        return friendsPath

    def createMovies(self,graph):
        print("Creating Movies")
        firstBlood = Node('MOVIE',name='First Blood')
        avengers = Node('MOVIE',name='Avengers')
        matrix = Node('MOVIE',name='matrix')
        graph.create(firstBlood,avengers,matrix)
        print("Movies Created")
        
        movies = {'firstBlood':firstBlood,'avengers':avengers,'matrix':matrix}
        return movies
         
    def rateMovies(self,graph,movies,people):
        print("Start Rating the Movies")
        
        matthew_firstBlood = Relationship(people['matthew'],'HAS_RATED',movies['firstBlood'],ratings=4)
        john_firstBlood = Relationship(people['john'],'HAS_RATED',movies['firstBlood'],ratings=4)
        annie_firstBlood = Relationship(people['annie'],'HAS_RATED',movies['firstBlood'],ratings=4)
        ripley_firstBlood = Relationship(people['ripley'],'HAS_RATED',movies['firstBlood'],ratings=4)
        lisa_avengers = Relationship(people['lisa'],'HAS_RATED',movies['avengers'],ratings=5)
        matthew_avengers = Relationship(people['matthew'],'HAS_RATED',movies['avengers'],ratings=4)
        annie_avengers = Relationship(people['annie'],'HAS_RATED',movies['avengers'],ratings=3)
        
        moviesPath = graph.create(matthew_firstBlood,john_firstBlood,annie_firstBlood,ripley_firstBlood,lisa_avengers,matthew_avengers,annie_avengers)
        
        print("Finished Rating the Movies")
        return moviesPath
        

if __name__ == '__main__':
    print("Start Creating Social Network Data")
    #Create an Object of Class
    data = CreateSocialNetworkData()
    #Connect to Graph
    graph = data.connectGraph()
    #Create People - Male and Females
    people = data.createPeople(graph)
    #Create Relationships between People
    friendsPath = data.createFriends(graph,people)
    #Create Movies
    movies = data.createMovies(graph)
    #Rate Movies
    ratings = data.rateMovies(graph,movies,people)
    print("Finished Creating Social Network Data")
    
    