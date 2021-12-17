"""
1. создать  объект фласк
2. создать роуты и функции для игры "жизнь"
- (get) главная страница с формой в которой мы можем задать высоту и ширину поля
- (post) генерируем игру с заполненным полем,
+ выводим ее в шаблоне  в виде таблицы.
 кроме того в шаблоне помещаем форму со скрытым полем содержащим сериализованную игру + размеры поля
 и кнопку "следующий шаг"
- (post) заполнение данных игры из десериализованного объекта, расчет хода, вывод результата через +

"""

from flask import Flask, render_template,url_for,request

app = Flask(__name__)


@app.route('/start', methods=['GET'])
def start():
    return render_template('game_convey.html')


@app.route('/init', methods=['POST'])
def init_game():
    from life import Game
    width = int(request.form.get('width'))
    height = int(request.form.get('height'))
    game = Game(width,height)
    return render_template('table.html',width = width,height = height,game = game)

@app.route('/step',methods=['POST'])
def step():
    from life import Game
    width = int(request.form.get('width'))
    height = int(request.form.get('height'))
    field = request.form.get('field')
    game = Game(width,height)
    game.deserialize(field)
    game.step()
    return render_template('table.html',width = width,height = height,game = game)

if __name__ == '__main__':
    app.run(debug=True)