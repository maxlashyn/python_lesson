"""
1. создать урл (гет) для фласка
при переходе на который мы получим данные о стоимости
биткоина в гривнах
2. Для получения стоимости биткоина в долларах
используем апи https://api.coindesk.com/v1/bpi/currentprice.json
3. Для конвертации в гривны испльзовать апи
https://openexchangerates.org/api/latest.json?app_id=3a70b529858a40c9b08f32bbd3b1e850&base=USD
в нем найти курс рубля и пересчитать стоимость биткоина в рубли

"""

import requests
import json
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/bitcoin', methods=['GET'])
def bitcoin():
    rate = bitcoin_in_dollars()
    rate_in_rub = rate * course_usd_to_rub()
    return render_template('bitcoin.html',rate = rate_in_rub)

def bitcoin_in_dollars():
    result = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
    content = json.loads(result.content)
    return content['bpi']['USD']['rate_float']

def course_usd_to_rub():
    result = requests.get('https://openexchangerates.org/api/latest.json?app_id=3a70b529858a40c9b08f32bbd3b1e850&base=USD')
    content = json.loads(result.content)
    return content['rates']['RUB']


if __name__ == '__main__':
    app.run()