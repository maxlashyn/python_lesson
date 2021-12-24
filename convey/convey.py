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

from flask import Blueprint, render_template,request,url_for

convey_blueprint = Blueprint('convey', __name__, template_folder='templates')


@convey_blueprint.route('/', methods=['GET'])
def start():
    return render_template('convey/game_convey.html')


@convey_blueprint.route('/ method="post"', methods=['POST'])
def init_game():
    from convey.life import Game
    width = int(request.form.get('width'))
    height = int(request.form.get('height'))
    game = Game(width,height)
    return render_template('convey/table.html', width = width, height = height, game = game)

@convey_blueprint.route('/step',methods=['POST'])
def step():
    from convey.life import Game
    width = int(request.form.get('width'))
    height = int(request.form.get('height'))
    field = request.form.get('field')
    game = Game(width,height)
    game.deserialize(field)
    game.step()
    return render_template('convey/table.html', width = width, height = height, game = game)

