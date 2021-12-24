from flask import Blueprint, render_template, request

gallows_blueprint = Blueprint('gallows', __name__, template_folder='templates')

"""
1. создать экшен который выведет html-форму содержащую
поле для ввода слова (type="text"), поле для ввода количества жизней (type='number')
и кнопку с текстом "старт" которая будет отправлять содержимое формы

2. создать экшен который будет инициализировать игру переданными словом и жизнями
и выводить форму в которой 
- будет readonly поле содержащее текущее количество жизней
- будет readonly поле содержащее guess_chars (для  удобства дальнейшей обработки символы разделены пробелами) ' '.join(guess_chars)
- будет содержать скрытое поле в котором будет храниться введеное слово
- будет содержать текстовое поле ввода для ввода следующей буквы
- будет содержать кнопу "отправить"

3. создать экшен который будет по переданным данным создавать новый объект игры
подставлять guess_chars, делать шаг в игре и возвращать форму из п.2 если не проигрыш или выигрышь, 
в противном случае возвращать другой шаблон с результатом игры
"""


# 1
@gallows_blueprint.route('/', methods=['GET'])
def start():
    return render_template('gallows/game.html')


@gallows_blueprint.route('/init', methods=['POST'])
def init():
    from gallows.gallows_with_functions import Game, Word, Life
    word = request.form.get('input_word').lower().strip(' ')
    life = int(request.form.get('input_life'))
    game = Game(Word(word), Life(life))
    return render_template('gallows/step.html', word=word, life=life, guess_chars=" ".join(game.get_guess_chars()))


@gallows_blueprint.route('/step', methods=['POST'])
def step():
    from gallows.gallows_with_functions import Game, Word, Life
    word = request.form.get('word')
    life = int(request.form.get('life'))
    guess_chars = request.form.get('guess_chars')
    game = Game(Word(word), Life(life))
    game.set_guess_chars(guess_chars.split(' '))
    char = request.form.get('char').lower().strip(' ')
    game.step(char)
    if game.is_win():
        return render_template('gallows/win.html')
    if game.is_loose():
        return render_template('gallows/loose.html')
    return render_template('gallows/step.html', word=word, life=game.get_life(), guess_chars=" ".join(game.get_guess_chars()))



