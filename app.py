from flask import Flask, render_template, redirect, url_for
import requests

app = Flask(__name__)

NASA_API_KEY= "Cl7lyEwEct4zRGrTjGKSP4JzO0H0kimltbhWbNQ2"

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/nasa')
def nasa_home():
    response = requests.get(f'https://api.nasa.gov/planetary/apod?api_key={NASA_API_KEY}')
    data = response.json()
    return render_template('nasa.html', title=data.get("title"), description=data("explanation"), image=data.get('url'))

@app.route('/cat')
def cat_home():
    response = requests.get('https://catfact.ninja/fact')
    data = response.json()
    return render_template('cat.html', fact=data.get("fact"))

if __name__ == '__main__':
    app.run(debug=True)