import json
import re
from collections import Counter


# Читаем объединенный файл с вакансиями из ТОП-10 городов

with open("pyskill/src/parced_data/merged_file.json", encoding="utf-8") as file:
    content = json.load(file)
    vac_amount = len(content)


# Требования к кандидату
requirements = []


# Фильтруем, оставляем только те вакансии, где есть требования к кандидату
for vac in content:
    if vac["requirement"] is None:
        continue
    requirements.append(vac["requirement"])


# Преобразуем все требования в текст

string_to_analyze = "".join(requirements)

# Разделяем текст на слова и сохраняем в список

words = re.findall(r"\w+", string_to_analyze.lower())

# Подсчитываем частоту слов и возвращаем
# словарь, где ключ - слово, значение - количество в тексте

word_count = Counter(words)

# Оставляем 400 наиболее встречающихся слов

most_common_words = word_count.most_common(400)


# Преобразуем данные в словарь, где ключ - слово, значение - частота его упоминания

parced_skills = {}
for item in most_common_words:
    parced_skills[item[0]] = item[1]


python_hard_skills = [
    "sql",
    "bash",
    "linux",
    "pandas",
    "postgresql",
    "docker",
    "git",
    "django",
    "numpy",
    "api",
    "powershell",
    "ci",
    "ml",
    "rest",
    "субд",
    "fastapi",
    "flask",
    "cd",
    "mysql",
    "html",
    "clickhouse",
    "ansible",
    "gitlab",
    "kubernetes",
    "css",
    "jenkins",
    "pytest",
    "scipy",
    "vba",
    "golang",
    "matplotlib",
    "nginx",
    "selenium",
    "jira",
    "pytorch",
    "oracle",
    "google",
    "grafana",
    "http",
    "unix",
    "tcp",
    "zabbix",
    "airflow",
    "spark",
    "postgres",
    "matlab",
    "kafka",
    "tensorflow",
    "confluence",
    "sklearn",
    "prometheus",
    "powerbi",
    "groovy",
    "redis",
    "aiohttp",
    "asyncio",
    "json",
    "scikit",
    "elk",
    "postman",
]


# Фильтруем данные от лишних слов, оставляем только hard skills

pure_skills = {}
for key in parced_skills:
    if key in python_hard_skills:
        pure_skills[key] = parced_skills[key]


for key, value in pure_skills.items():
    # Добавляем в словарь данные % вакансий, в которых встречается hard skill

    percentage = round(pure_skills[key] / vac_amount * 100, 1)
    total = [value, percentage]
    pure_skills[key] = total
