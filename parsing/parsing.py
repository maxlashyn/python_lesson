"""
спарсить со странички https://kttc.ru/wot/ru/clans/ названия кланов и
с помощью фласка вывести их на нашей страничке в теге <ul><li>
"""
from bs4 import BeautifulSoup
import requests
from flask import Blueprint, render_template, request

parsing_blueprint = Blueprint('parsing', __name__, template_folder='templates')

@parsing_blueprint.route('/', methods=['GET'])
def parse():
    return render_template('parsing/parsing.html', clans_name = clans_name())

def clans_name():
    response = requests.get("https://kttc.ru/wot/ru/clans/")
    bs = BeautifulSoup(response.content, 'html.parser')
    clans = bs.select('span.clanNameStat')
    clan_names = list()
    for clan in clans:
        link = clan.select('a')
        clan_names.append(link[0].get_text())
    return clan_names