from flask import Flask
from functions.functions import get_all_candidates, get_candidates_for_id, get_candidates_for_skill, get_candidates

# создаем экземпляр Flask
app = Flask(__name__)


@app.route('/')
def page_home():
    """
        Функция обработки ответа при переходе на главную страницу
    Returns:
        str answer
    """
    candidates: list[dict] = get_all_candidates()
    return get_candidates(candidates)


@app.route('/candidates/<int:uid>/')
def page_candidates(uid):
    """
        функция обработки ответа при переходе на /candidates/<uid>
    Args:
        uid: переменная для получения искомого id

    Returns:
        str answer
    """
    candidate: dict | None = get_candidates_for_id(uid)
    if candidate is None:
        return ''
    return get_candidates([candidate])


@app.route('/skills/<skill>/')
def page_skills(skill):
    """
        функция обработки ответа при переходе на skills/<skill>
    Args:
        skill: переменная для получения искомого skill

    Returns:
        str answer
    """
    candidates: list[dict] = get_candidates_for_skill(skill)
    return get_candidates(candidates)


if __name__ == '__main__':
    app.run()
