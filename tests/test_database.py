from praktikum.database import Database
from data import test_buns, test_ingredients


class TestDatabase:

    def test_buns_amount(self):
        database = Database()
        assert len(database.buns) == 3

    def test_available_buns_list_is_correct(self):
        database = Database()
        database.available_buns() == test_buns

    def test_ingredients_amount(self):
        database = Database()
        assert len(database.ingredients) == 6

    def test_available_ingredients_list_is_correct(self):
        database = Database()
        database.available_ingredients() == test_ingredients
