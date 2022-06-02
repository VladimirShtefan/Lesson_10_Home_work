from json import load
from os.path import join, abspath


def load_json(file_name: str) -> list:
    with open(file_name) as file:
        data = load(file)
    return data


path_file = abspath(join('files', 'candidates.json'))
DATA = load_json(path_file)


def get_candidates() -> str:
    answer = ''
    for line in DATA:
        answer += f'Имя кандидата - {line["name"]}\n' \
                  f'Позиция кандидата - {line["position"]}\n' \
                  f'Навыки - {line["skills"]}\n\n'
    return answer


def get_candidates_for_id(uid: int) -> str:
    answer = ''
    for line in DATA:
        if line["id"] == uid:
            answer += f'<img src = "www.ya.ru/{uid}">\n\n' \
                      f'<pre>\nИмя кандидата - {line["name"]}\n' \
                      f'Позиция кандидата - {line["position"]}\n' \
                      f'Навыки - {line["skills"]}\n<pre>'
            return answer
    return ''


def get_candidates_for_skill(skill: str) -> str:
    answer = ''
    for line in DATA:
        if skill.lower() in map(str.lower, line["skills"].split(',')):
            answer += f'Имя кандидата - {line["name"]}\n' \
                      f'Позиция кандидата - {line["position"]}\n' \
                      f'Навыки - {line["skills"]}\n\n'
    return answer
