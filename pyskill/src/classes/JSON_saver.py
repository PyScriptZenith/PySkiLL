import json
import os


class JSON_Saver:
    PARCED_DATA_PATH = os.path.join("pyskill", "src", "parced_data")

    VACANCIES_RF_PATH = os.path.join(
        "pyskill", "src", "parced_data", "vacancies_RF.txt"
    )
    MERGED_JSON_PATH = os.path.join("pyskill", "src", "parced_data", "merged_file.json")

    def __init__(self, filename: str):
        self.filename = filename

    def save_to_JSON(self, data: list):
        """Записывает вакансии в JSON"""

        with open(
                f"{self.PARCED_DATA_PATH}\\{self.filename}.json", "w", encoding="utf-8"
        ) as file:
            json.dump(data, file, indent=4, ensure_ascii=False)

    def save_filenames(self):
        """Записывает имена JSON-файлов в txt"""

        with open(self.VACANCIES_RF_PATH, "a", encoding="utf-8") as file:
            data = f"{self.PARCED_DATA_PATH}\\{self.filename}.json"
            file.write(f"{data}\n")

    def get_union_json(self):
        """Создает единый JSON со всеми вакансиями по ТОП-10 городов"""

        with open(self.VACANCIES_RF_PATH, "r", encoding="utf-8") as outfile:
            files_to_merge = [line.strip() for line in outfile.readlines()]
        merged_data = []
        for file_name in files_to_merge:
            with open(file_name, "r", encoding="utf-8") as file:
                # Загружаем данные из текущего файла
                data = json.load(file)

                # Объединяем данных в список merged_data
                merged_data.extend(data)

        with open(self.MERGED_JSON_PATH, "w", encoding="utf-8") as merged_file:
            json.dump(merged_data, merged_file, indent=2, ensure_ascii=False)
