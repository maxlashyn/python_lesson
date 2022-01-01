from flask import Flask, request, render_template
from bitcoin.bitcoin import bitcoin_blueprint
from convey.convey import convey_blueprint
from gallows.gallows import gallows_blueprint
from parsing.parsing import parsing_blueprint
app = Flask(__name__)

app.register_blueprint(parsing_blueprint, url_prefix="/parse")

app.register_blueprint(bitcoin_blueprint, url_prefix="/btc")

app.register_blueprint(convey_blueprint, url_prefix = "/start")

app.register_blueprint(gallows_blueprint, url_prefix = "/start_gallows")
"""
1. Вынести в блюпринты convey и gallows, и переделать урлы если  надо
2. В index.html прописать к ним ссылки
3. в шаблонах этих блюпринтов добавить ссылки на главную страницу
"""

@app.route('/', methods=['GET'])  # получить что-то
def get():
    return render_template('index.html')


@app.route('/test/<int:get_id>/<name>', methods=['GET'])
def test_params(get_id: int, name):
    return f"{get_id} = {name}"


@app.route('/test2/<path:sub>', methods=['GET'])
def test_params2(sub):
    return render_template('test2.html', sub=sub)


@app.route('/calcs/<int:number_1>/<operation>/<int:number_2>')
def calcs(number_1, operation, number_2):
    from bc.calc import process, http_available_operations
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


if __name__ == '__main__':
    app.run(debug=True)
