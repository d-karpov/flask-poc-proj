# About
This's small REST app was made like as proof of concept. Solution based on flask+uWSGI+nginx and running as docker multy-containers app (for non-docker build see branch 'non-docker-proj').

Task is very simple - find shortest path between two points setted as *city_start* and *city_finish* variables of request based on given *matrix_distance* then show it with distance value. Also simple API key validation was used.

# Installation
- [x] Make shure that you have installed docker and all requirements for it. This [link](https://docs.docker.com/engine/install/ubuntu/) may help.
- [x] Copy repo.
- [x] run following code:

		$ cd flask-poc-proj
		$ sudo docker-compose up --build

# Testing 
After installation done let's make test from other TTY:
		
	$ curl -G "http://127.0.0.1/?city_start=3&city_finish=43"
Will return:

	{
  	"body": "401: The server could not verify that you are authorized to access the URL requested. You either supplied the wrong credentials (e.g. a bad password), or your browser doesn't understand how to supply the credentials required."
	}
Let's add API key into header request:
		
	$ curl -H "x-api-key: 123321" -G "http://127.0.0.1/?city_start=3&city_finish=43"
		
Will return:	
     
	{
		"body": {
			"path": [
				3,
				42,
				43
			],
			"distance": 2
		}
	}



		 
