import time

from django.core.management import BaseCommand

from pyskill.src.classes.JSON_saver import JSON_Saver
from pyskill.src.classes.hh import HH
from pyskill.src.utils import load_data_hh_obj


class Command(BaseCommand):
    def handle(self, *args, **options):

        hh = HH()

        cities_id = [{1: "Москва"},
                     {2: "Санкт-Петербург"},
                     {4: "Новосибирск"},
                     {3: "Екатеринбург"},
                     {88: "Казань"},
                     {66: "Нижний Новгород"},
                     {104: "Челябинск"},
                     {78: "Самара"},
                     {99: "Уфа"},
                     {76: "Ростов-на-Дону"},
                     ]
        # Москва

        for x in range(len(cities_id)):
            for key, value in cities_id[x].items():
                hh_city_id = key

                key_word = 'Python'

                filename = f'Вакансии python в г. {value}'

                # получаем вакансии по ключевому слову и id города

                vacancies = hh.get_vacancies(key_word, hh_city_id)

                time.sleep(3)

                # Преобразуем данные для записи в json файл

                data_to_record = load_data_hh_obj(vacancies)

                js_obj = JSON_Saver(filename)

                # Записываем данные в json файл
                js_obj.save_to_JSON(data_to_record)

                js_obj.save_filenames()

                js_obj.get_union_json()
