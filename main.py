from flask import Flask, request, render_template
import random
from bitcoin.bitcoin import bitcoin_blueprint

app = Flask(__name__)

app.register_blueprint(bitcoin_blueprint, url_prefix = "/btc")

@app.route('/', methods=['GET'])  # получить что-то
def get():
    return render_template('index.html')


@app.route('/post', methods=['POST'])  # сохранить что-то
def post():
    return request.values


@app.route('/put', methods=['PUT'])  # изменить что-то
def test_put():
    return request.values


@app.route('/delete', methods=['DELETE'])  # удалить что-то
def test_delete():
    return request.values


@app.route('/test/<int:get_id>/<name>', methods=['GET'])
def test_params(get_id: int, name):
    return f"{get_id} = {name}"


@app.route('/test2/<path:sub>', methods=['GET'])
def test_params2(sub):
    return render_template('test2.html', sub=sub)


"""
1. через урл передать запросом GET number1, number2, operation = [add, sub, mul, div]
/cals/1/add/2
2. используя функции из модуля calc.py произвести расчет введенного выражения
3. ответ передать в шаблоне с названием calc_result.htlm
"""


@app.route('/calcs/<int:number_1>/<operation>/<int:number_2>')
def calcs(number_1, operation, number_2):
    from calc import process, http_available_operations
    result = process(number_1, operation, number_2, http_available_operations)
    return render_template('calc.html', result=result)


@app.route('/primer')
def index():
    with open('words.txt', 'r') as word_file:
        words = word_file.readlines()
    return ''.join(words)

@app.route('/form', methods=['GET', 'POST'])
def form():
    return render_template('form.html', request=request.values)

"""
при заходе на некоторый урл (путь сам выбери)
фласк возврщает список слов из файла words.txt.txt
"""

if __name__ == '__main__':
    app.run(debug=True)
