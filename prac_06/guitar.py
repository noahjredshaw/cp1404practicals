"""
Estimated time: 20
Actual time:
"""
import datetime

CURRENT_DATE = datetime.datetime.now().year
VINTAGE_YEAR_THRESHOLD = 50


class Guitar:
    def __init__(self, name="", year=0, cost=0.0):
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        return f"{self.name} ({self.year}) : ${self.cost:.2f}"

    def get_age(self):
        return CURRENT_DATE - self.year

    def is_vintage(self):
        return self.get_age() >= VINTAGE_YEAR_THRESHOLD

