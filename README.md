# WeatherApp

pip install -r requirements.txt             //Install dependencies from requirements.txt file
mkvritualenv env-name                       //Setup a virtual enviroment:-
env-name\Scripts\activate                   //Activate your virtuale enviroment
cd weatherApp                               //Go to weatherApp folder
python manage.py runserver                  //Runserver

Start the celery worker using the following command:-

celery --app=weatherApp worker -l INFO

Start the beat a celery scheduler [ Note: for the demonstration i added 20sec, but we configure it to 30mins in code ] 

celery -app=weatherApp beat -l INFO


Credentials:-
  Username:- admin
  Password:- admin
