# Добавьте в модуль с загадками функцию, которая принимает на вход строку (текст загадки) и
# число (номер попытки, с которой она угадана).
# Функция формирует словарь с информацией о результатах отгадывания.
# Для хранения используйте защищённый словарь уровня модуля.
# Отдельно напишите функцию, которая выводит результаты угадывания из защищённого словаря в удобном для чтения виде.
# Для формирования результатов используйте генераторное выражение.

def survey(dct: dict[str, list[str]], tries=3) -> dict:
    _dct_answers = {}
    for question, answers in dct.items():
        _dct_answers[question] = guess_answer(question, answers, tries)
    return _dct_answers


def print_answers(dct: dict[str, int]):
    [print(question, tries) for question, tries in dct.items()]