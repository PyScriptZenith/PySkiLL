import requests


class HH:
    """
    Класс позволяет собирать информацию о вакансиях с платформы hh.ru
    """

    def __init__(self, name="hh"):
        self.name = name

    def get_vacancies(self, key_word: str, area_id: int):
        """
        Получаем вакансии с hh.ru с заданными параметрами
        :param key_word: ключевое слово для поискового запроса
        :param area_id: id города
        :return: список словарей с вакансиями
        """

        def get_data(page=1):
            """
            Внутрення функция - парсим данные о вакансиях постранично
            :param page: номер страницы
            """

            # Делаем get запрос с необходимыми параметрами
            # и получаем данные в json формате

            self.params = {
                "text": key_word,
                "area": area_id,
                "pages": 20,
                "page": page,
                "per_page": 100,
            }
            self.response = requests.get("https://api.hh.ru/vacancies", self.params)
            self.response_json = self.response.json()
            return self.response_json

        self.data_store = []
        total = 0
        for page in range(0, 15):
            self.content = get_data(page)
            self.data_store.extend(self.content["items"])
            total += 100
            print("Загружаются данные с hh.ru: 100 вакансий загружено")
            print(f"ИТОГО {total}")
        return self.data_store
