from datetime import datetime
from django.core.exceptions import ValidationError

FIRST_CUP_YEAR = 1930

cup_years = list(range(FIRST_CUP_YEAR, datetime.now().year, 4))
cup_years.remove(1942)
cup_years.remove(1946)


class NegativeTitlesError(Exception):
    def __init__(self, message):
        self.message = message


class InvalidYearCupError(Exception):
    def __init__(self, message):
        self.message = message


class ImpossibleTitlesError(Exception):
    def __init__(self, message):
        self.message = message


def validate_title(title):
    if title < 0:
        raise NegativeTitlesError("titles cannot be negative")


def validate_first_cup(first_cup):
    if not datetime.strptime(first_cup, "%Y-%m-%d").year in cup_years:
        raise InvalidYearCupError("there was no world cup this year")


def validate_impossible_titles(titles, first_cup):
    first_cup_index = cup_years.index(datetime.strptime(first_cup, "%Y-%m-%d").year)

    if titles > len(cup_years[first_cup_index:]):
        raise ImpossibleTitlesError("impossible to have more titles than disputed cups")


# date_string = data["first_cup"]
# date_object = datetime.strptime(date_string, "%Y-%m-%d")
# cup_years = list(range(date_object.year, datetime.now().year, 4))
