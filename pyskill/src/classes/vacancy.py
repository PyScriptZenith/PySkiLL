class Vacancy:
    All_vacancies = []

    def __init__(self, name: str, pay: int, requirement: str, city: str, url=None):
        self._name = name
        self._url = url
        self._pay = pay
        self._requirement = requirement
        self._city = city

        Vacancy.All_vacancies.append(self)

    @property
    def name(self):
        return self._name

    @property
    def city(self):
        return self._city

    @property
    def url(self):
        return self._url

    @property
    def pay(self):
        return self._pay

    @property
    def requirement(self):
        return self._requirement

    def __str__(self):
        return f"{self.name}"

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.url}, {self.pay})"

    def to_json(self):
        """Преобразуем данные для записи в JSON - файл"""

        return {
            "name": self.name,
            "url": self.url,
            "pay": self.pay,
            "requirement": self.requirement,
            "city": self.city,
        }

    def __gt__(self, other):
        return self.pay > other.pay

    def __lt__(self, other):
        return self.pay < other.pay
