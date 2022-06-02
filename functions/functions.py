from json import load
from os.path import join, abspath


def load_json() -> list[dict]:
    path_file = abspath(join('files', 'candidates.json'))
    with open(path_file) as file:
        data = load(file)
    return data


def get_candidates(candidates: list[dict]) -> str:
    answer = '<pre>\n'
    for candidate in candidates:
        answer += f'Имя кандидата - {candidate["name"]}\n' \
                  f'Позиция кандидата - {candidate["position"]}\n' \
                  f'Навыки - {candidate["skills"]}\n\n'
    answer += '<pre>'
    return answer


def get_all_candidates() -> list[dict]:
    return load_json()


def get_candidates_for_id(uid: int) -> dict | None:
    candidates = get_all_candidates()
    for candidate in candidates:
        if candidate["id"] == uid:
            return candidate


def get_candidates_for_skill(skill: str) -> list[dict]:
    answer = []
    candidates = get_all_candidates()
    for candidate in candidates:
        if skill in candidate["skills"].lower().split(', '):
            answer.append(candidate)
    return answer
