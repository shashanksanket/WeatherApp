# WeatherApp

#### How to run the app? 

##### Set up the virtual env

##### Install the libs
```
pip install -r requirements.txt             //Install dependencies from requirements.txt file                    
      
cd weatherApp                               //Go to weatherApp folder

python manage.py runserver                  //runserver

```

##### Make sure we have installed the readis, and it is running on the default port

##### Start the celery worker using the following command:-

```
celery --app=weatherApp worker -l INFO
```

##### Start the beat a celery scheduler [ Note: for the demonstration i added 20sec, but we configure it to 30mins in code ] 

```
celery -app=weatherApp beat -l INFO
```

##### Test Creads
``` 
Credentials:-
  Username:- admin
  Password:- admin
```
