from pyskill.src.classes.vacancy import Vacancy


def load_data_hh_obj(clear_data):
    """
    Загружаем данные о вакансиях с hh.ru в объекты класса Vacancy

    :param clear_data: список словарей с вакансиями
    :return: список словарей с атрибутами объекта класса Vacancy
    """
    data_js_obj = []
    for x in range(len(clear_data)):
        name = clear_data[x]["name"]
        url = clear_data[x]["alternate_url"]
        requirement = clear_data[x]["snippet"]["requirement"]
        city = clear_data[x]["area"]["name"]
        if clear_data[x]["salary"] is None:
            pay = None
        else:
            pay = clear_data[x]["salary"]["from"]

        vacancy = Vacancy(name, pay, requirement, city, url)
        data_js_obj.append(vacancy.to_json())

    return data_js_obj
