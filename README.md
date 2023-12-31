# PySkill: Сервис аналитики навыков Python-разработчика
Pyskill помогает начинающим Python – разработчикам лучше ориентироваться в стремительно меняющемся рынке IT. Здесь ты получишь живую аналитику по тем HARD SKILL, который актуальны именно на сегодняшний день. Приложение анализирует все вакансии Python-разработчика в ТОП-10 городов России.

## Логика работы сервиса:

- подключаемся к API hh.ru
- парсим вакансии Python – разработчика
- смотрим требования к кандидату
- выделяем ключевые хард скиллы и делаем по ним аналитику
## Исползуемые технологии
  * API
  * django
  * PostgreSQL
  * Bootstrap
  * JSON
  * ООП


## Сущности системы
  ### Рассылка
  * почта для получения аналитики

### Пользователь
* почта
* пароль
* телефон 
* страна 


## Как использовать данный проект?

- Убедитесь, что у вас установлен docker и docker-compose
- Склонировать репозиторий и перейти в директорию
  
  В терминале ввести команды
  ```
  git clone https://github.com/PyScriptZenith/PySkiLL
  ```
  ```
  cd PySkiLL/
  ```
- Создать файл ``.env``, который необходимо заполнить данными из файла ``env.sample``
- Запустить проект
  
  В терминале ввести команду
  ```
  docker-compose up --build
  ```
- Откройте браузер и перейдите по адресу http://localhost:8000 для доступа к приложению.

## Контакты

Если у Вас возникли вопросы или пожелания по развитию проекта, пожалуйста, свяжитесь со мной.

tg: opensda91