
# API Coalescing

This example tests the coalescence of many API responses

## API list
  - In the config.py file you can update the api url list in order to 
    increase/decrease the amount of apis where you will retrieve the data.

## Running
  - To run the project run the `src/app.py` file to start the flask application:
    ```python src/app.py```
  - To test the api use the route http://127.0.0.1:5000/api/data?member_id=1 
  - Since we are using test data all the requests returns sample response, 
    to use real calls you must update the api_base_urls config variable and 
    
## Strategies
  - Modify the constant `STRATEGY` in the `src/config.py` file to assign the coalescence strategy.
  - There are 3 different kind of coalescence strategies you can apply:
    1. `avg`: returns the average value of every field.
    2. `min`: returns the min value for every field.
    3. `max`: returns the max value for every field.
    
## Tests
  You can run the tests by running the `src/tests.py` test file.
  
   ```$ python src/tests.py ```

## Running in Docker
  - To run the project using docker run the bash script `runserver.sh` this will clean any old container, 
    run the tests and then build and run the container, you will be able to access to the project in the
    url http://0.0.0.0:5001/api/data?member_id=1
  - To stop the server run the bash file `stop_server.sh`