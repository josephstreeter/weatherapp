from flask import Flask, request, jsonify, render_template, redirect, url_for
import os, requests, json

app = Flask(__name__)

def getHoulryForecast():
    URL = 'https://api.weather.gov/gridpoints/MKX/50,80/forecast/hourly'
    response = requests.get(URL)
    forecast = response.json()
    return forecast

def getDailyForecast():
    URL = 'https://api.weather.gov/gridpoints/MKX/50,80/forecast'
    response = requests.get(URL)
    forecast = response.json()
    return forecast

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/forecast_hourly')
def forecastHourly():
    forecast_hourly = getHoulryForecast()
    forecasts = forecast_hourly['properties']['periods']
    return render_template('forecast_hourly.html', forecasts = forecasts)

@app.route('/forecast_daily')
def forecastDaily():
    forecast_hourly = getDailyForecast()
    forecasts = forecast_hourly['properties']['periods']
    print(forecasts)
    return render_template('forecast_daily.html', forecasts = forecasts)

@app.route('/links')
def links():
    return render_template('links.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)