import os
import time

from django.core.management import BaseCommand

from pyskill.src.classes.JSON_saver import JSON_Saver
from pyskill.src.classes.hh import HH
from pyskill.src.utils import load_data_hh_obj


class Command(BaseCommand):
    """Команда для парсинга вакансий и записи в JSON-файл"""

    def handle(self, *args, **options):
        hh = HH()

        cities_id = [
            {1: "Москва"},
            {2: "Санкт-Петербург"},
            # {4: "Новосибирск"},
            # {3: "Екатеринбург"},
            # {88: "Казань"},
            # {66: "Нижний Новгород"},
            # {104: "Челябинск"},
            # {78: "Самара"},
            # {99: "Уфа"},
            # {76: "Ростов-на-Дону"},
        ]

        # Тут хранятся имена JSON-файлов с вакансиями по каждому городу

        JSON_FILES_STORE = os.path.join(
            "pyskill", "src", "parced_data", "vacancies_RF.txt"
        )

        for x in range(len(cities_id)):
            # Если файл уже есть
            if os.path.exists(JSON_FILES_STORE):
                with open(JSON_FILES_STORE, encoding="utf-8") as file:
                    content = file.readlines()

                    # Исключаем повторную запись

                    if len(content) >= len(cities_id):
                        print("Вы уже загрузили все вакансии с hh.ru!")
                        break

            # Парсим вакансии по городам из списка

            for key, value in cities_id[x].items():
                HH_CITY_ID = key
                KEY_WORD = "Python"
                filename = f"Вакансии python в г. {value}"

                # получаем вакансии по ключевому слову и id города

                vacancies = hh.get_vacancies(KEY_WORD, HH_CITY_ID)
                time.sleep(3)

                # Преобразуем данные для записи в json файл

                data_to_record = load_data_hh_obj(vacancies)

                js_obj = JSON_Saver(filename)

                # Записываем вакансии по каждому городу в отельный json файл

                js_obj.save_to_JSON(data_to_record)

                # Записывает имена JSON-файлов в один txt - файл

                js_obj.save_filenames()

                # Объединяем вакансии по всем городам в один JSON

                js_obj.get_union_json()
