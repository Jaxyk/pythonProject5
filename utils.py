import json


def load_candidates():
    """
    Загрузка данных из файла
    """
    with open('candidates.json', 'r', encoding='utf-8') as file:
        return json.load(file)


def get_all():
    """
    Показать всех кандидатов
    """
    return load_candidates()


def get_candidate_by_pk(pk):
    """
    Показать кандидата по номеру
    """
    for candidate in load_candidates():
        if candidate['id'] == pk:
            return candidate
    return


def get_candidate_by_skill(skill):
    """
    Показать кандидатов по навыку
    """
    candidates = []
    for candidate in load_candidates():
        if skill.lower() in candidate['skills'].lower().split(', '):
            candidates.append(candidate)
    return candidates