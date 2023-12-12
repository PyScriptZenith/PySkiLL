import json
from abc import ABC, abstractmethod


class File_Saver(ABC):
    @abstractmethod
    def __init__(self, filename):
        pass

class JSON_Saver(File_Saver):

    def __init__(self, filename: str):
        self.filename = filename

    def save_to_JSON(self, data: list):
        with open(f'pyskill\src\parced_data\{self.filename}.json', 'w', encoding='utf-8') as file:
            json.dump(data, file, indent=4, ensure_ascii=False)


    def save_filenames(self):
        with open('pyskill\src\parced_data\\vacancies_RF.txt', 'a', encoding='utf-8') as file:
            data = f"pyskill\src\parced_data\{self.filename}.json"
            file.write(f'{data}\n')


    def get_union_json(self):
        with open('pyskill\src\parced_data\\vacancies_RF.txt', "r", encoding='utf-8') as outfile:
            files_to_merge = [line.strip() for line in outfile.readlines()]
        merged_data = []
        for file_name in files_to_merge:
            with open(file_name, 'r', encoding='utf-8') as file:
                # Загрузка данных из текущего файла
                data = json.load(file)

                # Объединение данных в список merged_data
                merged_data.extend(data)

        with open('pyskill\src\parced_data\\merged_file.json', 'w', encoding='utf-8') as merged_file:
            json.dump(merged_data, merged_file, indent=2, ensure_ascii=False)






