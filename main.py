from os.path import join, abspath
from flask import Flask
from functions.functions import load_json

app = Flask(__name__)
path_file = abspath(join('files', 'candidates.json'))
DATA = load_json(path_file)


@app.route('/')
def page_home(answer=''):
    for line in DATA:
        answer += f'Имя кандидата - {line["name"]}\n' \
                  f'Позиция кандидата - {line["position"]}\n' \
                  f'Навыки - {line["skills"]}\n\n'
    return '<pre>\n' + answer + '<pre>'


@app.route('/candidates/<int:uid>/')
def page_candidates(uid, answer=''):
    for line in DATA:
        if line["id"] == uid:
            answer += f'<img src = "www.ya.ru/{uid}">\n\n' \
                     f'<pre>\nИмя кандидата - {line["name"]}\n' \
                     f'Позиция кандидата - {line["position"]}\n' \
                     f'Навыки - {line["skills"]}\n<pre>'
            return answer


@app.route('/skills/<skill>/')
def page_skills(skill, answer=''):
    for line in DATA:
        if skill.lower() in map(str.lower, line["skills"].split(',')):
            answer += f'Имя кандидата - {line["name"]}\n' \
                      f'Позиция кандидата - {line["position"]}\n' \
                      f'Навыки - {line["skills"]}\n\n'
    return '<pre>\n' + answer + '<pre>'


app.run()
