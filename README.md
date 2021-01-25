# About
This's small REST app was made like as proof of concept. Solution based on flask.

Task is very simple - find shortest path between two points setted as *city_start* and *city_finish* variables of request based on given *matrix_distance* then show it with distance value. Also simple API key validation was used.

# Installation for Windows
:white_check_mark: Copy repo.     
:white_check_mark: Inside the repo folder make virtual enviroment for testing and activate it:    
      
      >python -m venv env
      >/env/Scripts/activate
:white_check_mark: Install all required python modules and start app :    

      (env)>pip install -r requirements.txt
      (env)>/flask/run.py

If all goes right you'll see something like this:

       * Serving Flask app "app" (lazy loading)
       * Environment: production
         WARNING: This is a development server. Do not use it in a production deployment.
         Use a production WSGI server instead.
       * Debug mode: off
       * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
# Testing 
After installation done let's make test from other console:
		
	>curl -G "http://127.0.0.1:5000/?city_start=3&city_finish=43"
Will return:

	{
  	"body": "401: The server could not verify that you are authorized to access the URL requested. You either supplied the wrong credentials (e.g. a bad password), or your browser doesn't understand how to supply the credentials required."
	}
Let's add API key into header request:
		
	>curl -H "x-api-key: 123321" -G "http://127.0.0.1:5000/?city_start=3&city_finish=43"
		
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
