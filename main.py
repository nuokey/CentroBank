from flask import Flask
from flask import render_template

import requests

app = Flask(__name__)

@app.route('/')
def main():
    site = requests.get('https://www.cbr-xml-daily.ru/daily_json.js')
    data = site.json()

    date = data['Date']

    return render_template('index.html', date=date)

@app.route('/dollar')
def dollar():
    site = requests.get('https://www.cbr-xml-daily.ru/daily_json.js')
    data = site.json()

    date = data['Date']

    cost = round(float(data['Valute']['USD']['Value']), 2)

    difference = round(100 - float(cost)  * 100 / float(data['Valute']['USD']['Previous']), 2)
    if difference > 0:
        difference = '+' + str(difference)
    else:
        pass


    return render_template('dollar/index.html', date=date, cost=cost, difference=difference)

app.run()