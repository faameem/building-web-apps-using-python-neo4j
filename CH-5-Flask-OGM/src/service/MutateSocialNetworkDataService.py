'''
Created on 22-Mar-2015

@author: sagupta
'''

from flask import Flask, request,jsonify
from flask_restful import Api, Resource 
from model.SocialDataModel import Person
from operations.ExecuteCRUDOperations import CreateNodesRelationships,UpdateNodesRelationships,DeleteNodesRelationships
from operations.ExecuteSearchOperations import SearchMovie,SearchPerson
from http.client import HTTPException

webapp = Flask(__name__)
api = Api(webapp)

#Class for handling all kinds of create operations on Nodes
createOperation = CreateNodesRelationships('localhost','7474','neo4j','sumit')
#Class for handling all kinds of update operations on Nodes
updateOperation = UpdateNodesRelationships('localhost','7474','neo4j','sumit')
#Class for handling all kinds of delete operations on Nodes
deleteOperation = DeleteNodesRelationships('localhost','7474','neo4j','sumit')
#Class for handling all kinds of search operations on Nodes 
searchMovie = SearchMovie('localhost','7474','neo4j','sumit')
#Class for handling all kinds of search operations on Nodes
searchPerson = SearchPerson('localhost','7474','neo4j','sumit')


class PersonService(Resource):
    '''
    Defines operations with respect to Entity - Person 
    '''
    #example - GET http://localhost:5000/person/Bradley    
    def get(self, name):
        node = searchPerson.searchPerson(name)
        #Convert into JSON and return it back
        return jsonify(name=node[0].name,surName=node[0].surname,age=node[0].age,country=node[0].country)
    
    #POST http://localhost:5000/person
    #{"name": "Bradley","surname": "Green","age": "24","country": "US"}
    def post(self):
        
        jsonData = request.get_json(cache=False)
        attr={}
        for key in jsonData:
            attr[key]=jsonData[key]
            print(key,' = ',jsonData[key] )
        person = createOperation.createPerson(attr['name'],attr['surname'],attr['age'],attr['country'])
        createOperation.save('person',person)
        
        return jsonify(result='success')
    #POST http://localhost:5000/person/Bradley
    #{"name": "Bradley1","surname": "Green","age": "24","country": "US"}    
    def put(self,name):
        oldNode = searchPerson.searchPerson(name)
        jsonData = request.get_json(cache=False)
        attr={}
        for key in jsonData:
            attr[key] = jsonData[key]
            print(key,' = ',jsonData[key] )
        newNode = Person(attr['name'],attr['surname'],attr['age'],attr['country'])
        
        updateOperation.updatePersonNode(oldNode[0],newNode)

        return jsonify(result='success')
    
    #DELETE http://localhost:5000/person/Bradley1
    def delete(self,name):
        node = searchPerson.searchPerson(name)
        deleteOperation.deletePersonNode(node[0])
        return jsonify(result='success')
    
class MovieService(Resource):
    '''
    Defines operations with respect to Entity - Movie
    '''
    #GET http://localhost:5000/movie/Avengers
    def get(self, movieName):
        node = searchMovie.searchMovie(movieName)
        return jsonify(name=node[0].movieName)
    
    #POST http://localhost:5000/movie
    #{"movieName":"Avengers"}
    def post(self):
        jsonData = request.get_json(cache=False)
        attr={}
        for key in jsonData:
            attr[key]=jsonData[key]
            print(key,' = ',jsonData[key] )
        
        movie=createOperation.createMovie(attr['movieName'])
        createOperation.save('movie',movie)
        return jsonify(result='success')
    
    
    def put(self):
        return {'Not Supported' : 'true'}
    
    #DELETE http://localhost:5000/movie/Avengers
    def delete(self,movieName):
        node = searchMovie.searchMovie(movieName)
        deleteOperation.deleteMovieNode(node[0])
        return {'result':  'success'}

class RelationshipService(Resource):
    
    def get(self):
        return {'Not Supported' : 'true'}
    
    '''
    Assuming that the given nodes are already created this operation 
    will associate Person Node either with another Person or Movie Node.
    
    Request for Defining relationship between 2 persons: -
        POST http://localhost:5000/relationship/person/Bradley
        {"entity_type":"person","person.name":"Matthew","relationship": "FRIEND"}
    Request for Defining relationship between Person and Movie
        POST http://localhost:5000/relationship/person/Bradley
        {"entity_type":"Movie","movie.movieName":"Avengers","relationship": "HAS_RATED"
         "relationship.ratings":"4"}
    '''
    def post(self, entity,name):
        jsonData = request.get_json(cache=False)
        attr={}
        for key in jsonData:
            attr[key]=jsonData[key]
            print(key,' = ',jsonData[key] )
            
        if(entity == 'person'):
            startNode = searchPerson.searchPerson(name)
            if(attr['entity_type']=='movie'):
                endNode = searchMovie.searchMovie(attr['movie.movieName'])
                createOperation.createHasRatedRelationship(startNode[0], endNode[0], attr['relationship.ratings'])
                createOperation.save('person', startNode[0])
            elif (attr['entity_type']=='person' and attr['relationship']=='FRIEND'):
                endNode = searchPerson.searchPerson(attr['person.name'])
                createOperation.createFriendRelationship(startNode[0], endNode[0])
                createOperation.save('person', startNode[0])
            elif (attr['entity_type']=='person' and attr['relationship']=='TEACHES'):
                endNode = searchPerson.searchPerson(attr['person.name'])
                createOperation.createTeachesRelationship(startNode[0], endNode[0])
                createOperation.save('person', startNode[0])
        else:
            raise HTTPException("Value is not Valid")
  
        return jsonify(result='success')
    
    def put(self):
        return {'Not Supported' : 'true'}
    
    def delete(self,entity,name):
        return {'Not Supported' : 'true'}
    
    
if __name__ == '__main__':
    api.add_resource(PersonService,'/person','/person/<string:name>')
    api.add_resource(MovieService,'/movie','/movie/<string:movieName>')
    api.add_resource(RelationshipService,'/relationship','/relationship/<string:entity>/<string:name>')
    webapp.run(debug=True)
    
    