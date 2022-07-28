from celery import Celery
from .views import fetchWeatherReport
from weatherApp.celery import app
import datetime

@app.task(name='tasks.fetchWeatherReportTask')
def fetchWeatherReportTask():
    fetchWeatherReport()
    print("Fetching latest weather report : " + str(datetime.datetime.now()))