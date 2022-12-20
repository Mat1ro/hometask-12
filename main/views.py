from flask import Blueprint, render_template, request
from functions import *
from json import JSONDecodeError
import logging

main_blueprint = Blueprint('main_blueprint', __name__, template_folder='templates')


@main_blueprint.route("/")
def page_main():
    return render_template('index.html')


@main_blueprint.route('/search/')
def page_search():
    query = request.args.get('s', '')
    logging.info('Выполняю поиск')
    try:
        posts = get_by_word(query)
    except FileNotFoundError:
        logging.error('Фай не найден')
        return 'Файл не найден'
    except JSONDecodeError:
        return 'Невалидный файл'
    return render_template('post_list.html', query=query, posts=posts)
