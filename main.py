from flask import Flask
from functions.functions import get_candidates, get_candidates_for_id, get_candidates_for_skill

# создаем экземпляр Flask
app = Flask(__name__)


@app.route('/')
def page_home():
    """
        Функция обработки ответа при переходе на главную страницу
    Returns:
        str answer
    """
    return '<pre>\n' + get_candidates() + '<pre>'


@app.route('/candidates/<int:uid>/')
def page_candidates(uid):
    """
        функция обработки ответа при переходе на /candidates/<uid>
    Args:
        uid: переменная для получения искомого id

    Returns:
        str answer
    """
    return get_candidates_for_id(uid)


@app.route('/skills/<skill>/')
def page_skills(skill):
    """
        функция обработки ответа при переходе на skills/<skill>
    Args:
        skill: переменная для получения искомого skill

    Returns:
        str answer
    """
    return '<pre>\n' + get_candidates_for_skill(skill) + '<pre>'


if __name__ == '__main__':
    app.run()
