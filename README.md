# gantt
 
Status : Progress 

# Steps to Follow
  
  1. Check and test on the cmd that python up and running. 
    
  2. Locate to the folder, and install the required packages on the machine for that use command

    ```
        pip install -r requirements.txt
    ``` 
  3. Once all packages were install then, set the flask ENV and set APP.
  
    ## For windows

        ```
            set FLASK_ENV=development
            set FLASK_APP=app.py
        ```        
    
    ## For linux

        ```
            export FLASK_ENV=development
            export FLASK_APP=app.py
        ```
  4. Now for start the flask server 

    ```
        flask run
    ```
  5. Now, app is serving over 127.0.0.1:5000   
